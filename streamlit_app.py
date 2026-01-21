import streamlit as st
import sqlite3
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set page config
st.set_page_config(
    page_title="IPL Player Statistics Dashboard",
    page_icon="🏏",
    layout="wide"
)

# Connect to database
@st.cache_data
def load_data():
    """Load data from SQLite database"""
    conn = sqlite3.connect("data/ipl_stats.db")
    df = pd.read_sql_query("SELECT * FROM player_stats", conn)
    conn.close()
    return df

# Load data
df = load_data()

# Clean data - fill NaN values appropriately
df = df.fillna({
    'Runs_Scored': 0,
    'Wickets_Taken': 0,
    'Centuries': 0,
    'Half_Centuries': 0,
    'Batting_Average': 0,
    'Bowling_Average': 0,
    'Year': 0
})

# Convert Year to int for better handling
df['Year'] = df['Year'].astype(int)

# Title
st.title("🏏 IPL Player Statistics Dashboard")
st.markdown("Interactive analysis of IPL player performance data")

# Sidebar filters
st.sidebar.header("Filters")

# Year filter
years = sorted(df[df['Year'] > 0]['Year'].unique())  # Only valid years
selected_years = st.sidebar.multiselect(
    "Select Years",
    years,
    default=years[-3:] if len(years) > 3 else years  # Default to last 3 years
)

# Player search
player_search = st.sidebar.text_input("Search Player", "")

# Filter data
filtered_df = df.copy()
if selected_years:
    filtered_df = filtered_df[filtered_df['Year'].isin(selected_years)]
if player_search:
    filtered_df = filtered_df[filtered_df['Player_Name'].str.contains(player_search, case=False, na=False)]

# Main content
col1, col2, col3, col4 = st.columns(4)

with col1:
    try:
        st.metric("Total Players", len(filtered_df['Player_Name'].unique()))
    except:
        st.metric("Total Players", 0)

with col2:
    try:
        total_runs = filtered_df['Runs_Scored'].sum()
        st.metric("Total Runs", f"{total_runs:,.0f}")
    except:
        st.metric("Total Runs", "0")

with col3:
    try:
        total_wickets = filtered_df['Wickets_Taken'].sum()
        st.metric("Total Wickets", f"{total_wickets:,.0f}")
    except:
        st.metric("Total Wickets", "0")

with col4:
    try:
        avg_batting_avg = filtered_df['Batting_Average'].mean()
        st.metric("Avg Batting Average", f"{avg_batting_avg:.2f}")
    except:
        st.metric("Avg Batting Average", "0.00")

# Tabs for different views
tab1, tab2, tab3, tab4 = st.tabs(["🏏 Batting Stats", "🥎 Bowling Stats", "📊 Player Comparison", "🔍 Individual Player"])

with tab1:
    st.header("Top Run Scorers")

    # Aggregate runs by player
    if not filtered_df.empty and 'Runs_Scored' in filtered_df.columns:
        runs_by_player = filtered_df.groupby('Player_Name')['Runs_Scored'].sum().reset_index()
        runs_by_player = runs_by_player[runs_by_player['Runs_Scored'] > 0]  # Only players with runs
        runs_by_player = runs_by_player.sort_values('Runs_Scored', ascending=False).head(15)

        if not runs_by_player.empty:
            fig_runs = px.bar(
                runs_by_player,
                x='Runs_Scored',
                y='Player_Name',
                orientation='h',
                title="Top 15 Run Scorers",
                labels={'Runs_Scored': 'Total Runs', 'Player_Name': 'Player'}
            )
            fig_runs.update_layout(height=600)
            st.plotly_chart(fig_runs, use_container_width=True)
        else:
            st.warning("No run scoring data available for the selected filters.")
    else:
        st.warning("No data available for run scoring analysis.")

    # Centuries and Half-Centuries
    if not filtered_df.empty and 'Centuries' in filtered_df.columns and 'Half_Centuries' in filtered_df.columns:
        centuries_data = filtered_df.groupby('Player_Name')[['Centuries', 'Half_Centuries']].sum().reset_index()
        centuries_data = centuries_data[(centuries_data['Centuries'] > 0) | (centuries_data['Half_Centuries'] > 0)]
        centuries_data = centuries_data.sort_values('Centuries', ascending=False).head(10)

        if not centuries_data.empty:
            col1, col2 = st.columns(2)
            with col1:
                fig_centuries = px.bar(
                    centuries_data,
                    x='Player_Name',
                    y='Centuries',
                    title="Most Centuries",
                    color='Centuries'
                )
                st.plotly_chart(fig_centuries, use_container_width=True)

            with col2:
                fig_half_centuries = px.bar(
                    centuries_data,
                    x='Player_Name',
                    y='Half_Centuries',
                    title="Most Half-Centuries",
                    color='Half_Centuries'
                )
                st.plotly_chart(fig_half_centuries, use_container_width=True)
        else:
            st.info("No centuries or half-centuries data available for the selected filters.")
    else:
        st.warning("Centuries data not available.")

with tab2:
    st.header("Top Wicket Takers")

    # Aggregate wickets by player
    wickets_by_player = filtered_df.groupby('Player_Name')['Wickets_Taken'].sum().reset_index()
    wickets_by_player = wickets_by_player.sort_values('Wickets_Taken', ascending=False).head(15)

    fig_wickets = px.bar(
        wickets_by_player,
        x='Wickets_Taken',
        y='Player_Name',
        orientation='h',
        title="Top 15 Wicket Takers",
        labels={'Wickets_Taken': 'Total Wickets', 'Player_Name': 'Player'}
    )
    fig_wickets.update_layout(height=600)
    st.plotly_chart(fig_wickets, use_container_width=True)

    # Bowling averages
    bowling_avg_data = filtered_df[filtered_df['Wickets_Taken'] > 0].groupby('Player_Name').agg({
        'Bowling_Average': 'mean',
        'Wickets_Taken': 'sum'
    }).reset_index()
    bowling_avg_data = bowling_avg_data[bowling_avg_data['Wickets_Taken'] >= 10].sort_values('Bowling_Average').head(15)

    fig_bowling_avg = px.bar(
        bowling_avg_data,
        x='Bowling_Average',
        y='Player_Name',
        orientation='h',
        title="Best Bowling Averages (Min 10 wickets)",
        labels={'Bowling_Average': 'Bowling Average', 'Player_Name': 'Player'}
    )
    st.plotly_chart(fig_bowling_avg, use_container_width=True)

with tab3:
    st.header("Player Comparison")

    # Scatter plot: Batting Average vs Strike Rate
    scatter_data = filtered_df[filtered_df['Runs_Scored'] > 100].copy()  # Players with significant runs

    fig_scatter = px.scatter(
        scatter_data,
        x='Batting_Average',
        y='Batting_Strike_Rate',
        size='Runs_Scored',
        color='Year',
        hover_name='Player_Name',
        title="Batting Average vs Strike Rate (Players with >100 runs)",
        labels={
            'Batting_Average': 'Batting Average',
            'Batting_Strike_Rate': 'Strike Rate',
            'Runs_Scored': 'Total Runs'
        }
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    # Season trends
    st.subheader("Season-wise Trends")
    season_stats = filtered_df.groupby('Year').agg({
        'Runs_Scored': 'sum',
        'Wickets_Taken': 'sum',
        'Batting_Average': 'mean',
        'Bowling_Average': 'mean'
    }).reset_index()

    col1, col2 = st.columns(2)
    with col1:
        fig_runs_trend = px.line(
            season_stats,
            x='Year',
            y='Runs_Scored',
            title="Total Runs by Season",
            markers=True
        )
        st.plotly_chart(fig_runs_trend, use_container_width=True)

    with col2:
        fig_wickets_trend = px.line(
            season_stats,
            x='Year',
            y='Wickets_Taken',
            title="Total Wickets by Season",
            markers=True
        )
        st.plotly_chart(fig_wickets_trend, use_container_width=True)

with tab4:
    st.header("Individual Player Analysis")

    # Player selector
    players = sorted(filtered_df['Player_Name'].unique())
    selected_player = st.selectbox("Select Player", players)

    if selected_player:
        player_data = filtered_df[filtered_df['Player_Name'] == selected_player]

        # Player summary
        col1, col2, col3 = st.columns(3)
        with col1:
            total_runs = player_data['Runs_Scored'].sum()
            st.metric("Total Runs", f"{total_runs:,.0f}")

        with col2:
            total_wickets = player_data['Wickets_Taken'].sum()
            st.metric("Total Wickets", f"{total_wickets:,.0f}")

        with col3:
            seasons = len(player_data)
            st.metric("Seasons Played", seasons)

        # Player career chart
        fig_career = go.Figure()

        fig_career.add_trace(go.Scatter(
            x=player_data['Year'],
            y=player_data['Runs_Scored'],
            mode='lines+markers',
            name='Runs Scored',
            line=dict(color='blue')
        ))

        fig_career.add_trace(go.Scatter(
            x=player_data['Year'],
            y=player_data['Wickets_Taken'],
            mode='lines+markers',
            name='Wickets Taken',
            line=dict(color='red'),
            yaxis='y2'
        ))

        fig_career.update_layout(
            title=f"{selected_player} - Career Performance",
            xaxis=dict(title="Year"),
            yaxis=dict(title="Runs Scored"),
            yaxis2=dict(title="Wickets Taken", overlaying="y", side="right"),
            height=400
        )

        st.plotly_chart(fig_career, use_container_width=True)

        # Detailed stats table
        st.subheader("Season-wise Statistics")
        display_cols = ['Year', 'Matches_Batted', 'Runs_Scored', 'Batting_Average',
                       'Matches_Bowled', 'Wickets_Taken', 'Bowling_Average']
        st.dataframe(player_data[display_cols].sort_values('Year', ascending=False))

# Footer
st.markdown("---")
st.markdown("Built with Streamlit | Data from IPL Statistics ETL Pipeline")