import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px

st.set_page_config(
    page_title="Retail Sales Dashboard",
    page_icon= "💹",
    layout="wide"
)

df = pd.read_csv("retail_sales_data.csv")
raw_data = df.copy().set_index("Order_ID")

st.header("Retail Sales Data Analysis")
st.subheader("Sales Data Info")
st.write("Sales Data Header:")
st.dataframe(df.head())

st.write(f"Data frame shape: {df.shape}")

st.subheader("Data Validation")
st.write(f"Missing data info :")
st.dataframe(df.isnull().sum())

st.write("Datatype :")
st.dataframe(df.dtypes)

df["Revenue"] = df["Units_Sold"] * df["Unit_Price"]
df["Total_Cost"] = df["Units_Sold"] + df["Unit_Cost"]
df["Profit"]  = df["Revenue"] - df["Total_Cost"]

low_profit_threshold = df["Profit"].quantile(0.33)
high_profit_threshold = df["Profit"].quantile(0.66)

def profit_category(n):
    if n < low_profit_threshold:
        return "Low"
    elif n < high_profit_threshold:
        return "Medium"
    else:
        return "High"

df["Profit_Category"] = df["Profit"].apply(profit_category)

df["City_Code"] = df["City"].astype("category").cat.codes
df["Product_Code"] = df["Product"].astype("category").cat.codes
df["Product_Category_Code"] = df["Product_Category"].astype("category").cat.codes
df["Profit_Code"] = df["Profit"].astype("category").cat.codes

df["Units_Sold_Norm"] = (df["Units_Sold"] - df["Units_Sold"].min()) / (df["Units_Sold"].max() - df["Units_Sold"].min())
df["Unit_Price_Norm"] = (df["Unit_Price"] - df["Unit_Price"].min()) / (df["Unit_Price"].max() - df["Unit_Price"].min())
df["Unit_Cost_Norm"]  = (df["Unit_Cost"]  - df["Unit_Cost"].min())  / (df["Unit_Cost"].max()  - df["Unit_Cost"].min())
df["Revenue_Norm"]    = (df["Revenue"] - df["Revenue"].min())/ (df["Revenue"].max() - df["Revenue"].min())
df["Profit_Norm"]     = (df["Profit"] - df["Profit"].min())/ (df["Profit"].max() - df["Profit"].min())

st.subheader("Enhanced Data")
color_map = {
    "Low": "#1b4332",
    "Medium": "#2d6a4f",
    "High": "#40916c"
}

st.dataframe(
    df.style.applymap(
        lambda x: f'background-color: {color_map[x]}; color: white;' if x in color_map else '',
        subset=["Profit_Category"]
    )
)


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

# Graphs
profit_by_product_category = df.groupby("Product_Category")["Profit"].sum()
profit_by_city = df.groupby("City")["Profit"].sum()
revenue_by_product_category = df.groupby("Product_Category")["Revenue"].sum()
revenue_by_city = df.groupby("City")["Revenue"].sum()
products_sell_count = df.groupby("Product")["Units_Sold"].sum()
units_sold_by_city = df.groupby("City")["Units_Sold"].sum()

unit_price_vs_unit_cost = alt.Chart(df).mark_circle(size=60).encode(
    x = alt.X("Unit_Cost", title = 'Unit Cost ($)'),
    y = alt.Y("Unit_Price", title = 'Unit Price ($)'),
    color = 'Product_Category',
    tooltip = ['Product', 'Unit_Price', 'Unit_Cost', 'Revenue', 'Profit']
).interactive()

unit_price_vs_units_sold_vs_profit = px.scatter_3d(
    df,
    x = 'Unit_Price',
    y = 'Units_Sold',
    z = 'Profit',
    color = 'Product_Category',
    size = 'Revenue',
    hover_data=['Unit_Price', 'Unit_Cost', 'Revenue', 'Profit', 'City', 'Product']
)
unit_price_vs_units_sold_vs_profit.update_layout(template = 'plotly_dark')


st.header("Profit and Revenue")

st.subheader("Profit by Product Category")
st.bar_chart(profit_by_product_category)
st.subheader("Revenue by Product Category")
st.bar_chart(revenue_by_product_category)

st.subheader("Profit by City")
st.bar_chart(profit_by_city)
st.subheader("Revenue by City")
st.bar_chart(revenue_by_city)

st.subheader("Units sold per Product")
st.bar_chart(products_sell_count)

st.subheader("Units sold per City")
st.bar_chart(units_sold_by_city)

st.subheader("Unit_Price vs Unit_Cost per Product")
st.altair_chart(unit_price_vs_unit_cost, use_container_width=True)

st.subheader("Unit_Price vs Units sold vs Profit")
st.plotly_chart(unit_price_vs_units_sold_vs_profit, use_container_width=True)

# Raw Dataset
st.header("Raw Dataset")
st.dataframe(raw_data)