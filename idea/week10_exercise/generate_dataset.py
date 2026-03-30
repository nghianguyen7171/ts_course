import os
import sys
import pandas as pd
import argparse

def get_data_path():
    """Check for the dataset in typical Kaggle and local locations."""
    # Kaggle path
    kaggle_path = "/kaggle/input/tetuan-city-power-consumption/Tetuan City power consumption.csv"
    
    # Local paths to check
    local_paths = [
        "data/Tetuan City power consumption.csv",
        "data/tetuan_city_power_consumption.csv",
        "../data/Tetuan City power consumption.csv",
        "Tetuan City power consumption.csv"
    ]
    
    if os.path.exists(kaggle_path):
        return kaggle_path
        
    for p in local_paths:
        if os.path.exists(p):
            return p
            
    return None

def prepare_data(input_path, output_path="data/hourly_tetuan_power.csv"):
    """Load the raw 10-minute dataset and resample to hourly."""
    print(f"Loading data from {input_path}...")
    df = pd.read_csv(input_path)
    
    # Check if Datetime column exists
    if 'DateTime' in df.columns:
        df['DateTime'] = pd.to_datetime(df['DateTime'])
        df.set_index('DateTime', inplace=True)
    else:
        print("Error: 'DateTime' column not found.")
        return False
        
    print("Original shape:", df.shape)
    print("Resampling to hourly frequency...")
    
    # Resample to hourly and take the mean
    # Numeric columns will be averaged
    numeric_cols = df.select_dtypes(include=['number']).columns
    df_hourly = df[numeric_cols].resample('H').mean()
    
    # Drop rows with NaN that might have been created by resampling gaps
    df_hourly = df_hourly.dropna()
    print("Hourly shape:", df_hourly.shape)
    
    # Ensure output directory exists
    os.makedirs(os.path.dirname(output_path) if os.path.dirname(output_path) else ".", exist_ok=True)
    
    # Save the prepared data
    df_hourly.to_csv(output_path)
    print(f"Saved prepared hourly data to {output_path}")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prepare Tetuan City Power dataset.")
    parser.add_argument("--output", type=str, default="data/hourly_tetuan_power.csv", help="Output path for hourly data")
    args = parser.parse_args()
    
    path = get_data_path()
    if path:
        print(f"Found dataset at: {path}")
        success = prepare_data(path, args.output)
        if not success:
            sys.exit(1)
    else:
        print("="*60)
        print("ERROR: Dataset not found!")
        print("="*60)
        print("Please download the 'Tetuan City Power Consumption' dataset from Kaggle:")
        print("URL: https://www.kaggle.com/datasets/gmkeshav/tetuan-city-power-consumption")
        print("\nIf you are on local, create a 'data' folder and place the CSV file there:")
        print("  data/Tetuan City power consumption.csv")
        print("\nIf you are on Kaggle, ensure you have added the dataset to your input.")
        print("="*60)
        sys.exit(1)
