# In this exercise, you will use the dummy dataset you created to verify your operations on the Titanic dataset.

# Please Design unit tests to:

# ensure that you read in the dataset correctly (use the number of rows and columns as a test parameter)
# check if the function you created in the previous exercise to count the number of woman in the dataset returns the correct values, when you pass in the dummy dataset in place of the original dataset.
# check if the function you created in the previous exercise to return the average age of all passengers.


import Titanic
import pandas as pd
Titanic_csv=pd.read_csv("Python for Data Analysis/Week 1/data/Titanic_dummy.csv", sep=",")

# Add titanic unit tests here
def test_df_check():
    assert Titanic.df_check() == (10, 3)

def test_sex_check():
    assert Titanic.sex_check('Female') == 4

def test_avr_age():
    assert Titanic.avr_age() == 33
    