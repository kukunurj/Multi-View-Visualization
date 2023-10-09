import pandas as pd
from dash import dcc, html
import plotly.express as px
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import dash

df = pd.read_csv('data.csv')

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

# Creating the line chart for total deaths over the years
total_deaths_chart = px.line(df.groupby('YEAR')['DEATHS'].sum().reset_index(), 
                             x='YEAR', 
                             y='DEATHS', 
                             title='Total Deaths Over the Years (\'WHAT\')',
                             labels={'DEATHS':'Total Deaths', 'YEAR':'Year'})

# Creating the line chart for rates over the years
line_chart = px.line(df.groupby('YEAR')['RATE'].mean().reset_index(), 
                     x='YEAR', 
                     y='RATE',
                     title='Suicide Rate Over the Years (\'WHY\')',
                     labels={'RATE':'Suicide Rate', 'YEAR':'Year'})

# Creating the chloropleth map for geospatial distribution
map = px.choropleth(df, 
                    geojson=state_geojson, 
                    locations='STATE', 
                    color='RATE',
                    hover_name='STATE', 
                    animation_frame='YEAR',
                    title='Geospatial Distribution of Suicide Rates (\'WHERE\')',
                    labels={'RATE':'Suicide Rate'})

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(dcc.Graph(figure=total_deaths_chart), md=6),
        dbc.Col(dcc.Graph(figure=line_chart), md=6)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=map), md=12)
    ])
])

if __name__ == "__main__":
    app.run_server(debug=True)
