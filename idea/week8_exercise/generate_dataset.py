"""
Fetch the classic AirPassengers dataset and save locally.
Source: R datasets::AirPassengers via statsmodels.
Run once and commit data/air_passengers.csv.
"""
import pandas as pd
from pathlib import Path
from statsmodels.datasets import get_rdataset

raw = get_rdataset("AirPassengers", "datasets").data

dates = pd.date_range(start="1949-01-01", periods=len(raw), freq="MS")
df = pd.DataFrame({
    "date": dates,
    "Passengers": raw.iloc[:, -1].values,
})

out_dir = Path(__file__).resolve().parent / "data"
out_dir.mkdir(parents=True, exist_ok=True)
out_path = out_dir / "air_passengers.csv"
df.to_csv(out_path, index=False)
print(f"Saved {len(df)} rows to {out_path}")
