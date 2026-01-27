import streamlit as st
import pandas as pd
from io import StringIO

df = pd.read_csv("sales_data.csv")
df["Total_Sales"] = df["Units_Sold"] * df["Unit_Price"]

st.title("📊 Sales Dashboard")

st.subheader("Data Header")
st.dataframe(df.head())

st.subheader("Dataset Info")
buffer = StringIO()
df.info(buf=buffer)
s = buffer.getvalue()
st.text(s)

st.subheader("Raw Data")
st.dataframe(df)

st.subheader("High Value Sales (> 100k)")
st.dataframe(df[df["Total_Sales"] > 100_000])

st.subheader("Total Sales by Product")
st.bar_chart(
    df.groupby("Product")["Total_Sales"].sum()
)

st.subheader("Units Sold by Region")
st.bar_chart(
    df.groupby("Region")["Units_Sold"].sum()
)
