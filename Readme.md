# Geospatial Analysis of Suicide Trends in the United States: An Integrated Multi-View Visualization Study

This repository contains the project materials and code for a comprehensive geospatial analysis of suicide trends in the United States, integrating multi-view visualizations. The aim is to provide a holistic understanding of suicide rates, allowing users to discern trends, disparities, correlations, and anomalies through different perspectives.

## Contributors
- Jai Reddy Kukunuru (kukuruj@oregonstate.edu)

## Motivation
Suicide is a significant public health crisis in the United States, influenced by demographic and locational variables. Analyzing suicide rates across diverse demographic categories and integrating geospatial patterns can provide valuable insights into the interplay of location and demographic factors in the manifestation of suicide rates. This understanding is crucial for devising effective prevention strategies.

## Description
This project focuses on geospatial analysis of suicide trends, incorporating multi-view visualization techniques. Three main geospatial visualization techniques are explored: Choropleth Maps, Heat Maps, and Hexagonal Binning. These techniques are utilized to represent suicide rates across different demographic categories and geographical regions, allowing for a comprehensive analysis.

## Data Source
The primary data source used in this project is from [Data.gov](https://catalog.data.gov/dataset/death-rates-for-suicide-by-sex-race-hispanic-origin-and-age-united-states-020c1), providing death rates for suicide by sex, race, Hispanic origin, and age in the United States.

## Comparison of Geospatial Visualization Techniques
In this project, we compare and analyze three geospatial visualization techniques:
- **Choropleth Maps**: Used to represent suicide rates by coloring geographical regions according to the variable's value, helping identify spatial patterns.
- **Heat Maps**: Represent data on a grid, using color intensity to indicate the variable's value, providing a granular view of suicide rates and variations.
- **Hexagonal Binning**: Aggregates data into hexagonal bins, allowing for a detailed representation of local patterns within larger regions.

## Multiview Visualization
The multiview visualization in this project aims to present a comprehensive understanding of suicide rates, utilizing different components:
- **What Component (Bar Chart)**: Displays death rates per state for the latest available year, offering an overview of variation in death rates across states.
- **Why Component (Line Chart)**: Illustrates the temporal trend in death rates for the state with the highest number of deaths, aiding in identifying patterns and trends over the years.
- **When Component (Line Chart)**: Shows the trend in death rates for the state with the highest number of deaths across various years, aiding in identifying temporal patterns.
- **Where Component (Geospatial Map)**: Visualizes the geographical distribution of the states using markers on the map, offering insights into the spatial distribution of death rates.

The interaction between these components enables a holistic exploration of the dataset, facilitating a more informed analysis.

## Technologies Used
- **Pandas**: For loading and manipulating the dataset.
- **Plotly Express**: For creating interactive visualizations, including bar charts, line charts, and geospatial maps.
- **Dash**: For creating the web application framework for displaying the multiview visualization.

## Running the Application
The Dash application was used to display the multiview visualization in a web browser. Users can interact with the visualizations and explore the data through the interactive features provided.

## Design Principles
Several design principles were employed in creating the multiview visualization to enhance its effectiveness and usability, including consistency, clarity, visual hierarchy, color encoding, interactivity, and responsive design.

For more details, refer to the [data source](https://catalog.data.gov/dataset/death-rates-for-suicide-by-sex-race-hispanic-origin-and-age-united-states-020c1).

Feel free to explore the code and project materials for a comprehensive understanding of the geospatial analysis of suicide trends in the United States. If you have any questions or suggestions, please contact the contributors mentioned above.