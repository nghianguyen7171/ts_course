"""Prepare the Beijing PM2.5 Air Quality dataset for Week 13 lab.

Downloads / discovers the raw CSV (Kaggle or local), parses datetime from
year/month/day/hour columns, handles missing values, and exports a clean
hourly CSV ready for the notebook.
"""

import argparse
import sys
from pathlib import Path

import pandas as pd


def discover_input_path(cli_input: str | None = None) -> Path | None:
    """Return the first available raw CSV path."""
    candidates: list[Path] = []

    if cli_input:
        candidates.append(Path(cli_input))

    script_dir = Path(__file__).resolve().parent

    candidates.extend(
        [
            Path("/kaggle/input/beijing-pm2-5-data-data-set/PRSA_data_2010.1.1-2014.12.31.csv"),
            Path("/kaggle/input/beijing-pm25-data/PRSA_data_2010.1.1-2014.12.31.csv"),
            Path("data/PRSA_data_2010.1.1-2014.12.31.csv"),
            Path("data/PRSA_data.csv"),
            script_dir / "data" / "PRSA_data_2010.1.1-2014.12.31.csv",
            script_dir / "data" / "PRSA_data.csv",
        ]
    )

    for path in candidates:
        if path.exists():
            return path
    return None


def prepare_data(input_path: Path, output_path: Path) -> pd.DataFrame:
    """Load raw Beijing PM2.5 data, clean, and export hourly CSV."""
    print(f"Loading data from: {input_path}")
    df = pd.read_csv(input_path)

    df["datetime"] = pd.to_datetime(
        df[["year", "month", "day", "hour"]], errors="coerce"
    )
    df = df.dropna(subset=["datetime"]).set_index("datetime").sort_index()

    drop_cols = [c for c in ["No", "year", "month", "day", "hour"] if c in df.columns]
    df = df.drop(columns=drop_cols)

    rename_map = {
        "pm2.5": "pm25",
        "DEWP": "dewpoint",
        "TEMP": "temperature",
        "PRES": "pressure",
        "Iws": "wind_speed",
        "Is": "snow_hours",
        "Ir": "rain_hours",
        "cbwd": "wind_dir",
    }
    df = df.rename(columns={k: v for k, v in rename_map.items() if k in df.columns})

    if "pm25" in df.columns:
        missing_before = df["pm25"].isna().sum()
        df["pm25"] = df["pm25"].interpolate(method="time", limit_direction="both")
        print(f"PM2.5 missing values filled: {missing_before}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path)
    print(f"Rows: {len(df):,}")
    print(f"Columns: {list(df.columns)}")
    print(f"Saved to: {output_path}")
    return df


def main() -> int:
    parser = argparse.ArgumentParser(description="Prepare Beijing PM2.5 dataset.")
    parser.add_argument("--input", type=str, default=None, help="Path to raw CSV.")
    parser.add_argument(
        "--output",
        type=str,
        default="data/beijing_air_quality.csv",
        help="Output CSV path.",
    )
    args = parser.parse_args()

    input_path = discover_input_path(args.input)
    if input_path is None:
        print("=" * 72)
        print("ERROR: Beijing PM2.5 dataset not found.")
        print("Download from: https://www.kaggle.com/datasets/djhaveri/beijing-pm2-5-data-data-set")
        print("Then place CSV at: data/PRSA_data_2010.1.1-2014.12.31.csv")
        print("Or pass an explicit path with: python generate_dataset.py --input <path>")
        print("=" * 72)
        return 1

    try:
        prepare_data(input_path=input_path, output_path=Path(args.output))
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
