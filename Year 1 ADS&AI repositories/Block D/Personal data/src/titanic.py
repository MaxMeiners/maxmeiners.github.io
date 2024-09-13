import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn

# Load the data
df = pd.read_csv('titanic.csv')

# Data Exploration
df.head()
df.info()