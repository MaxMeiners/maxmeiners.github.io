import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

def set_page_configuration():
    """
    Sets the configuration for the public nuisance predictor Streamlit page.
    """
    st.set_page_config(
    page_title="Machine Learning model",
    page_icon="🎯",
    layout="wide",
    )

# Call the function to set the page configuration
set_page_configuration()

# Load the trained machine learning model
model = joblib.load(
    "machine_learning/nuisance_predictor_model.sav"
)


neighbourhoods = [
    'Bavel',
    'Belcrum',
    'Biesdonk',
    'Blauwe Kei',
    'Boeimeer',
    'Brabantpark',
    'Buitengebied Bavel',
    'Buitengebied Prinsenbeek',
    'Buitengebied Teteringen',
    'Buitengebied Ulvenhout',
    'Chassé',
    'City',
    'Doornbos-Linie',
    'Effen-Rith',
    'Emer',
    'Fellenoord',
    'Gageldonk',
    'Geeren-noord',
    'Geeren-zuid',
    'Ginneken',
    'Haagpoort',
    'Hagebeemd',
    'Hazeldonk',
    'Heilaar',
    'Heksenwiel',
    'Heusdenhout',
    'Heuvel',
    'Hoogeind',
    'Kesteren',
    'Kievitsloop',
    'Kroeten',
    'Krogten',
    'Liesbos',
    'Mastbos',
    'Moleneind-oost',
    'Muizenberg',
    'Nieuw Wolfslaar',
    'Overakker',
    'Overkroeten',
    'Princenhage',
    'Prinsenbeek',
    'Ruitersbos',
    'Schorsmolen',
    'Sportpark',
    'Station',
    'Steenakker',
    'Teteringen',
    'Tuinzigt',
    'Ulvenhout',
    'Valkenberg',
    'Vuchtpolder',
    'Waterdonken',
    'Westerpark',
    'Wisselaar',
    'Ypelaar',
    'Zandberg',
]


def encode_neighbourhood(neighbourhood):
    """
    Encodes the selected neighbourhood by creating a dictionary with encoded values for each neighbourhood.

    Parameters:
        neighbourhood (str): The name of the neighbourhood to be encoded.

    Returns:
        dict: A dictionary with encoded values for each neighbourhood, where the selected neighbourhood has a value of 1 and others have a value of 0.
    """
    data = {
        'Neighbourhood_Bavel': 0,
        'Neighbourhood_Belcrum': 0,
        'Neighbourhood_Biesdonk': 0,
        'Neighbourhood_Blauwe Kei': 0,
        'Neighbourhood_Boeimeer': 0,
        'Neighbourhood_Brabantpark': 0,
        'Neighbourhood_Buitengebied Bavel': 0,
        'Neighbourhood_Buitengebied Prinsenbeek': 0,
        'Neighbourhood_Buitengebied Teteringen': 0,
        'Neighbourhood_Buitengebied Ulvenhout': 0,
        'Neighbourhood_Chassé': 0,
        'Neighbourhood_City': 0,
        'Neighbourhood_Doornbos-Linie': 0,
        'Neighbourhood_Effen-Rith': 0,
        'Neighbourhood_Emer': 0,
        'Neighbourhood_Fellenoord': 0,
        'Neighbourhood_Gageldonk': 0,
        'Neighbourhood_Geeren-noord': 0,
        'Neighbourhood_Geeren-zuid': 0,
        'Neighbourhood_Ginneken': 0,
        'Neighbourhood_Haagpoort': 0,
        'Neighbourhood_Hagebeemd': 0,
        'Neighbourhood_Hazeldonk': 0,
        'Neighbourhood_Heilaar': 0,
        'Neighbourhood_Heksenwiel': 0,
        'Neighbourhood_Heusdenhout': 0,
        'Neighbourhood_Heuvel': 0,
        'Neighbourhood_Hoogeind': 0,
        'Neighbourhood_Kesteren': 0,
        'Neighbourhood_Kievitsloop': 0,
        'Neighbourhood_Kroeten': 0,
        'Neighbourhood_Krogten': 0,
        'Neighbourhood_Liesbos': 0,
        'Neighbourhood_Mastbos': 0,
        'Neighbourhood_Moleneind-oost': 0,
        'Neighbourhood_Muizenberg': 0,
        'Neighbourhood_Nieuw Wolfslaar': 0,
        'Neighbourhood_Overakker': 0,
        'Neighbourhood_Overkroeten': 0,
        'Neighbourhood_Princenhage': 0,
        'Neighbourhood_Prinsenbeek': 0,
        'Neighbourhood_Ruitersbos': 0,
        'Neighbourhood_Schorsmolen': 0,
        'Neighbourhood_Sportpark': 0,
        'Neighbourhood_Station': 0,
        'Neighbourhood_Steenakker': 0,
        'Neighbourhood_Teteringen': 0,
        'Neighbourhood_Tuinzigt': 0,
        'Neighbourhood_Ulvenhout': 0,
        'Neighbourhood_Valkenberg': 0,
        'Neighbourhood_Vuchtpolder': 0,
        'Neighbourhood_Waterdonken': 0,
        'Neighbourhood_Westerpark': 0,
        'Neighbourhood_Wisselaar': 0,
        'Neighbourhood_Ypelaar': 0,
        'Neighbourhood_Zandberg': 0,
    }

    encoded_name = "Neighbourhood_" + neighbourhood

    data[encoded_name] = 1

    return data


# Define a function that takes in user entered variables as input and returns the predicted public nuisances
def predict_nuisance(num_crimes, num_unemployed, population, neighbourhood):
    """
    Predicts the nuisance level based on input features and the selected neighbourhood.

    Parameters:
        num_crimes (int): The number of crimes in the area.
        num_unemployed (int): The number of unemployed individuals in the area.
        population (int): The population of the area.
        neighbourhood (str): The name of the neighbourhood.

    Returns:
        int: The predicted nuisance level, represented as a non-negative integer.
    """
    input = [num_crimes, num_unemployed, population]

    encoded_neighbourhood = encode_neighbourhood(neighbourhood)
    X = np.array([input + list(encoded_neighbourhood.values())])
    columns = ['Total crimes', 'Unemployment', 'Population'] + list(
        encoded_neighbourhood.keys()
    )
    X = pd.DataFrame(X, columns=columns)

    prediction = model.predict(X)

    # Return non-negative integer
    return int(max(0, round(prediction[0], 0)))


# Define the user interface for the app
st.title("Public Nuisance Predictor")

# year = st.slider("Year", 2010, 2050, 2022)
neighbourhood = st.selectbox("Neighborhood", neighbourhoods)
population = st.slider("Population", 45, 10980, 1000)
num_crimes = st.slider("Number of Crimes", 2, 2100, 2)
num_unemployed = st.slider("Number of Unemployed People", 0, 290, 0)


# Add a button to trigger the model prediction
if st.button("Predict public nuisances for next year"):
    result = predict_nuisance(num_crimes, num_unemployed, population, neighbourhood)
    st.markdown("### Prediction Results")
    st.write(
        f"The predicted number of public nuisance reports next year in {neighbourhood} for the selected inputs is:   **{result}**."
    )