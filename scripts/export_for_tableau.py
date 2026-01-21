import sqlite3
import pandas as pd

def export_to_csv(db_path="data/ipl_stats.db", table_name="player_stats", csv_path="data/ipl_stats_for_tableau.csv"):
    """
    Exports data from SQLite database to CSV for Tableau
    """
    print("Exporting data to CSV for Tableau...")

    # Connect to database
    conn = sqlite3.connect(db_path)

    try:
        # Read data into pandas DataFrame
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, conn)

        # Export to CSV
        df.to_csv(csv_path, index=False)
        print(f"✅ Data exported to {csv_path}")
        print(f"   Rows: {df.shape[0]}, Columns: {df.shape[1]}")

    except Exception as e:
        print(f"❌ Error exporting data: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    export_to_csv()