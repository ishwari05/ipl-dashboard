import pandas as pd


def clean_highest_score(df):
    """
    Removes '*' from Highest_Score (e.g., '37*' -> 37)
    """
    df["Highest_Score"] = (
        df["Highest_Score"]
        .astype(str)
        .str.replace("*", "", regex=False)
    )
    return df


def convert_numeric_columns(df):
    """
    Converts selected columns to numeric types.
    Invalid values are safely converted to NULL.
    """
    numeric_columns = [
        "Year",
        "Matches_Batted", "Not_Outs", "Runs_Scored", "Balls_Faced",
        "Batting_Average", "Batting_Strike_Rate",
        "Centuries", "Half_Centuries", "Fours", "Sixes",
        "Matches_Bowled", "Balls_Bowled", "Runs_Conceded",
        "Wickets_Taken", "Bowling_Average",
        "Economy_Rate", "Bowling_Strike_Rate",
        "Four_Wicket_Hauls", "Five_Wicket_Hauls",
        "Highest_Score"
    ]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    return df


def clean_player_names(df):
    """
    Standardizes player names
    """
    df["Player_Name"] = df["Player_Name"].str.strip().str.title()
    return df


def transform_data(df):
    """
    Main transformation function (ETL Transform step)
    """
    print("Starting transformation...")

    # Replace 'No stats' with NULL
    df = df.replace("No stats", pd.NA)
    print("✔ Replaced 'No stats' with NULL")

    # Clean columns
    df = clean_highest_score(df)
    df = convert_numeric_columns(df)
    df = clean_player_names(df)

    print("✅ Transformation complete")
    return df


# -------------------------
# Test block (safe to keep)
# -------------------------
if __name__ == "__main__":
    df_raw = pd.read_csv("data/raw/cricket_data_2025.csv")
    df_clean = transform_data(df_raw)

    print("\nData types:")
    print(df_clean.dtypes)

    print("\nSample Highest_Score values:")
    print(df_clean["Highest_Score"].head())
