# 📊 Netflix Data Visualization Dashboard

This project is a data visualization dashboard built using **Plotly** and **Dash**, designed to explore and analyze Netflix's catalog of Movies and TV Shows.

## 🚀 Features

- Cleaned and processed Netflix dataset using **Pandas**
- Interactive bar chart showing count of Movies vs TV Shows
- Created using **Plotly Express** and deployed using **Dash**
- Modular and beginner-friendly codebase
- Perfect starter project for Data Visualization & Dashboard building

## 🧰 Technologies Used

- Python 🐍
- Pandas 📊
- Plotly 📈
- Dash 🌐

## 📂 Project Structure
📁 Netflix-Dashboard/
├── netflix_cleaned.csv     
├── netflix_dash.py         
├── README.md 


## 🧹 Data Cleaning Summary

- Removed null or missing values from important columns
- Formatted `date_added` column into proper datetime format
- Extracted year and month for time-based analysis
- Used `.value_counts()` and grouping for summary statistics

## 📉 Visualizations

✅ Bar chart: Count of Movies vs TV Shows  
📍 More interactive plots can be added using Plotly or Dash Components
![Bar Chart](screenshots/barchart.png)

## 📦 How to Run Locally

1. Clone the repo:
   ```bash
   git clone git clone https://github.com/satwiksahu320/netflix-dash-app.git
   cd netflix-dashboard


2. install dependecies
   pip install -r requirements.txt
   pip install pandas plotly dash
3.Run the Dash app
  python netflix_dash.py
4.View in Browser
  Visit: http://127.0.0.1:8050 in your browser
