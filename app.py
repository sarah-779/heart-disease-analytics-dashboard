import streamlit as st
import pandas as pd
import plotly.express as px
from utils import load_data, generate_insights

# Page config
st.set_page_config(page_title="Heart Disease Dashboard", layout="wide")

# Load data
df = load_data("heart.csv")

st.title("❤️ Heart Disease Analytics Dashboard")
st.markdown("Interactive data analysis and insights for heart health dataset")

# Sidebar filters
st.sidebar.header("Filters")

min_age = int(df["age"].min())
max_age = int(df["age"].max())

age_range = st.sidebar.slider(
    "Select Age Range",
    min_age,
    max_age,
    (min_age, max_age)
)

# Filter dataset
filtered_df = df[
    (df["age"] >= age_range[0]) &
    (df["age"] <= age_range[1])
]

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Overview", "📈 Visuals", "🧠 Insights"])

# ---------------- OVERVIEW ----------------
with tab1:
    st.subheader("Dataset Overview")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Records", len(filtered_df))
    col2.metric("Average Age", round(filtered_df["age"].mean(), 2))
    col3.metric("Heart Disease Cases", int(filtered_df["target"].sum()))

    st.dataframe(filtered_df.head())

# ---------------- VISUALS ----------------
with tab2:
    st.subheader("Data Visualizations")

    fig1 = px.histogram(
        filtered_df,
        x="age",
        color="target",
        title="Age Distribution vs Heart Disease"
    )
    st.plotly_chart(fig1, use_container_width=True)

    fig2 = px.box(
        filtered_df,
        x="target",
        y="chol",
        title="Cholesterol vs Heart Disease"
    )
    st.plotly_chart(fig2, use_container_width=True)

    fig3 = px.scatter(
        filtered_df,
        x="age",
        y="chol",
        color="target",
        title="Age vs Cholesterol"
    )
    st.plotly_chart(fig3, use_container_width=True)

# ---------------- INSIGHTS ----------------
with tab3:
    st.subheader("AI Insights")

    insights = generate_insights(filtered_df)

    for i in insights:
        st.success(i)

    st.warning("This dashboard is for educational purposes only.")
