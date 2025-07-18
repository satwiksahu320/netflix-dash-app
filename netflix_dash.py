# Import required libraries
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

# Load the cleaned Netflix dataset
net = pd.read_csv('netflix_cleaned.csv')  # Make sure this file is in the same folder

# Setup the Dash app
app = Dash(__name__)

# ========================
# Plot 1: Bar chart of Movies vs TV Shows
# ========================

# Prepare data
type_counts = net['type'].value_counts().reset_index()
type_counts.columns = ['Content Type', 'Count']

# Create Plotly bar chart
bar1 = px.bar(
    type_counts,
    x='Content Type',
    y='Count',
    title='Count of Movies vs TV Shows on Netflix',
    labels={'Content Type': 'Type', 'Count': 'Total'},
    color='Content Type'
)

# ========================
# Layout
# ========================
app.layout = html.Div(children=[
    html.H1('📺 Netflix Data Dashboard', style={'textAlign': 'center'}),

    # Show bar chart
    dcc.Graph(
        id='bar-chart-type',
        figure=bar1
    )
])

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
