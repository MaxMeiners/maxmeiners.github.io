import pandas as pd

Titanic=pd.read_csv("Python for Data Analysis/Week 1/data/Titanic_dummy.csv", sep=",")
print(Titanic.info())

def df_check():
    return Titanic.shape
    # return ([len(Titanic), len(Titanic.columns)])

# print(df_check())

def sex_check(G):
        return (Titanic['Sex']==G).sum()
def avr_age():
    return (round(Titanic['Age'].mean()))