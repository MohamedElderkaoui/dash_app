import dash
from dash import html
from layout import app_layout
from callbacks import register_callbacks

# Initialize the app
app = dash.Dash(__name__)
app.layout = app_layout

# Register all callbacks
register_callbacks(app)
if __name__ == '__main__':
    app.run_server(host='127.0.0.1', port=8050)
