"""
IPL Data Update Automation Script
This script checks for new IPL data and updates the database automatically.
Run this script periodically to keep your dashboard fresh with latest data.
"""

import os
import sys
import pandas as pd
import sqlite3
from datetime import datetime, timedelta
import logging

# Add scripts directory to path
sys.path.append(os.path.dirname(__file__))

from extract import extract_data
from transform import transform_data
from load import load_data_to_db

# Set up logging
logging.basicConfig(
    filename='data/update_log.txt',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_for_new_data(csv_path="data/raw/cricket_data_2025.csv"):
    """
    Check if there's new data available
    For now, we'll simulate this by checking file modification time
    In production, you might check an API or website for updates
    """
    if not os.path.exists(csv_path):
        logging.warning(f"Data file {csv_path} not found")
        return False

    # Check if file was modified in the last 24 hours
    file_modified = datetime.fromtimestamp(os.path.getmtime(csv_path))
    time_since_update = datetime.now() - file_modified

    # If file was updated recently, assume there's new data
    if time_since_update < timedelta(hours=24):
        logging.info(f"New data detected in {csv_path} (modified {time_since_update} ago)")
        return True

    logging.info("No new data detected")
    return False

def update_database():
    """
    Main function to update the database with new data
    """
    try:
        logging.info("Starting automated database update")

        # Check for new data
        csv_path = "data/raw/cricket_data_2025.csv"
        if not check_for_new_data(csv_path):
            logging.info("No update needed - data is current")
            return True

        # Extract
        logging.info("Extracting data...")
        df_raw = extract_data(csv_path)

        # Transform
        logging.info("Transforming data...")
        df_clean = transform_data(df_raw)

        # Load
        logging.info("Loading data to database...")
        db_path = "data/ipl_stats.db"
        table_name = "player_stats"
        load_data_to_db(df_clean, db_path, table_name)

        # Update timestamp file
        with open("data/last_updated.txt", "w") as f:
            f.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

        logging.info("Database update completed successfully")
        return True

    except Exception as e:
        logging.error(f"Database update failed: {str(e)}")
        return False

def send_notification(success, update_type="scheduled"):
    """
    Send notification about update status
    For now, we'll just log it. You could extend this to send emails or desktop notifications.
    """
    if success:
        message = f"✅ IPL Dashboard {update_type} update completed successfully"
    else:
        message = f"❌ IPL Dashboard {update_type} update failed - check logs"

    logging.info(message)
    print(message)  # Also print to console for immediate feedback

if __name__ == "__main__":
    print("🔄 Starting IPL Data Update Automation")
    print("=" * 50)

    success = update_database()
    send_notification(success, "manual")

    if success:
        print("✅ Update completed successfully!")
    else:
        print("❌ Update failed - check data/update_log.txt for details")

    print("=" * 50)