import streamlit as st
import folium
from streamlit_folium import folium_static
from shapely.geometry import shape
import branca
import geopandas as gpd
import pandas as pd

# Load shapefile
boa_2018 = gpd.read_file(r'C:\Users\maxme\OneDrive\Documenten\GitHub\2022-23d-1fcmgt-reg-ai-01-group-team10\baseline_ML_EDA\datasets\boa\CC_2018.shp')
boa_2019 = gpd.read_file(r'C:\Users\maxme\OneDrive\Documenten\GitHub\2022-23d-1fcmgt-reg-ai-01-group-team10\baseline_ML_EDA\datasets\boa\CC_2019.shp')
boa_2020 = gpd.read_file(r'C:\Users\maxme\OneDrive\Documenten\GitHub\2022-23d-1fcmgt-reg-ai-01-group-team10\baseline_ML_EDA\datasets\boa\CC_2020.shp')
boa_2021 = gpd.read_file(r'C:\Users\maxme\OneDrive\Documenten\GitHub\2022-23d-1fcmgt-reg-ai-01-group-team10\baseline_ML_EDA\datasets\boa\CC_2021.shp')
boa_2022 = gpd.read_file(r'C:\Users\maxme\OneDrive\Documenten\GitHub\2022-23d-1fcmgt-reg-ai-01-group-team10\baseline_ML_EDA\datasets\boa\CC_2022.shp')
gpkg_data = gpd.read_file(r'C:\Users\maxme\OneDrive\Documenten\GitHub\2022-23d-1fcmgt-reg-ai-01-group-team10\baseline_ML_EDA\datasets\boa\geographical_shapes_keys\breda_grid_keys.gpkg')
cbs = gpd.read_file(r'C:\Users\maxme\OneDrive\Documenten\GitHub\2022-23d-1fcmgt-reg-ai-01-group-team10\baseline_ML_EDA\datasets\boa\cbs_breda_grid.gpkg')

cbs = cbs.rename(columns={'cbs_grid_code': 'CBS_code'})

merged_data_2022 = boa_2022.merge(cbs, on='CBS_code')

# Define color mapping for each unique value in the "Soort" column
color_mapping = {
    "Afval": "blue",
    "Zwervers": "green",
    "Drugs/alcohol": "red",
    "Jeugd": "orange",
    "Parkeeroverlast": "purple",
    "Fietsoverlast": "yellow",
    "Wildplassen": "gray"
}

# Create a folium Map object
m = folium.Map()
print(merged_data_2022)
# Convert the merged_data DataFrame to GeoJSON-like format
features = []
for index, row in merged_data_2022.iterrows():
    geometry = shape(row['geometry_y'])
    feature = {
        'type': 'Feature',
        'geometry': geometry.__geo_interface__,
        'properties': {
            'Soort': row['Soort'],
            'Count': row['Count']
        }
    }
    features.append(feature)

# Create a GeoJson object for all features
geojson = folium.GeoJson(
    data={
        'type': 'FeatureCollection',
        'features': features
    },
    name='Categories',
    style_function=lambda feature: {
        'fillColor': color_mapping[feature['properties']['Soort']],
        'color': 'black',
        'weight': 1,
        'fillOpacity': 0.7,
        'radius': feature['properties']['Count'] * 10
    }
)

# Add the GeoJson object to the map
geojson.add_to(m)

# Add layer control to toggle the GeoJson object visibility
folium.LayerControl().add_to(m)

# Display the map using Streamlit
st.title("Interactive Map")
folium_static(m)