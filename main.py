import streamlit as st
import pandas as pd

st.set_page_config(page_title="Customer Product Productivity Analysis", layout="wide")

# Load dataset
df = pd.read_csv("dataset/APL_Logistics_small.csv")

st.sidebar.title("Filters")

category = st.sidebar.selectbox(
    "Select Category",
    ["All"] + sorted(df["Category Name"].dropna().unique().tolist())
)

delivery = st.sidebar.selectbox(
    "Delivery Status",
    ["All"] + sorted(df["Delivery Status"].dropna().unique().tolist())
)

if category != "All":
    df = df[df["Category Name"] == category]

if delivery != "All":
    df = df[df["Delivery Status"] == delivery]


st.title("📊 Customer Product Productivity Analysis Dashboard")

# KPI Cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Records", len(df))
col2.metric("Total Columns", len(df.columns))
col3.metric("Total Sales", f"${df['Sales per customer'].sum():,.2f}")
col4.metric("Total Profit", f"${df['Benefit per order'].sum():,.2f}")

st.divider()

st.metric("Filtered Records", len(df))
st.divider()

st.divider()

st.subheader("Dataset Preview")
st.dataframe(df.head(20), use_container_width=True)

st.divider()

st.subheader("Sales by Delivery Status")
st.bar_chart(df["Delivery Status"].value_counts())

st.divider()

st.subheader("Top 10 Product Categories")
st.bar_chart(df["Category Name"].value_counts().head(10))


st.divider()

st.subheader("Sales by Category")
sales = df.groupby("Category Name")["Sales per customer"].sum().sort_values(ascending=False).head(10)
st.bar_chart(sales)

st.divider()

st.subheader("Profit by Category")
profit = df.groupby("Category Name")["Benefit per order"].sum().sort_values(ascending=False).head(10)
st.bar_chart(profit)

st.divider()

st.subheader("Top 10 Customers by Sales")

#features

st.divider()

st.subheader("Delivery Status Percentage")
st.write(df["Delivery Status"].value_counts())

st.divider()

st.subheader("Top 10 Customer Cities")
city = df["Customer City"].value_counts().head(10)
st.bar_chart(city)

st.subheader("Top 10 Customer States")

st.divider()

st.subheader("Sales by Payment Type")
payment = df.groupby("Type")["Sales per customer"].sum()
st.bar_chart(payment)

st.divider()

st.metric("Total Categories", df["Category Name"].nunique())

st.divider()

st.download_button(
    "Download Filtered Dataset",
    df.to_csv(index=False),
    "filtered_data.csv",
    "text/csv"
)

st.divider()

st.subheader("Dataset Information")
st.write(df.describe())

st.divider()

st.markdown("---")
st.markdown("### Customer Product Productivity Analysis Dashboard")
st.markdown("Developed by: Uppari Shivani")
st.markdown("Data Science Project")




