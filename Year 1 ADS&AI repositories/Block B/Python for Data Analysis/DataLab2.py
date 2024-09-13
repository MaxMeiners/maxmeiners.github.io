##########################################################################################################
# Week 1, Datalab 2

# Q.5 RIVM Vaccine Registration
## Write a Python function which prints out the location for a user supplied year of birth. 
#Use a Pandas dataframe to store and retrieve data. 
# Last, write a unit test in the DataLab2Test.py file to ensure that your code is working reliably.

import pandas as pd

def rivm_pandas(dob):
    vaccines = {
    'year':['1931 or earlier','1932 - 1936','1937 - 1941','1942 - 1946','1947 - 1951','1952 - 1955','1956 - 1957','1958 - 1960','1961 - 1971','1972 - 1981','1982 - 1991','1992 or later'],
    'city':['Groningen','Arnhem','Breda','Harlingen','Edam','Amsterdam','Sittard','Rotterdam','Groningen','Arnhem','Breda','Maastricht']
    }
    new_frame = pd.DataFrame(vaccines)
    new_frame = new_frame.set_index('year')
   
    return new_frame.loc[dob,'city']