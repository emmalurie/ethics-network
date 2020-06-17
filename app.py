# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:30:51 2020

@author: emma
"""
import plotly.graph_objects as go
#import pandas as pd
# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from data import createGraph
import pandas as pd
df = pd.read_excel("link_data.xlsx")
df.dropna(subset=['destination'], inplace =True)
g_fig = createGraph(df, "Google")
m_fig = createGraph(df, "Microsoft")
s_fig = createGraph(df, "Salesforce")
a_fig = createGraph(df, "Amazon")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

app.layout = html.Div([
    dcc.Tabs([
        dcc.Tab(label='Google', children=[
            dcc.Graph(
                figure=g_fig
            )
        ]),
        dcc.Tab(label='Microsoft', children=[
            dcc.Graph(
                figure=m_fig
            )
        ]), 
        dcc.Tab(label='Salesforce', children=[
            dcc.Graph(
                figure=s_fig
            )
        ]), 
        dcc.Tab(label='Amazon', children=[
            dcc.Graph(
                figure=a_fig
            )
        ])
            
    ])
])







if __name__ == '__main__':
    app.run_server(debug=True)

