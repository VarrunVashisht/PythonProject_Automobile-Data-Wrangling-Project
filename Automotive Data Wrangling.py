import pandas as pd
import numpy as np

path = "raw_data_automotive.csv"
df = pd.read_csv(path, header=None)

# Giving names to the columns
columns = [
    "symboling",
    "normalized_losses",
    "make",
    "fuel_type",
    "aspiration",
    "num_doors",
    "body_style",
    "drive_wheels",
    "engine_location",
    "wheel_base",
    "length",
    "width",
    "height",
    "curb_weight",
    "engine_type",
    "num_cylinders",
    "engine_size",
    "fuel_system",
    "bore",
    "stroke",
    "compression_ratio",
    "horsepower",
    "peak_rpm",
    "city_mpg",
    "highway_mpg",
    "price"
]
df.columns = columns

# Replacing '?' with Nan
df.replace('?', np.nan, inplace=True)

# Convert Numeric Columns to Proper Type
numeric_cols = ["normalized_losses", "bore", "stroke", "horsepower", "peak_rpm", "price"]

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Handle Missing Values
df["normalized_losses"] = df["normalized_losses"].fillna(df["normalized_losses"].mean())
df["bore"] = df["bore"].fillna(df["bore"].mean())
df["stroke"] = df["stroke"].fillna(df["stroke"].mean())
df["horsepower"] = df["horsepower"].fillna(df["horsepower"].mean())
df["peak_rpm"] = df["peak_rpm"].fillna(df["peak_rpm"].mean())
df["price"] = df["price"].fillna(df["price"].mean())

df["num_doors"] = df["num_doors"].fillna(df["num_doors"].mode()[0])

# ALL columns summary (numeric + categorical):
print(df.describe(include="all"))

# Data Normalization
df["length_norm"] = df["length"] / df["length"].max()
df["width_norm"] = df["width"] / df["width"].max()
df["height_norm"] = df["height"] / df["height"].max()

# Binning (Categorizing Continuous Data)
bins = [0, 100, 150, 300]
labels = ["Low", "Medium", "High"]

df["hp_category"] = pd.cut(df["horsepower"], bins=bins, labels=labels)

#Indicator Variables (One-Hot Encoding)
df = pd.get_dummies(df, columns=["fuel_type", "aspiration", "drive_wheels"], drop_first=True)

#Simple Visualization (Beginner Friendly)
import matplotlib.pyplot as plt

plt.hist(df["price"], bins=20)
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("Distribution of Car Prices")
plt.show()

df.to_csv("cleaned_automobile_data.csv", index=False)








