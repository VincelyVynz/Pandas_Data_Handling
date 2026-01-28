import pandas as pd
import streamlit as st

customer_df = pd.read_csv("customers.csv")
orders_df = pd.read_csv("orders.csv")

customer_df.set_index("customer_id", inplace=True)
orders_df.set_index("order_id", inplace=True)

st.title("Merging Data with Pandas")

st.subheader("Customer Dataset header")
st.dataframe(customer_df.head())

st.subheader("Orders Dataset header")
st.dataframe(orders_df.head())

inner_joined_df = pd.merge(
    customer_df.reset_index(),
    orders_df.reset_index(),
    on="customer_id",
    how="inner"
)

left_joined_df = pd.merge(
    customer_df.reset_index(),
    orders_df.reset_index(),
    on="customer_id",
    how="left"
)

st.header("Merged Dataset")

st.subheader("Inner Joined Dataset")
st.dataframe(inner_joined_df)

st.subheader("Left Joined Dataset")
st.dataframe(left_joined_df)

# Missing relationships
st.header("Missing Relationships")

customers_without_orders = left_joined_df[left_joined_df["order_id"].isna()].reset_index()
st.subheader("Customers without Orders")
st.dataframe(customers_without_orders)

orders_without_customers = orders_df[~orders_df["customer_id"].isin(customer_df.index)]
st.subheader("Orders without Customers")
st.dataframe(orders_without_customers)