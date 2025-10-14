import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    df = pd.read_csv("diabetes(2).csv")
    return df

df = load_data()

st.set_page_config(page_title="Diabetes Data Dashboard", layout="wide")
st.title("📊 Interactive Diabetes Data Dashboard")
st.markdown("Use the filters in the sidebar to explore the dataset interactively.")

st.sidebar.header("🔍 Filter Data")

bmi_range = st.sidebar.slider(
    "Select BMI Range:",
    float(df["BMI"].min()),
    float(df["BMI"].max()),
    (float(df["BMI"].min()), float(df["BMI"].max()))
)

glucose_range = st.sidebar.slider(
    "Select Glucose Range:",
    float(df["Glucose"].min()),
    float(df["Glucose"].max()),
    (float(df["Glucose"].min()), float(df["Glucose"].max()))
)

age_range = st.sidebar.slider(
    "Select Age Range:",
    int(df["Age"].min()),
    int(df["Age"].max()),
    (int(df["Age"].min()), int(df["Age"].max()))
)

filtered_df = df[
    (df["BMI"] >= bmi_range[0]) & (df["BMI"] <= bmi_range[1]) &
    (df["Glucose"] >= glucose_range[0]) & (df["Glucose"] <= glucose_range[1]) &
    (df["Age"] >= age_range[0]) & (df["Age"] <= age_range[1])
]

st.subheader("📄 Filtered Dataset")
st.write(f"Showing {filtered_df.shape[0]} records after filtering.")
st.dataframe(filtered_df)


col1, col2 = st.columns(2)

with col1:
    st.subheader("📌 Age Distribution")
    fig, ax = plt.subplots()
    sns.histplot(filtered_df["Age"], bins=20, kde=True, ax=ax, color="skyblue")
    st.pyplot(fig)

with col2:
    st.subheader("📌 Glucose Distribution")
    fig, ax = plt.subplots()
    sns.histplot(filtered_df["Glucose"], bins=20, kde=True, ax=ax, color="orange")
    st.pyplot(fig)

st.subheader("📌 Correlation Heatmap")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(filtered_df.corr(), annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)


col1, col2 = st.columns(2)

with col1:
    st.subheader("⚠️ Misleading Visualization")
    fig, ax = plt.subplots(figsize=(4.5, 3))
    sns.barplot(x='Outcome', y='Age', data=df, ax=ax, palette='cool')
    ax.set_ylim(25, 35)
    ax.set_title('Misleading Age vs Outcome\n(Truncated Y-Axis)', fontsize=10)
    st.pyplot(fig)

with col2:
    st.subheader("✅ Correct Visualization")
    fig, ax = plt.subplots(figsize=(4.5, 3))
    sns.barplot(x='Outcome', y='Age', data=df, ax=ax, palette='crest')
    ax.set_title('Age vs Outcome (Full Scale)', fontsize=10)
    st.pyplot(fig)


st.subheader("📊 Box Plot for Glucose & Outcome Analysis")
fig, ax = plt.subplots(figsize=(6, 3))
sns.boxplot(x='Outcome', y='Glucose', data=df, ax=ax)
ax.set_title('Glucose Levels by Diabetes Outcome')
st.pyplot(fig)


st.subheader("📊 Scatter Plot for Age & BMI Comparison")
fig, ax = plt.subplots(figsize=(6, 3))
sns.scatterplot(x='Age', y='BMI', hue='Outcome', data=df, ax=ax)
ax.set_title('BMI vs Age with Diabetes Outcome')
st.pyplot(fig)

st.markdown("---")
st.markdown("✅ **Developed for Data Visualisation Assignment** | Powered by Streamlit")
