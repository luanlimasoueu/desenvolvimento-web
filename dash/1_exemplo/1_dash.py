# Import necessary libraries
import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

# Create a Dash application
app = dash.Dash(__name__)
# Sample data
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [10, 11, 12, 13, 14]
})
# Define the layout of your app
app.layout = html.Div([
    html.H1("My First Dash Application"),
    
    dcc.Graph(
        id='scatter-plot',
        figure={
            'data': [
                {'x': data['x'], 'y': data['y'], 'type': 'scatter', 'mode': 'markers', 'name': 'Scatter Plot'},
            ],
            'layout': {
                'title': 'Scatter Plot Example'
            }
        }
    )
])
# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)