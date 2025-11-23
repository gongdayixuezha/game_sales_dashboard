# Global Video Game Sales Data Storytelling Dashboard
## Project Introduction
This project is an interactive data storytelling application built with Streamlit, focusing on global video game sales data from the 1980s to the 2010s. It explores industry trends, regional preferences, and market competition patterns.

## Dataset
- Source: [Video Game Sales Dataset](https://raw.githubusercontent.com/justmarkham/pandas-videos/master/data/vgsales.csv)
- Scale: 16,598 game sales records
- Core Fields: Game name, platform, release year, genre, publisher, sales in various regions, global sales

## Functional Modules
1. Introduction and Data Description: Project background, dataset details, data quality explanation
2. Core Metrics Overview: KPIs such as total global sales, total number of games, top publishers, etc.
3. In-depth Analysis: Time trends, regional preferences, publisher rankings, platform evolution
4. Insights and Implications: Key findings and action recommendations

## Running Steps
1. Clone the code repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the application: `streamlit run app.py`
4. Access the local address: http://localhost:8501

## Tech Stack
- Frontend Framework: Streamlit ≥ 1.33
- Data Processing: Pandas, Numpy
- Visualization: Plotly, Altair
- Data Formats: CSV, PyArrow

## Deliverables Description
- `app.py`: Main application entry
- `sections/`: Pages for each functional module
- `utils/`: Utility functions for data loading, preprocessing, and visualization
- `data/`: Backup dataset files
- `requirements.txt`: List of dependent packages
- `demo_video.md`: Demo video script

## Demo Video Script (2-4 minutes)
1. Opening (30 seconds): Introduce the project theme, dataset, and core objectives
2. Function Demonstration (2 minutes):
   - Usage of navigation menu
   - Interactions with filters (year range, region selection)
   - Interpretation of various visual charts (trend charts, comparison charts, ranking charts)
3. Summary of Key Insights (1 minute): Extract 3 key findings and their application value
4. Conclusion (30 seconds): Explain limitations and future improvement directions