import pandas as pd

# Data Import from CSV
print("--- Importing from CSV ---")
df_csv = pd.read_csv("test_Y3wMUE5_7gLdaTN.csv")
print(df_csv.head())

# Data Import from Excel
print("\n--- Importing from Excel ---")
df_excel = pd.read_excel("Historicalinvesttemp.xlsx", sheet_name="Sheet1")
print(df_excel.head())

# Data Import from Web
print("\n--- Importing from Web Scraping ---")
url = "https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
try:
    tables = pd.read_html(url)
    df_web = tables[0]
    print(df_web.head())
except Exception as e:
    print("Could not scrape web data:", e)

# Data Export
print("\n--- Exporting to Excel ---")
df = pd.read_excel("Historicalinvesttemp.xlsx")
df.to_excel("weeeeee.xlsx", index=False)
print(df.head())
print("\nExported successfully to weeeeee.xlsx")
