# Importing required libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

# Load the dataset
df = pd.read_csv('test_Y3wMUE5_7gLdaTN.csv')

# Display basic information
print("Initial Data Overview:")
print(df.info())

# 1. Handling Missing Values
print("\nMissing Values in Each Column:\n", df.isnull().sum())
sns.heatmap(df.isnull(), cbar=False, cmap="Blues")
plt.title("Missing Value Heatmap")
# plt.show() # Disabled to allow non-interactive execution
print("Heatmap generated, but plt.show() skipped for non-interactive execution.")

for col in ['Gender', 'Married', 'Dependents', 'Self_Employed']:
    df[col] = df[col].fillna(df[col].mode()[0])

df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())
df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0])
df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].mode()[0])

# 2. Removing Duplicates
initial_rows = df.shape[0]
df.drop_duplicates(inplace=True)
print(f"\nRemoved {initial_rows - df.shape[0]} duplicate rows.")

# 3. Data Type Conversion
# Convert 'Dependents' to numeric (replace '3+' with 3)
df['Dependents'] = df['Dependents'].replace('3+', 3).fillna(0).astype(int)

# 4. Ensuring Categorical Consistency
for col in ['Gender', 'Married', 'Education', 'Self_Employed', 'Property_Area']:
    df[col] = df[col].astype(str).str.strip().str.capitalize()

# 5. Normalization
min_max_scaler = MinMaxScaler()
scale_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']
df[scale_cols] = min_max_scaler.fit_transform(df[scale_cols])

scaler = StandardScaler()
df[['Credit_History']] = scaler.fit_transform(df[['Credit_History']])

# 6. Final Overview
print("\nCleaned Data Summary:")
print(df.info())
print(df.head())
