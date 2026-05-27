import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load your dataset
df = pd.read_csv("cleaned_fraud_data.csv")

st.title("Fraud Detection Dashboard")

# ---------------- KPI ----------------
st.header("Overview")

total = len(df)
fraud = df['Fraud_Label'].sum()
normal = total - fraud

col1, col2, col3 = st.columns(3)

col1.metric("Total Transactions", total)
col2.metric("Fraud Cases", fraud)
col3.metric("Normal Cases", normal)

# ---------------- Pie Chart ----------------
st.subheader("Fraud vs Normal")

fig1, ax1 = plt.subplots()
df['Fraud_Label'].value_counts().plot.pie(
    autopct='%1.1f%%',
    labels=['Normal', 'Fraud'],
    ax=ax1
)
st.pyplot(fig1)

# ---------------- Bar Chart ----------------
st.subheader("Fraud by Location")

fraud_df = df[df['Fraud_Label'] == 1]

fig2, ax2 = plt.subplots()
fraud_df['Location'].value_counts().plot.bar(ax=ax2)
st.pyplot(fig2)
# ---------------- Line Chart ----------------
# Convert date and extract hour
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df['Hour'] = df['Date'].dt.hour

# Fraud data
fraud_df = df[df['Fraud_Label'] == 1]

# Line chart
fig3, ax3 = plt.subplots()
fraud_df['Hour'].value_counts().sort_index().plot(ax=ax3)
st.pyplot(fig3)

