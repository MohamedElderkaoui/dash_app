from dash import Input, Output
import plotly.express as px
from data_loader import load_csv

def register_callbacks(app):
    @app.callback(
        [Output('x-axis-dropdown', 'options'),
         Output('y-axis-dropdown', 'options'),
         Output('x-axis-dropdown', 'value'),
         Output('y-axis-dropdown', 'value')],
        [Input('file-dropdown', 'value')]
    )
    def update_axis_options(selected_file):
        df = load_csv(selected_file)
        if df is None:
            return [], [], None, None

        columns = [{'label': col, 'value': col} for col in df.columns]
        return columns, columns, df.columns[0], df.columns[1] if len(df.columns) > 1 else None

    @app.callback(
        Output('data-graph', 'figure'),
        [Input('file-dropdown', 'value'),
         Input('x-axis-dropdown', 'value'),
         Input('y-axis-dropdown', 'value'),
         Input('chart-type', 'value')]
    )
    def update_chart(selected_file, x_col, y_col, chart_type):
        df = load_csv(selected_file)
        if df is None or x_col is None or y_col is None:
            return px.scatter(title="No data available")

        if chart_type == 'line':
            fig = px.line(df, x=x_col, y=y_col, title=f"{chart_type.capitalize()} Chart: {x_col} vs {y_col}")
        elif chart_type == 'bar':
            fig = px.bar(df, x=x_col, y=y_col, title=f"{chart_type.capitalize()} Chart: {x_col} vs {y_col}")
        else:
            fig = px.scatter(df, x=x_col, y=y_col, title=f"{chart_type.capitalize()} Chart: {x_col} vs {y_col}")

        return fig
