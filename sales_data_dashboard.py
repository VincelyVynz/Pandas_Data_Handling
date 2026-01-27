import streamlit as st
import pandas as pd

df = pd.read_csv("sales_data.csv")
df["Total_Sales"] = df["Units_Sold"] * df["Unit_Price"]

st.title("📊 Sales Dashboard")

st.subheader("Raw Data")
st.dataframe(df)

st.subheader("High Value Sales (> 100k)")
st.dataframe(df[df["Total_Sales"] > 100000])

st.subheader("Total Sales by Product")
st.bar_chart(
    df.groupby("Product")["Total_Sales"].sum()
)

st.subheader("Units Sold by Region")
st.bar_chart(
    df.groupby("Region")["Units_Sold"].sum()
)
