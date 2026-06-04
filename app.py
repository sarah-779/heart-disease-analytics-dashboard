import pandas as pd
import streamlit as st

# Load your data
df = pd.read_csv("heart.csv")

# Clean column names (VERY IMPORTANT)
df.columns = df.columns.str.strip().str.lower()

# Ensure age is numeric
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df = df.dropna(subset=["age"])

# Get safe min/max values
min_age = int(df["age"].min())
max_age = int(df["age"].max())

# Streamlit slider (CORRECT)
age_range = st.sidebar.slider(
    "Select Age Range",
    min_age,
    max_age,
    (min_age, max_age)
)

# Filter data
filtered_df = df[(df["age"] >= age_range[0]) & (df["age"] <= age_range[1])]

st.write(filtered_df)
