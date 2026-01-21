"""
IPL Player Statistics ETL Pipeline
This script runs the complete ETL process:
1. Extract: Read raw data from CSV
2. Transform: Clean and transform the data
3. Load: Store cleaned data in SQLite database
"""

import sys
import os
sys.path.append(os.path.dirname(__file__))  # Add scripts folder to path

from extract import extract_data
from transform import transform_data
from load import load_data_to_db

def run_etl_pipeline():
    """
    Main function to run the ETL pipeline
    """
    print("🚀 Starting IPL Player Statistics ETL Pipeline")
    print("=" * 50)

    try:
        # Step 1: Extract
        print("\n📥 STEP 1: EXTRACT")
        raw_data_path = "data/raw/cricket_data_2025.csv"
        df_raw = extract_data(raw_data_path)

        # Step 2: Transform
        print("\n🔄 STEP 2: TRANSFORM")
        df_clean = transform_data(df_raw)

        # Step 3: Load
        print("\n💾 STEP 3: LOAD")
        db_path = "data/ipl_stats.db"
        table_name = "player_stats"
        load_data_to_db(df_clean, db_path, table_name)

        print("\n🎉 ETL Pipeline completed successfully!")
        print("=" * 50)

        # Optional: Show some basic stats
        print(f"📊 Pipeline Summary:")
        print(f"   - Raw data rows: {df_raw.shape[0]}")
        print(f"   - Clean data rows: {df_clean.shape[0]}")
        print(f"   - Columns: {df_clean.shape[1]}")
        print(f"   - Database: {db_path}")
        print(f"   - Table: {table_name}")

    except Exception as e:
        print(f"❌ ETL Pipeline failed: {e}")
        return False

    return True

if __name__ == "__main__":
    success = run_etl_pipeline()
    if success:
        print("\n✅ Ready for downstream analysis!")
    else:
        print("\n❌ Please check the errors above and try again.")