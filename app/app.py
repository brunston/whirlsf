
import dash
import dash_core_components as dcc
import dash_html_components as dhtml

import pandas as pd

app = dash.Dash()

colors = {
    'background': '#EEEEEE',
    'text': '#555555'
    }

app.layout = dhtml.Div(children=[
    dhtml.H1(
        children='Hello Dash',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }

    ),

    dhtml.Div(
        children='Dash: web app framework for py',
        style={
            'color': colors['text']
        }
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization'}
                }
                )
                ])
if __name__ == '__main__':
    app.run_server(debug=True)
