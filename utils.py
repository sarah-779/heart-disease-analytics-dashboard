import pandas as pd

# Load dataset
def load_data(path):
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    return df


# Generate simple insights
def generate_insights(df):
    insights = []

    if df["target"].mean() > 0.4:
        insights.append("High number of patients show heart disease risk.")

    if df["chol"].mean() > 200:
        insights.append("Average cholesterol level is high.")

    
    insights.append("Exercise and lifestyle strongly impact heart health.")

    return insights
