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

st.subheader("📊 Misleading Diabetes Outcome Analysis")
plt.figure(figsize=(6,4))
sns.barplot(x='Outcome', y='Age', data=df)
plt.ylim(25, 35)
plt.title('Misleading Age vs Outcome')
plt.show()

st.subheader("📊 Diabetes Outcome Analysis")
fig, ax = plt.subplots(figsize=(6, 6))
sns.countplot(x="Outcome", data=filtered_df, palette="viridis", ax=ax)
st.pyplot(fig)

st.subheader("📊 Box Plot for Glucose & Outcome Analysis")
plt.figure(figsize=(8,5))
sns.boxplot(x='Outcome', y='Glucose', data=df)
plt.title('Glucose Levels by Diabetes Outcome')
plt.show()


st.subheader("📊 Scatter Plot for Age & BMI Comparision")
plt.figure(figsize=(8,5))
sns.scatterplot(x='Age', y='BMI', hue='Outcome', data=df)
plt.title('BMI vs Age with Diabetes Outcome')
plt.show()

st.markdown("---")
st.markdown("✅ **Developed for Data Visualisation Assignment** | Powered by Streamlit")
