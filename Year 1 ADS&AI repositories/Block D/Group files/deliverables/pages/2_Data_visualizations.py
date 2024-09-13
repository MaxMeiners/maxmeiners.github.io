import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

def set_page_configuration():
    """
    Sets the configuration for the data visualizations Streamlit page.
    """
    st.set_page_config(
    page_title="Total registered nuisance in Breda",
    page_icon=":bar_chart:",
    layout="wide",
    )

# Call the function to set the page configuration
set_page_configuration()

#Read in CSV file
registered_nuisance = pd.read_csv("datasets/registered_nuisance/geregistreerde_overlast_breda.csv", sep=";")

# Delete the row(s) where 'Perioden' column is '2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022'
registered_nuisance = registered_nuisance[registered_nuisance['Perioden'] != '2012']
registered_nuisance = registered_nuisance[registered_nuisance['Perioden'] != '2013']
registered_nuisance = registered_nuisance[registered_nuisance['Perioden'] != '2014']
registered_nuisance = registered_nuisance[registered_nuisance['Perioden'] != '2015']
registered_nuisance = registered_nuisance[registered_nuisance['Perioden'] != '2016']
registered_nuisance = registered_nuisance[registered_nuisance['Perioden'] != '2017']
registered_nuisance = registered_nuisance[registered_nuisance['Perioden'] != '2018']
registered_nuisance = registered_nuisance[registered_nuisance['Perioden'] != '2019']
registered_nuisance = registered_nuisance[registered_nuisance['Perioden'] != '2020']
registered_nuisance = registered_nuisance[registered_nuisance['Perioden'] != '2021']
registered_nuisance = registered_nuisance[registered_nuisance['Perioden'] != '2022']

# Reset the index
registered_nuisance.reset_index(drop=True, inplace=True)

# Split the "Perioden" column into 2 new columns named "Year" and "Month"
registered_nuisance[['Year', 'Month']] = registered_nuisance['Perioden'].str.split(' ', n=1, expand=True)
# Delete the "Perioden" column
registered_nuisance.drop('Perioden', axis=1, inplace=True)
# Delete "Regio's" column
registered_nuisance.drop("Regio's", axis=1, inplace=True)
# Delete the "Month" column
registered_nuisance.drop('Month', axis=1, inplace=True)

# Aggregate the data by year, but add the values of the "Overlast" column
registered_nuisance = registered_nuisance.groupby(['Year', 'Overlast']).sum().reset_index()

#Pivot the table
registered_nuisance = registered_nuisance.pivot(index='Overlast', columns='Year', values='Geregistreerde overlast (aantal)')

registered_nuisance.columns.name = None

#Mainpage
st.title(":bar_chart: Total registered nuisance in Breda")
st.markdown("This chart shows the total registered nuisance in in Breda from 2012 to 2023.")

# Transpose the DataFrame to switch the x-axis and y-axis
df_transposed = registered_nuisance.T

# Visualize the bar chart with custom axes
st.bar_chart(df_transposed)
    
st.markdown("---")

@st.cache_data(show_spinner=True)
def load_file():
    """
    Loads a CSV file containing registered crime data.

    Returns:
    crime_df (pandas.DataFrame): The loaded DataFrame containing registered crime data.
    """
    crime_df = pd.read_csv("datasets/registered_crime/registered_crime.csv", sep=';', low_memory=False) #Adding "low_memory=False" to prevent warning
    
    return crime_df

crime_df = load_file()

# Delete rows where "Wijken en buurten" is "Breda"
# Delete rows where "Soort misdrijf" is "Totaal misdrijven"
crime_df = crime_df[crime_df['Wijken en buurten'] != 'Breda']
crime_df = crime_df[crime_df['Soort misdrijf'] != 'Totaal misdrijven']

# Reset the index
crime_df.reset_index(drop=True, inplace=True)

# Split the "Perioden" column into 2 new columns named "Year" and "Month"
crime_df[['Year', 'Month']] = crime_df['Perioden'].str.split(' ', n=1, expand=True)

# Delete the "Perioden" column
crime_df.drop('Perioden', axis=1, inplace=True)

# Delete the "Month" column
crime_df.drop('Month', axis=1, inplace=True)

#replace "." in geregisreerde misdrijven with nan
crime_df['Geregistreerde misdrijven (aantal)'] = crime_df['Geregistreerde misdrijven (aantal)'].replace('       .', 0)

#convert geregisreerde misdrijven to int
crime_df['Geregistreerde misdrijven (aantal)'] = crime_df['Geregistreerde misdrijven (aantal)'].astype(int)

crime_df_agg = crime_df.groupby(["Wijken en buurten", "Soort misdrijf", "Year"]).sum().reset_index()

def crime_line_chart():
    """
    Displays a line chart showing crime data based on user-selected crimes and neighborhoods.

    The function uses Streamlit to create interactive elements for selecting crimes and neighborhoods.
    It retrieves data from a DataFrame called crime_df_agg and plots the selected data as a line chart.

    Returns:
    None
    """
    st.title('👮Crime Line Chart')
    selected_crimes = st.multiselect('Select crimes:', crime_df_agg['Soort misdrijf'].unique())
    selected_neighbourhood = st.multiselect('Select neighbourhood:', crime_df_agg['Wijken en buurten'].unique())
    selected_data = crime_df_agg[
        (crime_df_agg['Wijken en buurten'].isin(selected_neighbourhood)) &
        (crime_df_agg['Soort misdrijf'].isin(selected_crimes))
    ] if selected_crimes and selected_neighbourhood else None

    if selected_data is not None:
        fig, ax = plt.subplots(figsize=(10, 6))
        for crime in selected_crimes:
            for neighbourhood in selected_neighbourhood:
                crime_data = selected_data[
                    (selected_data['Soort misdrijf'] == crime) &
                    (selected_data['Wijken en buurten'] == neighbourhood)
                ]
                ax.plot(crime_data['Year'], crime_data['Geregistreerde misdrijven (aantal)'], label=f'{crime} - {neighbourhood}')
        ax.set_xlabel('Year')
        ax.set_ylabel('Geregistreerde misdrijven (aantal)')
        ax.set_title('Crime Line Chart')
        ax.tick_params(axis='x', rotation=45)
        ax.grid()
        ax.legend()

        st.pyplot(fig)

if __name__ == '__main__':
    crime_line_chart()

st.markdown("---")

st.title('📚Nuisance, unemployment and crime per neighbourhood')

@st.cache_data(show_spinner=True)
def load_merged_file():
    """
    Loads a merged CSV file as a pandas DataFrame.

    Returns:
    df (pandas.DataFrame): The loaded DataFrame containing the merged data from the CSV file.
    """
    df = pd.read_csv("datasets/merged.csv")
    return df

df = load_merged_file()

neighborhoods = df['Neighbourhood'].unique()
selected_neighborhood = st.selectbox("Select Neighborhood", neighborhoods)

if selected_neighborhood == "Brabantpark":
    st.balloons()

filtered_data = df[df['Neighbourhood'] == selected_neighborhood]

total_crimes_initial = filtered_data['Total crimes'].iloc[0]
total_nuisances_initial = filtered_data['Total nuisances'].iloc[0]
unemployment_initial = filtered_data['Unemployment'].iloc[0]

total_crimes_final = filtered_data['Total crimes'].iloc[-1]
total_nuisances_final = filtered_data['Total nuisances'].iloc[-1]
unemployment_final = filtered_data['Unemployment'].iloc[-1]

percentage_change_crimes = (total_crimes_final - total_crimes_initial) / total_crimes_initial * 100 / len(filtered_data)
percentage_change_nuisance = (total_nuisances_final - total_nuisances_initial) / total_nuisances_initial * 100 / len(filtered_data)
percentage_change_unemployment = (unemployment_final - unemployment_initial) / unemployment_initial * 100 / len(filtered_data)

st.write("Select the factors to visualize:")
show_crimes = st.checkbox("Crimes", value=True)
show_nuisances = st.checkbox("Nuisances", value=True)
show_unemployment = st.checkbox("Unemployment", value=True)

plt.figure(figsize=(10, 5))
bar_width = 0.3
years = filtered_data['Year']

if show_crimes:
    crimes = filtered_data['Total crimes']
    plt.bar(years, crimes, bar_width, label='Total Crimes')

if show_nuisances:
    nuisances = filtered_data['Total nuisances']
    plt.bar(years + bar_width, nuisances, bar_width, label='Total Nuisances')

if show_unemployment:
    unemployment = filtered_data['Unemployment']
    plt.bar(years + 2 * bar_width, unemployment, bar_width, label='Unemployment')

plt.xlabel('Year')
plt.ylabel('Count')
plt.title(f'Total Crimes, Total Nuisances, and Unemployment in {selected_neighborhood}')
plt.xticks(years + bar_width, years, rotation=90)
plt.legend()

st.pyplot(plt)

with st.expander("Description"):
    factors_description = ", ".join([factor for factor, show in zip(['Crimes', 'Nuisances', 'Unemployment'], [show_crimes, show_nuisances, show_unemployment]) if show])
    chart_description = f"This bar chart shows the trend(s) of the total {factors_description} in {selected_neighborhood} over the past 10 years."
    st.write(chart_description)

if show_crimes:
    st.write(f"Relative change in Total Crimes in {selected_neighborhood}: {percentage_change_crimes:.2f}%")
    if percentage_change_crimes > 0:
        st.write(f"Over the years, the relative change in Total Crimes in {selected_neighborhood} shows an increase of {percentage_change_crimes:.2f}%. This might indicate a decline in safety and security in the area.")
    else:
        st.write(f"Over the years, the relative change in Total Crimes in {selected_neighborhood} shows a decrease of {abs(percentage_change_crimes):.2f}%. This indicates improved safety and security.")

if show_nuisances:
    st.write(f"Relative change in Total Nuisances in {selected_neighborhood}: {percentage_change_nuisance:.2f}%")
    if percentage_change_nuisance > 0:
        st.write(f"The relative change in Total Nuisances in {selected_neighborhood} over the years shows an increase of {percentage_change_nuisance:.2f}%. It seems like there might be more community nuisances affecting the region.")
    else:
        st.write(f"The relative change in Total Nuisances in {selected_neighborhood} over the years shows a decrease of {abs(percentage_change_nuisance):.2f}%. It suggests efforts to address community nuisances and enhance the quality of life.")

if show_unemployment:
    st.write(f"Relative change in Unemployment in {selected_neighborhood}: {percentage_change_unemployment:.2f}%")
    if percentage_change_unemployment > 0:
        st.write(f"The relative change in Unemployment in {selected_neighborhood} over the years shows an increase of {percentage_change_unemployment:.2f}%. It might mean there are fewer job opportunities.")
    else:
        st.write(f"The relative change in Unemployment in {selected_neighborhood} over the years shows a decrease of {abs(percentage_change_unemployment):.2f}%. It indicates improved job opportunities and economic stability.")
