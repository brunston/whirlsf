# whirl dash app
# brunston poon
import dash
import dash_core_components as dcc
import dash_html_components as dhtml

import pandas as pd
import os.path
import plotly.graph_objs as go
import whirl as wh

app = dash.Dash()

filenames = {
    "park_old": "Park_Scores_2005-2014.csv",
    "park_new": "Park_Evaluation_Scores_starting_Fiscal_Year_2015.csv",
    "library": "Library_Usage.csv"
}
data_dir = os.path.dirname(os.getcwd()) + "/data/"
sf_dist_map = data_dir +\
              "sf_supervisor_district_maps/sf_district_map_sfyimby.png"

whirl = wh.Whirl(data_dir, filenames)

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
        children="## Perception\n##### As people who work with data, sometimes \
        we forget to see the greater picture of our work; the folks who end up \
        reading our analyses do not always think like the way that we do. \
        As a result, often we forget that the easiest way to show someone \
        something is to tell them a story..."
    ),

    dcc.Graph(
        id="supervisor_districts_park_scores",
        figure = {
            'data': [
                go.Bar(
                    x = [
                    "SD 1", "SD 2", "SD 3", "SD 4", "SD 5", "SD 6", "SD 7",
                    "SD 8", "SD 9", "SD 10", "SD 11"],
                    y = wh.mean(whirl.parkgrp_df)["Score"].values.tolist(),
                    text = wh.mean(whirl.parkgrp_df)["Score"].values.tolist()
                )
            ],
            'layout': {
                'title': "Average Park Scores by Supervisor District",
                'yaxis': [0.5, 1]
            }
        }
    ),

    dcc.Markdown(
        children="## Objective\n The objective of this exploration is to \
        explore whether there is any correlation between better park scores \
        and increased usage of libraries across supervisor districts in San \
        Francisco."
    ),

    dhtml.Img(src="https://i.imgur.com/6mROVMa.png", title="SF Supervisor \
District map, sourced from sfyimby.org")
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)
