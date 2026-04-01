# Importing Libraries
import pandas as pd
from sklearn.linear_model import LinearRegression

# Loading Data
df_emp = pd.read_csv("Data/occupazione.csv")
df_unemp = pd.read_csv("Data/disoccupazione.csv")

# Filtering Data
df_emp = df_emp[(df_emp["sex"] == "Total") & (df_emp["age"] == "15+")]
df_unemp = df_unemp[(df_unemp["sex"] == "Total") & (df_unemp["age"] == "15+")]

# Merge Data
df_merged = pd.merge(df_emp, df_unemp, on=["country", "year"], suffixes=("_emp", "_unemp"))

# Sort Merged Data
df_merged = df_merged.sort_values(by=["country", "year"])

# Choose Input(X) and Output(y)
X = df_merged[["year"]]
y_emp = df_merged["obs_value_emp"]
y_unemp = df_merged["obs_value_unemp"]

# Define Models
model_emp = LinearRegression()
model_unemp = LinearRegression()

# Train Models
model_emp.fit(X, y_emp)
model_unemp.fit(X, y_unemp)

# User Input
year = int(input("Enter year to predict enployment and unemployment rates: "))
year_df = pd.DataFrame([[year]], columns=["year"])

# Predictions
predicted_emp = model_emp.predict(year_df)
predicted_unemp = model_unemp.predict(year_df)

# Result
print(f"Emplyment rates for year {year}: {predicted_emp}\nUnemployment rates for year {year}: {predicted_unemp}")