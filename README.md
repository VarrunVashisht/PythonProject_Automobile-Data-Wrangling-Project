📘 Automobile Data Wrangling Project (Beginner Friendly)

This project is a complete A → Z beginner-friendly data wrangling walkthrough, using the Automobile Dataset.
The goal is to help new learners understand how real-world data is cleaned, prepared, and transformed before analysis or machine learning.

The dataset used in this project was provided as a CSV file with no column names, multiple missing values, and several columns stored as wrong datatypes — making it a perfect hands-on learning example.

🔍 Project Overview

In this project, we performed a full data-wrangling pipeline:

Loaded raw data (CSV with no headers)

Added proper column names

Identified and replaced missing values (?)

Converted columns to correct datatypes

Cleaned missing values using appropriate strategies

Explored the dataset using descriptive statistics

Normalized numerical features

Created binned (categorical) variables

Applied one-hot encoding for categorical columns

Visualized data distributions

Exported a cleaned version of the dataset

Created practice questions for learning

This README explains each step in simple language, perfect for beginners learning data wrangling.

📂 Dataset Description

The dataset contains information about automobiles, including:

Car manufacturer

Fuel type

Body style

Engine specifications

Miles per gallon

Price

And more…

The raw file was messy:

No headers

Missing values represented as "?"

Some numeric columns stored as strings

Several missing doors, horsepower, and price entries

This made it an excellent dataset for practicing data cleaning!

🧹 Step-by-Step What We Did
🟦 1. Loaded the Dataset (without headers)

We loaded the CSV using Pandas and treated the first row as data—not column names—because the file had no headers.

This let us start from scratch and understand the raw structure clearly.

🟩 2. Added Official Column Names

We assigned proper column names based on the structure of the UCI Automobile dataset.
Examples:

make

fuel_type

engine_size

city_mpg

price

etc.

Good column names make the dataset easier to understand and work with.

🟧 3. Replaced "?" With Actual Missing Values (NaN)

The dataset used "?" to represent missing values.
We replaced all "?" with NaN.

Why?
Because Pandas can only detect missing values if they are represented correctly.

🟨 4. Converted Numeric Columns to Real Numbers

Columns like:

price

horsepower

bore

stroke

were stored as text, not numbers.

We converted them to numeric datatypes so they could be used for:

math

statistics

machine learning

🟫 5. Handled Missing Values

We used two strategies:

📌 Numeric columns → filled using mean

Example:

Missing horsepower

Missing bore

Missing peak rpm

Missing normalized losses

📌 Categorical columns → filled using mode

Example:

Missing num_doors (two or four)

This ensures the dataset becomes complete without dropping valuable rows.

🟥 6. Explored the Data with Descriptive Statistics

We used Pandas functions:

df.describe()

Summary of numeric columns (mean, std, min, max)

df.describe(include="all")

Summary of all columns
(counts, unique values, top categories, etc.)

df.info()

Datatypes

Missing values

Memory usage

This helped us understand the dataset’s shape and issues.

🟪 7. Normalization of Numerical Features

We normalized features like:

length

width

height

using the simple formula:

value / max(value)


This scales all values to 0–1, making them easier to compare.

Normalization is helpful in:

ML algorithms

Distance-based models

Visualization

🟫 8. Binning (Converting Numeric → Categories)

We converted horsepower into categories:

Low

Medium

High

Why?

Makes analysis easier

Helps understand distribution

Useful for beginner visualizations

🟩 9. Created Indicator Variables (One-Hot Encoding)

We converted categorical columns such as:

fuel_type

aspiration

drive_wheels

into numerical dummy variables.

Machine learning algorithms require numbers—not text—so this is essential.

🔵 10. Visualized Data

We created a simple histogram of price to see how car prices are distributed.

Visualization helps beginners spot:

Outliers

Skewness

Patterns

🟣 11. Exported Cleaned Dataset

Finally, we exported a fully cleaned dataset that is:

Ready for machine learning

Easy to analyze

Free of missing values

Properly typed

Well structured

📝 Practice Questions (Beginner Friendly)

These tasks help reinforce everything learned:

List all car manufacturers in the dataset.

What is the average horsepower of "gas" cars?

Find the top 5 most expensive cars.

Create a scatter plot of horsepower vs price.

Normalize curb weight.

Replace missing values in a numeric column using median.

One-hot encode "body_style".

Bin city_mpg into Low/Medium/High categories.

🎉 Summary

This project gave you hands-on practice in real-world data cleaning, including:

Importing raw data

Fixing missing values

Changing datatypes

Normalizing

Binning

Encoding

Visualizing

Exporting cleaned data

You now understand the full data-wrangling cycle—an essential skill before doing analysis or machine learning.

📎 Files in This Repository
File	Description
raw_automobile_data.csv	Original raw dataset (no headers)
cleaned_automobile_data.csv	Cleaned and processed dataset
notebook.ipynb	Step-by-step walkthrough
README.md	Project explanation (this file)
