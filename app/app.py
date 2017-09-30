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
                'yaxis': {
                    'range': [0.85, 0.96]
                }
            }
        }
    ),

    dcc.Markdown(
        children="## Objective\n The objective of this exploration is to \
        explore how geography plays roles across economics, education, and \
        usage of libraries across supervisor districts in San \
        Francisco."
    ),

    dhtml.Img(src="https://i.imgur.com/6mROVMa.png", title="SF Supervisor \
District map, sourced from sfyimby.org"),

    dcc.Markdown(
        children="We can explore first the general income levels of each of \
the supervisor districts in San Francisco, using both federal Census data \
and city-sourced data, along with district-level education information to help \
us understand the geography of both financial capital as well as educational \
capital in San Francisco. \
(Source: Phase 1 Socioeconomic Equity in the \
City of San Francisco Policy Analysis Report, SF Board of Supervisors)"
    ),

    dcc.Graph(
        id="income_and_education_percent_district_level",
        figure = {
            'data': [
                {
                    'x': whirl.sd_capital.index,
                    'y': whirl.sd_capital["fin"],
                    'type': 'bar',
                    'name': 'Average Household Income',
                    'yaxis': 'y1'
                },
                {
                    'x': whirl.sd_capital.index,
                    'y': whirl.sd_capital["edu"],
                    'type': 'bar',
                    'name': '% with college-level education',
                    'yaxis': 'y2'
                }
            ],
            'layout': {
            'yaxis': {
                'title': "t1",
                'range': [30000,110000]
            },
            'yaxis2': {
                'title': 't2',
                'range': [0,100],
                'overlaying': 'y',
                'side': 'right'
            }
            }
        }
    ),

    dcc.Markdown(
        children="How might we use this information in conjunction with \
        knowledge about how libraries are used by district?"
    ),

    dcc.Graph(
        id="libraries_by_district",
        figure = {
            'data':
                go.Bar(
                    x = whirl.libmean_df.index,
                    y = whirl.libmean_df["Total Checkouts"]
                ),
            'layout': {
                'title': "Average total checkouts by patron per district, 2003-2016"
            }
        }
    )

    ]

)

if __name__ == '__main__':
    app.run_server(debug=True)
