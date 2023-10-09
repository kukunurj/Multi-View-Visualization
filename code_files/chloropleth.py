import pandas as pd
import plotly.express as px

# Load the preprocessed CSV file
df = pd.read_csv('new_file.csv')

# Create the choropleth map
fig = px.choropleth(df, locations='state_abbr', color='RATE',
                    hover_name='FullGeoName', locationmode='USA-states',
                    animation_frame='YEAR',
                    title='Choropleth Map of RATE by State over Years',
                    color_continuous_scale=px.colors.sequential.Plasma)

fig.update_layout(geo_scope='usa')  # limit map scope to USA
fig.show()
