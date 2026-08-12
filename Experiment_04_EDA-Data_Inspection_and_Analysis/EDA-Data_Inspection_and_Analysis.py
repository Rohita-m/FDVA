import pandas as pd

df = pd.read_csv('test_Y3wMUE5_7gLdaTN.csv')

print("--- df.head() ---")
print(df.head())

print("\n--- df.tail() ---")
print(df.tail())

print("\n--- df.info() ---")
print(df.info())

print("\n--- df.describe() ---")
print(df.describe())

print("\n--- df.columns ---")
print(df.columns)

categorical_cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']

for col in categorical_cols:
    unique_vals = df[col].unique()
    print(f"\nUnique values in '{col}': {unique_vals}")

df['Dependents'] = df['Dependents'].replace('3+', 3)
df['Dependents'] = pd.to_numeric(df['Dependents'], errors='coerce').astype('Int64')

print("\nValue counts in 'Dependents' after conversion:")
print(df['Dependents'].value_counts(dropna=False))

cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']

for col in cols:
    print(f"\nStatistics for '{col}':")
    print(f"Mean: {df[col].mean():.2f}")
    print(f"Median: {df[col].median():.2f}")
    # Mode returns a Series, so we use .values
    print(f"Mode: {df[col].mode().values}")
    print(f"Range: {df[col].max() - df[col].min():.2f}")
    print(f"Variance: {df[col].var():.2f}")
    print(f"Standard Deviation: {df[col].std():.2f}")
