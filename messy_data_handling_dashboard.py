import pandas as pd
import streamlit as st

df = pd.read_csv("messy_employee_data.csv")

st.title("Messy Data Dashboard")

st.subheader("Raw Data")
st.dataframe(df)

st.subheader("Null Data")
null_values = df.isnull().sum()
st.dataframe(null_values)

st.subheader("Data types")
st.dataframe(df.dtypes)

st.subheader(" Duplicate Data")
duplicate_values = df.duplicated().sum()
st.write("Duplicate rows:", duplicate_values)

# Covert to correct data type

df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
df["hire_date"] = pd.to_datetime(df["hire_date"], errors="coerce")

# Drop nameless and employee id less rows

df = df.dropna(subset = ["employee_id", "name"])

# Fill missing numeric data

df["age"] = df["age"].fillna(df["age"].median())
df["salary"] = df["salary"].fillna(df["salary"].median())

# Add unknown to missing departments
df["department"] = df["department"].fillna("Unknown")

# Drop duplicate rows
df = df.drop_duplicates()
st.subheader("Cleaned Data")
st.dataframe(df)