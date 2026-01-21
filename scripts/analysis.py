import sqlite3
import pandas as pd

def connect_to_db(db_path="data/ipl_stats.db"):
    """Connect to the SQLite database"""
    return sqlite3.connect(db_path)

def get_top_run_scorers(limit=10):
    """Get top run scorers from the database"""
    conn = connect_to_db()
    query = """
    SELECT Player_Name, SUM(Runs_Scored) as Total_Runs,
           COUNT(*) as Seasons_Played,
           AVG(Batting_Average) as Avg_Batting_Avg
    FROM player_stats
    WHERE Runs_Scored IS NOT NULL
    GROUP BY Player_Name
    ORDER BY Total_Runs DESC
    LIMIT ?
    """
    df = pd.read_sql_query(query, conn, params=[limit])
    conn.close()
    return df

def get_top_wicket_takers(limit=10):
    """Get top wicket takers from the database"""
    conn = connect_to_db()
    query = """
    SELECT Player_Name, SUM(Wickets_Taken) as Total_Wickets,
           COUNT(*) as Seasons_Played,
           AVG(Bowling_Average) as Avg_Bowling_Avg
    FROM player_stats
    WHERE Wickets_Taken IS NOT NULL
    GROUP BY Player_Name
    ORDER BY Total_Wickets DESC
    LIMIT ?
    """
    df = pd.read_sql_query(query, conn, params=[limit])
    conn.close()
    return df

def get_player_stats(player_name):
    """Get detailed stats for a specific player"""
    conn = connect_to_db()
    query = """
    SELECT * FROM player_stats
    WHERE Player_Name LIKE ?
    ORDER BY Year DESC
    """
    df = pd.read_sql_query(query, conn, params=[f"%{player_name}%"])
    conn.close()
    return df

def run_basic_analysis():
    """Run basic analysis and print results"""
    print("📊 IPL Player Statistics Analysis")
    print("=" * 50)

    # Top run scorers
    print("\n🏏 TOP 10 RUN SCORERS (All-Time):")
    top_runs = get_top_run_scorers(10)
    print(top_runs.to_string(index=False))

    # Top wicket takers
    print("\n🥎 TOP 10 WICKET TAKERS (All-Time):")
    top_wickets = get_top_wicket_takers(10)
    print(top_wickets.to_string(index=False))

    # Example: Get stats for a specific player
    print("\n🔍 Example: Virat Kohli's stats:")
    kohli_stats = get_player_stats("Virat Kohli")
    if not kohli_stats.empty:
        print(kohli_stats[['Year', 'Runs_Scored', 'Batting_Average', 'Wickets_Taken']].to_string(index=False))
    else:
        print("No data found for Virat Kohli")

if __name__ == "__main__":
    run_basic_analysis()