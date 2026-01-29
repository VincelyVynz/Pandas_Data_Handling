import pandas as pd
import streamlit as st

# TODO 1: Load the dataset into a DataFrame and inspect basic structure
#         (check shape, column names, data types, and missing values)

df = pd.read_csv("retail_sales_data.csv")
raw_data = df.copy()

st.header("Retail Sales Data Analysis")
st.subheader("Sales Data Info")
st.write("Sales Data Header:")
st.dataframe(df.head())

st.write(f"Data frame shape: {df.shape}")

# TODO 2: Validate data quality

st.subheader("Data Validation")
st.write(f"Number of rows with missing data:")
st.dataframe(df.isnull().sum())

st.write("Datatype: ")
st.dataframe(df.dtypes)

# TODO 3: Create a Revenue column   (Revenue = Units_Sold * Unit_Price)

df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]


# TODO 4: Create a Total_Cost column
#         (Total_Cost = Units_Sold * Unit_Cost)

df["Total_Cost"] = df["Units_Sold"] + df["Unit_Cost"]

# TODO 5: Calculate Profit per order
#         (Profit = Revenue - Total_Cost)

df["Profit"]  = df["Revenue"] - df["Total_Cost"]

# TODO 6: Define profit category thresholds
#         (e.g., Low, Medium, High based on profit distribution or business rules)

low_profit_threshold = df["Profit"].quantile(0.33)
high_profit_threshold = df["Profit"].quantile(0.66)

def profit_category(n):
    if n < low_profit_threshold:
        return "Low"
    elif n < high_profit_threshold:
        return "Medium"
    else:
        return "High"


# TODO 7: Create a Profit_Category column using the defined thresholds

df["Profit_Category"] = df["Profit"].apply(profit_category)

# TODO 8: Identify categorical columns (City, Product, Product_Category, Profit_Category)

df["City_Code"] = df["City"].astype("category").cat.codes
df["Product_Code"] = df["Product"].astype("category").cat.codes
df["Product_Category_Code"] = df["Product_Category"].astype("category").cat.codes
df["Profit_Code"] = df["Profit"].astype("category").cat.codes

# TODO 9: Encode categorical features into numeric form (choose appropriate encoding strategy per column)

# TODO 10: Identify numeric columns to normalize (Units_Sold, Unit_Price, Unit_Cost, Revenue, Profit)

df["Units_Sold_Norm"] = (df["Units_Sold"] - df["Units_Sold"].min()) / (df["Units_Sold"].max() - df["Units_Sold"].min())
df["Unit_Price_Norm"] = (df["Unit_Price"] - df["Unit_Price"].min()) / (df["Unit_Price"].max() - df["Unit_Price"].min())
df["Unit_Cost_Norm"]  = (df["Unit_Cost"]  - df["Unit_Cost"].min())  / (df["Unit_Cost"].max()  - df["Unit_Cost"].min())
df["Revenue_Norm"]    = (df["Revenue"] - df["Revenue"].min())/ (df["Revenue"].max() - df["Revenue"].min())
df["Profit_Norm"]     = (df["Profit"] - df["Profit"].min())/ (df["Profit"].max() - df["Profit"].min())

# TODO 11: Normalize selected numeric columns    (ensure comparable scale across features)

# TODO 12: Review the enhanced DataFrame
#          (verify new columns, encodings, and normalized values)
st.subheader("Enhanced Data")
st.dataframe(df)
# TODO 13: Prepare feature explanations
#          (describe each engineered and transformed feature in plain language)

st.subheader("Feature Explanation")

st.markdown("""
- **Revenue** : Units_Sold x Unit_Price
- **Profit**  : Revenue - Total_Cost
- **Profit_Category** : Low/ Medium/ High (based on profit percentiles)
- **City_Code** : Numeric encoding of City
- **Product_Code** : Numeric encoding of Product
- **Product_Category_Code** : Numeric encoding of Product_Category
- **Normalized columns** : Units_Sold, Unit_Price, Unit_Cost, Revenue, Profit [ Min-max normalized (0 - 1)]
""")

# TODO 14: Save or export the enhanced DataFrame if needed
#          (CSV or other format for downstream use)


st.subheader("Raw Dataset")
st.dataframe(raw_data)