import streamlit as st
import folium
from streamlit_folium import folium_static
import branca.colormap
from shapely.geometry import shape
import pandas as pd
import geopandas as gpd

def set_page_configuration():
    """
    Sets the configuration for the BOA map visualization Streamlit page.
    """
    st.set_page_config(
    page_title="Map of registered nuisances in Breda",
    page_icon="🗺️",
    layout="wide",
    )

# Call the function to set the page configuration
set_page_configuration()

st.title("🗺️Map of registered nuisances in Breda")
st.markdown("On the slider beneath you can select the year you want to see the nuisances of.")

@st.cache_data(show_spinner=True)
def load_files():
    """
    Loads multiple shapefiles and geopackage files containing geographical and census data.

    Returns:
    boa_2018, boa_2019, boa_2020, boa_2021, boa_2022 (geopandas.GeoDataFrame): The loaded shapefile data for different years.
    gpkg_data (geopandas.GeoDataFrame): The loaded geopackage data.
    cbs (geopandas.GeoDataFrame): The loaded census data.

    Note:
    The column 'cbs_grid_code' in 'cbs' is renamed to 'CBS_code' in order to merge with CBS data.
    """
    boa_2018 = gpd.read_file('datasets/boa/CC_2018.shp')
    boa_2019 = gpd.read_file('datasets/boa/CC_2019.shp')
    boa_2020 = gpd.read_file('datasets/boa/CC_2020.shp')
    boa_2021 = gpd.read_file('datasets/boa/CC_2021.shp')
    boa_2022 = gpd.read_file('datasets/boa/CC_2022.shp')
    gpkg_data = gpd.read_file('datasets/boa/geographical_shapes_keys/breda_grid_keys.gpkg')
    cbs = gpd.read_file('datasets/boa/cbs_breda_grid.gpkg')
    
    # Renaming column name in order to merge with CBS data
    cbs = cbs.rename(columns={'cbs_grid_code': 'CBS_code'})
    
    return boa_2018, boa_2019, boa_2020, boa_2021, boa_2022, gpkg_data, cbs


@st.cache_data(show_spinner=True)
def merge_data(_boa_2018, _boa_2019, _boa_2020, _boa_2021, _boa_2022, _cbs):
    """
    Merges shapefile data with census data for different years.

    Args:
    _boa_2018, _boa_2019, _boa_2020, _boa_2021, _boa_2022 (geopandas.GeoDataFrame): Shapefile data for different years.
    _cbs (geopandas.GeoDataFrame): Census data.

    Returns:
    merged_data_2018, merged_data_2019, merged_data_2020, merged_data_2021, merged_data_2022 (geopandas.GeoDataFrame):
    The merged data for different years.

    Note:
    The merge is performed based on the 'CBS_code' column.
    """
    # Merge data with shape files
    merged_data_2018 = _boa_2018.merge(_cbs, on='CBS_code')
    merged_data_2019 = _boa_2019.merge(_cbs, on='CBS_code')
    merged_data_2020 = _boa_2020.merge(_cbs, on='CBS_code')
    merged_data_2021 = _boa_2021.merge(_cbs, on='CBS_code')
    merged_data_2022 = _boa_2022.merge(_cbs, on='CBS_code')
    
    return merged_data_2018, merged_data_2019, merged_data_2020, merged_data_2021, merged_data_2022

# Load shape files and geopackage files
boa_2018, boa_2019, boa_2020, boa_2021, boa_2022, gpkg_data, cbs = load_files()

# Merge data with shape files
merged_data_2018, merged_data_2019, merged_data_2020, merged_data_2021, merged_data_2022 = merge_data(boa_2018, boa_2019, boa_2020, boa_2021, boa_2022, cbs)
selected_year = None  # Global variable to store the selected year

def display_map():
    """
    Displays an interactive map with categorized markers based on selected data.

    Note:
    This function relies on external libraries such as folium and branca.

    Requirements:
    - folium
    - branca

    Returns:
    None
    """
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

    # Retrieve the selected year data from the year_data_mapping dictionary
    year_data = year_data_mapping[selected_year]

    # Create a folium Map object
    m = folium.Map()

    # Create feature groups and styles for each category
    category_groups = {}
    category_styles = {}
    for category, color in color_mapping.items():
        category_groups[category] = folium.FeatureGroup(name=category)
        category_styles[category] = {
            'fillColor': color,
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.7
        }

    # Convert the merged_data DataFrame to GeoJSON-like format
    year_data = year_data_mapping[selected_year]
    for index, row in year_data.iterrows():
        geometry = shape(row['geometry_y'])
        feature = {
            'type': 'Feature',
            'geometry': geometry.__geo_interface__,
            'properties': {
                'Soort': row['Soort'],
                'Count': row['Count']
            }
        }
        category = row['Soort']

        # Add the feature to the corresponding category group with the appropriate style
        folium.GeoJson(feature, style_function=lambda feature, c=category: category_styles[c]).add_to(category_groups[category])

    # Add the category groups to the map
    for group in category_groups.values():
        group.add_to(m)

    # Create a colormap
    colormap = branca.colormap.LinearColormap(
        colors=['blue', 'green', 'red', 'orange', 'purple', 'yellow', 'gray'],
        index=[0, 1, 2, 3, 4, 5, 6],
        vmin=0,
        vmax=6
    )

    # Define the legend HTML
    legend_html = '''
         <div style="position: fixed; 
                     bottom: 50px; left: 50px; width: 160px; height: 260px; 
                     border:2px solid grey; z-index:9999; font-size:14px;
                     background-color: white;
                     opacity: 0.9;
                     ">
             <p style="margin: 10px;"><b>Legend</b></p>
             <p style="margin: 10px;"><span onclick="toggleCategory('Afval')" style='background:blue;'>&nbsp;&nbsp;&nbsp;&nbsp;</span> Afval</p>
             <p style="margin: 10px;"><span onclick="toggleCategory('Zwervers')" style='background:green;'>&nbsp;&nbsp;&nbsp;&nbsp;</span> Zwervers</p>
             <p style="margin: 10px;"><span onclick="toggleCategory('Drugs/alcohol')" style='background:red;'>&nbsp;&nbsp;&nbsp;&nbsp;</span> Drugs/alcohol</p>
             <p style="margin: 10px;"><span onclick="toggleCategory('Jeugd')" style='background:orange;'>&nbsp;&nbsp;&nbsp;&nbsp;</span> Jeugd</p>
             <p style="margin: 10px;"><span onclick="toggleCategory('Parkeeroverlast')" style='background:purple;'>&nbsp;&nbsp;&nbsp;&nbsp;</span> Parkeeroverlast</p>
             <p style="margin: 10px;"><span onclick="toggleCategory('Fietsoverlast')" style='background:yellow;'>&nbsp;&nbsp;&nbsp;&nbsp;</span> Fietsoverlast</p>
             <p style="margin: 10px;"><span onclick="toggleCategory('Wildplassen')" style='background:gray;'>&nbsp;&nbsp;&nbsp;&nbsp;</span> Wildplassen</p>
         </div>
    '''

    # Create a DivIcon with the legend HTML
    legend = folium.features.DivIcon(html=legend_html)

    # Add the legend to the map at a specific location
    legend_location = 'bottomleft'
    legend_offset = (50, 50)
    folium.map.Marker(
        [m.get_bounds()[0][0], m.get_bounds()[1][1]],  # Adjust the coordinates based on your desired location
        icon=legend,
        draggable=False
    ).add_to(m)

    # Add layer control to toggle the category groups visibility
    folium.LayerControl().add_to(m)

    # Create a JavaScript function to toggle the visibility of a category group
    toggle_script = '''
    <script>
        function toggleCategory(category) {
            var group = document.querySelector('.leaflet-pane.leaflet-overlay-pane .feature-group-' + category);
            if (group.style.display === 'none') {
                group.style.display = 'block';
            } else {
                group.style.display = 'none';
            }
        }
    </script>
    '''

    # Add the toggle script to the map
    m.get_root().html.add_child(folium.Element(toggle_script))

    # Fit the map bounds to ensure all markers are visible
    m.fit_bounds(m.get_bounds())

    # Display the map
    folium_static(m)

# Load the map data for each year (adjust the variable names and data sources as needed)
data_2018 = merged_data_2018
data_2019 = merged_data_2019
data_2020 = merged_data_2020
data_2021 = merged_data_2021
data_2022 = merged_data_2022

# Create a dictionary mapping years to their respective data
year_data_mapping = {
    2018: data_2018,
    2019: data_2019,
    2020: data_2020,
    2021: data_2021,
    2022: data_2022
}

# Create a slider widget to select the year and update the map
selected_year = st.slider("Year", min_value=min(year_data_mapping), max_value=max(year_data_mapping))
display_map()