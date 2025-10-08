import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('diabetes(2).csv')

st.title("Diabetes Data Analysis")

if st.checkbox("Show Raw Data"):
    st.write(df)

st.subheader("Age Distribution")
fig, ax = plt.subplots()
sns.histplot(df['Age'], bins=20, kde=True, ax=ax)
st.pyplot(fig)

st.subheader("Correlation Heatmap")
fig, ax = plt.subplots(figsize=(10,8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)
