import argparse
import os
import sys
from pathlib import Path

import pandas as pd


def discover_input_path(cli_input: str | None = None) -> Path | None:
    """Return first available input CSV path from CLI, Kaggle, or local fallbacks."""
    candidates: list[Path] = []

    if cli_input:
        candidates.append(Path(cli_input))

    script_dir = Path(__file__).resolve().parent

    candidates.extend(
        [
            Path("/kaggle/input/tetuan-city-power-consumption/Tetuan City power consumption.csv"),
            Path("/kaggle/input/tetuan-city-power-consumption/tetuan city power consumption.csv"),
            Path("data/Tetuan City power consumption.csv"),
            Path("data/tetuan_city_power_consumption.csv"),
            Path("Tetuan City power consumption.csv"),
            script_dir / "data" / "Tetuan City power consumption.csv",
            script_dir / "data" / "tetuan_city_power_consumption.csv",
        ]
    )

    for path in candidates:
        if path.exists():
            return path
    return None


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize known column naming variants to one canonical schema."""
    rename_map = {
        "Datetime": "DateTime",
        "date_time": "DateTime",
        "date": "DateTime",
        "Zone 1 Power Consumption": "Zone 1 Power Consumption",
        "Zone 2  Power Consumption": "Zone 2 Power Consumption",
        "Zone 3  Power Consumption": "Zone 3 Power Consumption",
    }
    return df.rename(columns=rename_map)


def prepare_data(input_path: Path, output_path: Path) -> pd.DataFrame:
    """Load raw 10-minute data, clean schema, and export hourly features."""
    print(f"Loading data from: {input_path}")
    df = pd.read_csv(input_path)
    df = normalize_columns(df)

    if "DateTime" not in df.columns:
        raise ValueError("Missing required datetime column. Expected a 'DateTime' field.")

    df["DateTime"] = pd.to_datetime(df["DateTime"], errors="coerce")
    df = df.dropna(subset=["DateTime"]).set_index("DateTime").sort_index()

    numeric_cols = df.select_dtypes(include=["number"]).columns
    if numeric_cols.empty:
        raise ValueError("No numeric columns available for hourly aggregation.")

    print(f"Raw rows: {len(df):,}")
    hourly = df[numeric_cols].resample("h").mean().dropna(how="all")
    hourly = hourly.interpolate(method="time", limit_direction="both")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    hourly.to_csv(output_path)
    print(f"Hourly rows: {len(hourly):,}")
    print(f"Saved hourly dataset to: {output_path}")
    return hourly


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare Tetuan City Power hourly dataset.")
    parser.add_argument(
        "--input",
        type=str,
        default=None,
        help="Optional path to raw Tetuan CSV. If omitted, auto-detect Kaggle/local paths.",
    )
    parser.add_argument(
        "--output",
        type=str,
        default="data/hourly_tetuan_power.csv",
        help="Output CSV path for the cleaned hourly dataset.",
    )
    args = parser.parse_args()

    input_path = discover_input_path(args.input)
    if input_path is None:
        print("=" * 72)
        print("ERROR: Tetuan dataset not found.")
        print("Download from: https://www.kaggle.com/datasets/gmkeshav/tetuan-city-power-consumption")
        print("Then place CSV at: data/Tetuan City power consumption.csv")
        print("Or pass an explicit path with: python generate_dataset.py --input <path>")
        print("=" * 72)
        return 1

    try:
        prepare_data(input_path=input_path, output_path=Path(args.output))
    except Exception as exc:
        print(f"ERROR during dataset preparation: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
