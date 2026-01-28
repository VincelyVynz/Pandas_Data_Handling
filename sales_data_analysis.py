#Analyze sales data.
# Group by: # Product # Region
# Calculate: # Total sales # Average sales # Count of transactions # Deliverable # Aggregated table # Insight summary

import pandas as pd

df = pd.read_csv("sales_data.csv")

df["Total_sales"] = df["Units_Sold"]* df["Unit_Price"]

# Grouping
# Region

regional_product_sales = df.groupby(["Region", "Product"])["Total_sales"]
print("Mean")
print(regional_product_sales.mean())
print("Total")
print(regional_product_sales.sum())
print("Total Number of Transactions")
print(regional_product_sales.size())

# Aggregation
#aggregated = df.groupby(["Region", "Product"])["Total_sales"].agg(['sum','mean','count'])

aggregated_df = df.groupby(["Region", "Product"])["Total_sales"].agg(['sum', 'mean', 'count'])
print(aggregated_df)