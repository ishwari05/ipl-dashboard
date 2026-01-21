import pandas as pd

def extract_data(file_path):
    df = pd.read_csv(file_path)
    print("✅ Data extracted")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    return df

if __name__ == "__main__":
    df = extract_data("data/raw/cricket_data_2025.csv")
    print(df.head())
