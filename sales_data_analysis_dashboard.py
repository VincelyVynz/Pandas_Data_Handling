import pandas as pd
import streamlit as st

df = pd.read_csv("sales_data.csv")

st.title("Sales Data Analysis")


st.subheader("Dataset Header")
st.dataframe(df.head())

df["Total_sales"] = df["Units_Sold"]* df["Unit_Price"]

st.subheader("Total_sales by region and product")
regional_product_sales = df.groupby(["Region", "Product"])["Total_sales"].sum()
st.dataframe(regional_product_sales)


aggregated_df = df.groupby(["Region", "Product"])["Total_sales"].agg(Total_sales = 'sum',
                                                                     Average_Sales = 'mean',
                                                                     Transaction_count = 'count')

st.subheader("Aggregated Data")
st.dataframe(aggregated_df)