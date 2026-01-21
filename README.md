# 🏏 IPL Player Statistics Dashboard

An end-to-end data engineering project that extracts, transforms, and visualizes IPL (Indian Premier League) cricket player statistics.


## 📊 Features

- **ETL Pipeline**: Automated extraction, transformation, and loading of IPL data
- **Interactive Dashboard**: Beautiful Streamlit app with multiple visualizations
- **Automated Updates**: Self-maintaining system with scheduled data refreshes
- **Player Analytics**: Comprehensive analysis of batting and bowling statistics
- **Real-time Filtering**: Filter data by years and search players

## 🛠 Tech Stack

- **Language**: Python 3.11
- **Data Processing**: Pandas, SQLite
- **Visualization**: Streamlit, Plotly
- **Automation**: Windows Task Scheduler
- **Deployment**: Streamlit Cloud

## 📁 Project Structure

```
ipl/
├── data/
│   ├── raw/
│   │   └── cricket_data_2025.csv    # Raw IPL data
│   └── ipl_stats.db                 # Processed SQLite database
├── scripts/
│   ├── extract.py                   # Data extraction
│   ├── transform.py                 # Data cleaning & transformation
│   ├── load.py                      # Database loading
│   ├── etl_pipeline.py              # Complete ETL orchestration
│   ├── analysis.py                  # Data analysis queries
│   ├── streamlit_app.py             # Dashboard application
│   └── update_data.py               # Automated updates
├── tableau_dashboard_guide.md       # Tableau guide (optional)
├── update_dashboard.bat             # Windows automation script
├── update_dashboard.ps1             # PowerShell automation script
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## 🏁 Quick Start

### Prerequisites
- Python 3.11 or higher
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/ipl-dashboard.git
   cd ipl-dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the ETL pipeline**
   ```bash
   python scripts/etl_pipeline.py
   ```

4. **Launch the dashboard**
   ```bash
   streamlit run scripts/streamlit_app.py
   ```

5. **Open your browser** to `http://localhost:8501`

## 📊 Dashboard Features

### 🏏 Batting Statistics
- Top run scorers with career totals
- Centuries and half-centuries leaders
- Batting averages and strike rates

### 🥎 Bowling Statistics
- Leading wicket takers
- Best bowling averages
- Economy rates and strike rates

### 📊 Player Comparison
- Scatter plots for performance analysis
- Season-wise trends
- Interactive filtering

### 🔍 Individual Player Analysis
- Career progression charts
- Season-by-season statistics
- Detailed performance metrics

## 🔄 Automation Setup

### Windows Task Scheduler
1. Open Task Scheduler (`taskschd.msc`)
2. Create Basic Task → `IPL Dashboard Update`
3. Set trigger (Daily/Weekly)
4. Set action to run `update_dashboard.bat`
5. Configure for highest privileges

### Manual Updates
```bash
python scripts/update_data.py
```

## 📈 Data Sources

- **Primary Data**: IPL player statistics CSV (2020-2025 seasons)
- **Update Frequency**: Weekly automated checks
- **Data Quality**: Automated validation and cleaning

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 Data Dictionary

| Column | Description | Type |
|--------|-------------|------|
| Year | IPL season year | Integer |
| Player_Name | Player full name | String |
| Matches_Batted | Matches played as batsman | Integer |
| Not_Outs | Times not out while batting | Integer |
| Runs_Scored | Total runs scored | Integer |
| Highest_Score | Highest individual score | Integer |
| Batting_Average | Batting average | Float |
| Balls_Faced | Total balls faced | Integer |
| Batting_Strike_Rate | Strike rate | Float |
| Centuries | Number of 100+ scores | Integer |
| Half_Centuries | Number of 50-99 scores | Integer |
| Fours | Number of boundaries | Integer |
| Sixes | Number of sixes | Integer |
| Matches_Bowled | Matches played as bowler | Integer |
| Balls_Bowled | Total balls bowled | Integer |
| Runs_Conceded | Runs given while bowling | Integer |
| Wickets_Taken | Total wickets taken | Integer |
| Bowling_Average | Bowling average | Float |
| Economy_Rate | Economy rate | Float |
| Bowling_Strike_Rate | Bowling strike rate | Float |
| Four_Wicket_Hauls | 4+ wickets in innings | Integer |
| Five_Wicket_Hauls | 5+ wickets in innings | Integer |

## 📊 ETL Pipeline Architecture

```
Raw CSV Data → Extract → Transform → Load → Database → Dashboard
     ↓             ↓         ↓         ↓         ↓          ↓
  Source     Pandas    Clean    SQLite   Query    Streamlit
  Files      Reading   Data     Insert   Data     Charts
```

## 🚀 Deployment

### Streamlit Cloud (Recommended)
1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect GitHub repository
4. Deploy automatically

### Other Platforms
- **Heroku**: Container-based deployment
- **Vercel**: Serverless deployment
- **Railway**: Full-stack deployment

## 🐛 Troubleshooting

### Common Issues

**Dashboard not loading:**
```bash
# Clear Streamlit cache
streamlit cache clear
# Restart app
streamlit run scripts/streamlit_app.py
```

**Database errors:**
```bash
# Re-run ETL pipeline
python scripts/etl_pipeline.py
```

**Automation not working:**
- Check Task Scheduler logs
- Verify file paths in batch script
- Test manual update first

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/your-username/ipl-dashboard/issues)
- **Discussions**: [GitHub Discussions](https://github.com/your-username/ipl-dashboard/discussions)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- IPL data sourced from official records
- Built with love for cricket analytics
- Inspired by data engineering best practices

---

**Made with ❤️ by a data engineering enthusiast**

*Star this repo if you found it helpful!* ⭐
