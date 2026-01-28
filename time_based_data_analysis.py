import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Convert column to datetime # Create a date range  # Resample data: Daily → Monthly
# Plot trend using Matplotlib  Line chart
# Resampled DataFrame

df = pd.read_csv("daily_revenue_data.csv")
df["date"] = pd.to_datetime(df["date"], format= "%Y-%m-%d")
df = df.set_index("date")

st.title("Time Based Data Analysis")
st.subheader("Dataframe Header")
st.dataframe(df.head())

monthly_df = df.resample("ME").sum()

st.subheader("Monthly Revenue")
st.dataframe(monthly_df)

# Plotting in graph

fig, ax = plt.subplots(figsize = (10,10))

ax.plot(monthly_df.index, monthly_df["revenue"], marker = "o", label = "Revenue", color = "black", markerfacecolor = "white")

ax.set_xlabel("Month",  fontsize = 18, fontweight = "bold", fontname = "serif", family = "serif")
ax.set_ylabel("Revenue",  fontsize = 18, fontweight = "bold", fontname = "serif", family = "serif")
ax.set_title("Monthly Revenue",  fontsize = 24, fontweight = "bold", fontname = "serif", family = "serif")

ax.set_xticks(monthly_df.index)
ax.set_xticklabels(monthly_df.index.strftime("%b %Y"), rotation=45)


st.subheader("Monthly Revenue Line Chart")
st.pyplot(fig)














