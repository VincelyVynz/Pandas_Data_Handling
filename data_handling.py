import pandas as pd

df = pd.read_csv('sales_data.csv')

first_five_rows = df.head()

dataset_info = df.info()

print(dataset_info)

# Create Total sales column
df["Total_Sales"] = df["Units_Sold"] * df["Unit_Price"]

# Filtering sales over 100000

high_sales = df[df["Total_Sales"] > 100_000].reset_index(drop=True)


# Grouping

product_sales  =  df.groupby("Product")["Total_Sales"].sum().reset_index()
regional_sales =  df.groupby("Region")["Total_Sales"].sum().reset_index()