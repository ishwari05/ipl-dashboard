import sqlite3
import pandas as pd

def load_data_to_db(df, db_path="data/ipl_stats.db", table_name="player_stats"):
    """
    Loads the transformed DataFrame into a SQLite database.
    Creates the table if it doesn't exist.
    """
    print("Starting data load...")

    # Connect to SQLite database (creates it if it doesn't exist)
    conn = sqlite3.connect(db_path)

    try:
        # Load data into the database
        # if_exists='replace' will drop the table if it exists and create a new one
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        print(f"✅ Data loaded into table '{table_name}' in database '{db_path}'")

        # Verify by showing row count
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        row_count = cursor.fetchone()[0]
        print(f"Total rows in database: {row_count}")

    except Exception as e:
        print(f"❌ Error loading data: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    # For testing - load sample data
    # In real pipeline, this will be called from main script
    df_sample = pd.DataFrame({
        'Year': [2024, 2023],
        'Player_Name': ['Test Player 1', 'Test Player 2'],
        'Runs_Scored': [100, 200]
    })
    load_data_to_db(df_sample)