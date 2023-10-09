# Import required libraries
import pandas as pd
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

# Load the dataset
df = pd.read_csv('data-table.csv')

# Preprocess data
df['DEATHS'] = df['DEATHS'].str.replace(',', '').astype(int)

# Create plots
histogram = px.histogram(df, x="RATE", nbins=30, 
                         title="Histogram: RATE Distribution ('What')",
                         hover_data=['YEAR', 'STATE', 'RATE'])

bar_chart = px.bar(df, x='YEAR', y='RATE', color='STATE', 
                   title="Bar Chart: Average RATE by Year ('Why')", 
                   labels={'RATE': 'Average RATE'},
                   hover_data=['YEAR', 'STATE', 'RATE'])

line_chart = px.line(df.groupby(['YEAR', 'STATE'])['RATE'].mean().reset_index(), 
                     x='YEAR', y='RATE', color='STATE', 
                     title="Line Chart: Trend of RATE Over Years for Each State ('Why')",
                     hover_data=['YEAR', 'STATE', 'RATE'])

# We have a dictionary of state to lat, lon:
state_to_lat_lon = {
    'Alabama': [32.806671, -86.791130],
    'Alaska': [61.370716, -152.404419],
    'Arizona': [33.729759, -111.431221],
    'Arkansas': [34.969704, -92.373123],
    'California': [36.116203, -119.681567],
    'Colorado': [39.059811, -105.311104],
    'Connecticut': [41.597782, -72.755371],
    'Delaware': [39.318523, -75.507141],
    'Florida': [27.766279, -81.686783],
    'Georgia': [33.040619, -83.643074],
    'Hawaii': [21.094318, -157.498337],
    'Idaho': [44.240459, -114.478828],
    'Illinois': [40.349457, -88.986137],
    'Indiana': [39.849426, -86.258284],
    'Iowa': [42.011539, -93.210526],
    'Kansas': [38.526600, -96.726486],
    'Kentucky': [37.668140, -84.670067],
    'Louisiana': [31.169546, -91.867805],
    'Maine': [44.693947, -69.381927],
    'Maryland': [39.063946, -76.802101],
    'Massachusetts': [42.230171, -71.530106],
    'Michigan': [43.326618, -84.536095],
    'Minnesota': [45.694454, -93.900192],
    'Mississippi': [32.741646, -89.678696],
    'Missouri': [38.456085, -92.288368],
    'Montana': [46.921925, -110.454353],
    'Nebraska': [41.125370, -98.268082],
    'Nevada': [38.313515, -117.055374],
    'New Hampshire': [43.452492, -71.563896],
    'New Jersey': [40.298904, -74.521011],
    'New Mexico': [34.840515, -106.248482],
    'New York': [42.165726, -74.948051],
    'North Carolina': [35.630066, -79.806419],
    'North Dakota': [47.528912, -99.784012],
    'Ohio': [40.388783, -82.764915],
    'Oklahoma': [35.565342, -96.928917],
    'Oregon': [44.572021, -122.070938],
    'Pennsylvania': [40.590752, -77.209755],
    'Rhode Island': [41.680893, -71.511780],
    'South Carolina': [33.856892, -80.945007],
    'South Dakota': [44.299782, -99.438828],
    'Tennessee': [35.747845, -86.692345],
    'Texas': [31.054487, -97.563461],
    'Utah': [40.150032, -111.862434],
    'Vermont': [44.045876, -72.710686],
    'Virginia': [37.769337, -78.170000],
    'Washington': [47.400902, -121.490494],
    'West Virginia': [38.491000, -80.954570],
    'Wisconsin': [44.268543, -89.616508],
    'Wyoming': [42.755966, -107.302490]
}

# Add Latitude and Longitude columns to the DataFrame
df['Latitude'] = df['STATE'].map(lambda x: state_to_lat_lon[x][0] if x in state_to_lat_lon else None)
df['Longitude'] = df['STATE'].map(lambda x: state_to_lat_lon[x][1] if x in state_to_lat_lon else None)

# Create geospatial scatter plot
map = px.scatter_geo(df, lat='Latitude', lon='Longitude', 
                     color="RATE", hover_name="STATE",
                     animation_frame="YEAR", 
                     title="Geospatial Scatter Plot: Distribution of RATE over Years ('Where')")

# Initialize the Dash app
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the app layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(dcc.Graph(figure=histogram, id='histogram'), md=6),
        dbc.Col(dcc.Graph(figure=bar_chart, id='bar_chart'), md=6)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=line_chart, id='line_chart'), md=6),
        dbc.Col(dcc.Graph(figure=map, id='map'), md=6)
    ])
], fluid=True)

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)