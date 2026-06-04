import pandas as pd

# Load dataset safely
def load_data(path):
    df = pd.read_csv(path)

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    # Convert important columns to numeric
    for col in ["age", "chol", "target"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Drop missing values
    df = df.dropna(subset=["age", "chol", "target"])

    return df


# Generate insights
def generate_insights(df):
    insights = []

    if df["target"].mean() > 0.4:
        insights.append("High number of patients show heart disease risk.")

    if df["chol"].mean() > 200:
        insights.append("Average cholesterol level is high.")

    if df[df["target"] == 1]["age"].mean() > 55:
        insights.append("Older age group is more affected by heart disease.")

    insights.append("Exercise, diet, and lifestyle strongly impact heart health.")

    return insights
