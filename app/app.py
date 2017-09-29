# whirl dash app
# brunston poon
import dash
import dash_core_components as dcc
import dash_html_components as dhtml

import pandas as pd
import os.path
from whirl import *

app = dash.Dash()

filenames = {
    "park_old": "Park_Scores_2005-2014.csv",
    "park_new": "Park_Evaluation_Scores_starting_Fiscal_Year_2015.csv",
    "library": "Library_Usage.csv"
}
data_dir = os.path.dirname(os.getcwd()) + "/data/"

whirl = Whirl(data_dir, filenames)

# let's use a functional CSS dependency from the Dash tutorials; no need to
# spend an inordinate amount of time to develop my own at the moment.
app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

colors = {
    'background': '#EEEEEE',
    'text': '#555555'
    }



app.layout = dhtml.Div(children=[
    dhtml.H1(
        children='WhirlSF - a whirlwind tour of SF park and library data',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }

    ),

    dcc.Markdown(
        children="## Perception\n##### As people who work with data, sometimes we \
        forget to see the greater picture of our work; the folks who end up \
        reading our analyses do not always think like the way that we do. \
        As a result, often we forget that the easiest way to show someone \
        something is to tell them a story..."
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
