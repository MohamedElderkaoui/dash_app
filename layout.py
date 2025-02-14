from dash import dcc, html
from data_loader import get_csv_files

csv_files = get_csv_files()

app_layout = html.Div([
    html.H1("📊 Multi-File Dash Data Visualizer", style={'textAlign': 'center'}),

    html.Label("Select a CSV File:"),
    dcc.Dropdown(
        id='file-dropdown',
        options=[{'label': f, 'value': f} for f in csv_files],
        value=csv_files[0] if csv_files else None
    ),

    html.Label("Select X-axis:"),
    dcc.Dropdown(id='x-axis-dropdown', options=[], value=None),

    html.Label("Select Y-axis:"),
    dcc.Dropdown(id='y-axis-dropdown', options=[], value=None),

    html.Label("Select Chart Type:"),
    dcc.RadioItems(
        id='chart-type',
        options=[
            {'label': 'Line', 'value': 'line'},
            {'label': 'Bar', 'value': 'bar'},
            {'label': 'Scatter', 'value': 'scatter'}
        ],
        value='line',
        inline=True
    ),

    dcc.Graph(id='data-graph'),
])
