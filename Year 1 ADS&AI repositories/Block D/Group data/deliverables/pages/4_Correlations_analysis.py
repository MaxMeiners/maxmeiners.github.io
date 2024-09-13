import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import io

def set_page_configuration():
    """
    Sets the configuration for the correlations analysis Streamlit page.
    """
    st.set_page_config(
        page_title="Correlations analysis",
        page_icon="📈",
        layout="wide",
    )

def load_data(file_path):
    """
    Loads data from a CSV file.
    
    Parameters:
    - file_path (str): Path to the CSV file.
    
    Returns:
    - pandas.DataFrame: Loaded data as a DataFrame.
    """
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    """
    Preprocesses the data by removing unnecessary columns.
    
    Parameters:
    - df (pandas.DataFrame): Input DataFrame.
    
    Returns:
    - pandas.DataFrame: Preprocessed DataFrame.
    """
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    df = df.drop(columns=["Neighbourhood"])
    return df

def calculate_correlation_matrix(df):
    """
    Calculates the correlation matrix for the given DataFrame.
    
    Parameters:
    - df (pandas.DataFrame): Input DataFrame.
    
    Returns:
    - pandas.DataFrame: Correlation matrix.
    """
    correlation_matrix = df.corr()
    correlation_matrix = correlation_matrix.mask(correlation_matrix == 1)
    return correlation_matrix

def style_correlation_matrix(correlation_matrix, correlation_colors):
    """
    Applies styling to the correlation matrix based on predefined color ranges.
    
    Parameters:
    - correlation_matrix (pandas.DataFrame): Correlation matrix.
    - correlation_colors (dict): Dictionary mapping value ranges to colors.
    
    Returns:
    - pandas.Styler: Styled correlation matrix.
    """
    correlation_matrix_styled = correlation_matrix.style.format("{:.2f}").applymap(
        lambda x: f'background-color: {next((v for k, v in correlation_colors.items() if k[0] <= x <= k[1]), "white")}; color: black',
        subset=pd.IndexSlice[:, :],
    )
    return correlation_matrix_styled

def create_legend_patches(legend_labels, legend_colors):
    """
    Creates legend patches for the correlation colors.
    
    Parameters:
    - legend_labels (list): List of legend labels.
    - legend_colors (list): List of legend colors.
    
    Returns:
    - list: List of matplotlib.patches.Patch objects.
    """
    legend_patches = [
        mpatches.Patch(facecolor=color, edgecolor='black', label=label)
        for color, label in zip(legend_colors, legend_labels)
    ]
    return legend_patches

def plot_legend(legend_patches):
    """
    Plots the legend using the provided patches.
    
    Parameters:
    - legend_patches (list): List of matplotlib.patches.Patch objects.
    """
    fig, ax = plt.subplots()
    ax.legend(handles=legend_patches, loc='center', title='Correlation')
    ax.axis('off')
    return fig

def save_plot_to_buffer(fig):
    """
    Saves the figure to an in-memory buffer.
    
    Parameters:
    - fig (matplotlib.figure.Figure): Figure object to be saved.
    
    Returns:
    - io.BytesIO: In-memory buffer containing the saved image.
    """
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0)
    buffer.seek(0)
    return buffer

def display_image_from_buffer(buffer):
    """
    Displays the saved image from the buffer in Streamlit.
    
    Parameters:
    - buffer (io.BytesIO): In-memory buffer containing the image.
    """
    st.image(buffer)

# Example usage
set_page_configuration()
df = load_data('datasets/merged.csv')
df = preprocess_data(df)
correlation_matrix = calculate_correlation_matrix(df)

correlation_colors = {
    (-1.0, -0.5): '#F8766D',
    (-0.5, -0.2): '#FFB8A2',
    (-0.2, 0.2): '#FFFFCC',
    (0.2, 0.5): '#A2D8F0',
    (0.5, 1.0): '#61A4FF',
}

correlation_matrix_styled = style_correlation_matrix(correlation_matrix, correlation_colors)

st.title("Correlations analysis")
st.write("Correlation Matrix:")
st.dataframe(correlation_matrix_styled, height=400)

legend_labels = [
    'Negative correlation',
    'Small negative correlation',
    'No correlation',
    'Small positive correlation',
    'Positive correlation',
]
legend_colors = ['#F8766D', '#FFB8A2', '#FFFFCC', '#A2D8F0', '#61A4FF']
legend_patches = create_legend_patches(legend_labels, legend_colors)

st.write("Legend:")
fig = plot_legend(legend_patches)
buffer = save_plot_to_buffer(fig)
display_image_from_buffer(buffer)
