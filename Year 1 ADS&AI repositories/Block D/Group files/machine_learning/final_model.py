import joblib
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

DATASET_PATH = "./datasets/merged/merged_nuisance_next_year.csv"


def load_data():
    df = pd.read_csv(DATASET_PATH)

    return df


def perform_one_hot_encoding(df):
    df_encoded = pd.get_dummies(df, columns=['Neighbourhood'])

    return df_encoded


def train_test_split(df):
    df_train = df[df["Year"] < 2020]
    df_test = df[df["Year"] >= 2020]
    X_train = df_train.drop(["Total Nuisance Next Year", "Year"], axis=1)
    X_test = df_test.drop(["Total Nuisance Next Year", "Year"], axis=1)
    y_train = df_train["Total Nuisance Next Year"]
    y_test = df_test["Total Nuisance Next Year"]

    return X_train, X_test, y_train, y_test


df = load_data()

# perform one-hot encoding for the "Neighbourhood" variable
df = perform_one_hot_encoding(df)

# split data into train, test sets
X_train, X_test, y_train, y_test = train_test_split(df)


# train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# evaluate the model on the testing set
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"Root mean squared error = {rmse:.2f}")
print(f"R-squared = {r2:.2f}")

# Save the model to a file
joblib.dump(model, "./machine_learning/nuisance_predictor_model.sav")
