# -*- coding: utf-8 -*-
"""AmazonSales.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Vge_Z8J_Wj_nd3aGGM4Xf8Mjh978iIcY
"""

import pandas as pd

# Step 1: Loading the dataset
file_path = "/content/drive/MyDrive/Amazon Sale Report.csv"
data = pd.read_csv(file_path)
#Step 2: Removing Duplicates
data = data.drop_duplicates()

# Step 3: Handle missing values
# For numeric columns, replace missing values with the column mean
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())

# For categorical columns, replace missing values with "Unknown"
categorical_columns = data.select_dtypes(include=['object']).columns
data[categorical_columns] = data[categorical_columns].fillna('Unknown')

# Step 4: Convert date columns to datetime format
if 'Order Date' in data.columns:
    data['Order Date'] = pd.to_datetime(data['Order Date'])
else:
    print("Order Date column is missing!")

# Step 5: Feature Engineering
# Creating new columns for Year and Month from Order Date
if 'Order Date' in data.columns:
    data['Year'] = data['Order Date'].dt.year
    data['Month'] = data['Order Date'].dt.month

# Creating a Profit Margin column
if {'Cost', 'Amount'}.issubset(data.columns):
    data['Profit Margin'] = data['Amount'] - data['Cost']

# Step 6: Standardizing categorical columns for consistent analysis
if 'Fulfillment Method' in data.columns:
    data['Fulfillment Method'] = data['Fulfillment Method'].str.strip().str.title()

# Step 7: Saving the cleaned dataset
cleaned_file_path = "cleaned_amazon_data.csv"
data.to_csv(cleaned_file_path, index=False)
print(f"Cleaned data saved to {cleaned_file_path}")

data