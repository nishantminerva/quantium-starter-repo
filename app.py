import dash
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html


df = pd.read_csv("final-data.csv")
app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
# Sales, Date, region


fig = {
        "data": [{"x": df["date"], "y": df["sales"], "type": "line"}],
    }



app.layout = html.Div([
    html.H1(children='Sales Report'),

    html.Div(children='''
        Sales Analysis.
    '''),
    
    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    html.Div(children=[
    dcc.RadioItems(
        id='region-filter',
        options=[
            {'label': 'North', 'value': 'north'},
            {'label': 'East', 'value': 'east'},
            {'label': 'South', 'value': 'south'},
            {'label': 'West', 'value': 'west'},
            {'label': 'All', 'value': 'all'},
        ],
        value='all',
        labelStyle={'display': 'inline-block'}
    ),
    dcc.Graph(id='sales-chart')
])
    
], style={'display': 'flex', 'flex-direction': 'column'})

@app.callback(
    # Output(component_id='my-output', component_property='children'),
    # Input(component_id='my-input', component_property='value')
    
    dash.dependencies.Output('sales-chart', 'figure'),
    [dash.dependencies.Input('region-filter', 'value')]
)
def update_sales_chart(region):
    if region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == region]

    fig = {
        "data": [{"x": filtered_df["date"], "y": filtered_df["sales"], "type": "line"}],
        "layout": {"title": f"Sales by Region ({region.capitalize()})"},
    }
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

# https://github.com/nishantminerva/quantium-starter-repo