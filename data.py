# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 16:30:51 2020

@author: emma
"""
import networkx as nx
import plotly.graph_objects as go


def createGraph(df, company): 
    traceRecode = []
    
    df = df[df['company'] == company]

    G = nx.from_pandas_edgelist(df, 'source', 'destination')

    pos = nx.spring_layout(G)
    
    #nodes
    for node in G.nodes:
        G.nodes[node]['pos'] = list(pos[node])
        
        
    node_trace = go.Scatter(x=[], y=[], hovertext=[], text=[], mode='markers+text', textposition="bottom center",
                        hoverinfo="text", marker={})

    color_map = [] 
    size = [] 
    for node in G.nodes():
        x, y = G.nodes[node]['pos']
        hovertext = node
        text = ""
        node_trace['x'] += tuple([x])
        node_trace['y'] += tuple([y])
        node_trace['hovertext'] += tuple([hovertext])
        node_trace['text'] += tuple([text])
        
        try:
            if node in df.source.values: 
                color_map.append('green')
                size.append(25)
            elif df.loc[df.destination == node, 'type'].iloc[0] == 'internal':
                color_map.append('seagreen')
                size.append(15)
            elif df.loc[df.destination == node, 'type'].iloc[0] == 'affiliated':
                color_map.append('darkcyan')
                size.append(15)
            else: 
                color_map.append('blue')
                size.append(15)
        except IndexError:
            color_map.append('purple')
            size.append(15)
    
    node_trace['marker']['color'] = color_map
    node_trace['marker']['size'] = size
    
    traceRecode.append(node_trace)
        
    #Edges
    for edge in G.edges:
        x0, y0 = G.nodes[edge[0]]['pos']
        x1, y1 = G.nodes[edge[1]]['pos']
        trace = go.Scatter(x=tuple([x0, x1, None]), y=tuple([y0, y1, None]),
                           mode='lines',
                           line={'width': 0.5},
                           marker=dict(color='black'),
                           line_shape='spline',
                           opacity=0.5)
        traceRecode.append(trace)
    ### create figure dictionary 
    figure = {
    "data": traceRecode,
    "layout": go.Layout(title=company, showlegend=False, hovermode='closest',
                        margin={'b': 40, 'l': 40, 'r': 40, 't': 40},
                        xaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False},
                        yaxis={'showgrid': False, 'zeroline': False, 'showticklabels': False},
                        height=600)}
    return figure