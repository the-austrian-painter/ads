# -*- coding: utf-8 -*-
"""preprocessing_exercise.ipynb

"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.read_csv('winequality-red.csv')
df = pd.DataFrame(df)
df.head()

X = df.drop("quality", axis=1)
y = df["quality"]

standard_scaler = StandardScaler()
X_standardized = standard_scaler.fit_transform(X)
df_standardized = pd.DataFrame(
X_standardized,
columns=X.columns
)
df_standardized.head()

minmax_scaler = MinMaxScaler()
X_normalized = minmax_scaler.fit_transform(X)
df_normalized = pd.DataFrame(
X_normalized,
columns=X.columns
)
df_normalized.head()

"""Exercise 2"""

import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.read_excel('customer_preprocessing_dataset.xlsx')
print("Original Dataset:")
display(df.head())

# Separate numerical and categorical columns
num_cols = ["Age", "Annual_Income"]
cat_cols = ["Gender", "City", "Purchased"]
# Numerical Imputation (Mean)
num_imputer = SimpleImputer(strategy="mean")
df[num_cols] = num_imputer.fit_transform(df[num_cols])
# Categorical Imputation (Most Frequent)
cat_imputer = SimpleImputer(strategy="most_frequent")
df[cat_cols] = cat_imputer.fit_transform(df[cat_cols])
print("\nDataset after Missing Value Imputation:")
display(df.head())

label_encoder = LabelEncoder()
df["Purchased"] = label_encoder.fit_transform(df["Purchased"])

df_encoded = pd.get_dummies(
df,
columns=["Gender", "City"],
drop_first=True
)
print("\nDataset after Encoding:")
display(df_encoded.head())

# Separate features and target
X = df_encoded.drop(["Customer_ID", "Purchased"], axis=1)
y = df_encoded["Purchased"]
# Standardization
std_scaler = StandardScaler()
X_standardized = std_scaler.fit_transform(X)
df_standardized = pd.DataFrame(
X_standardized,
columns=X.columns
)
# Normalization
minmax_scaler = MinMaxScaler()
X_normalized = minmax_scaler.fit_transform(X)
df_normalized = pd.DataFrame(
X_normalized,
columns=X.columns
)

print("Standardized Dataset (Mean=0, Std=1):")
display(df_standardized.head())

print("Normalized Dataset (Range 0–1):")
display(df_normalized.head())

