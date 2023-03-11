# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd


data = pd.read_csv("final-data.csv")
app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = data
# Sales, Date, region


fig = px.bar(df, x="date", y="sales", color="region", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Sales Report'),

    html.Div(children='''
        Sales Analysis.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
