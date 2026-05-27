import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------- LOAD DATA ----------------
df = pd.read_csv("cleaned_fraud_data.csv")

st.title("💳 Financial Fraud Detection Dashboard")

# ---------------- KPI SECTION ----------------
st.header("📊 Overview")

total = len(df)
fraud = df['Fraud_Label'].sum()
normal = total - fraud

col1, col2, col3 = st.columns(3)

col1.metric("Total Transactions", total)
col2.metric("Fraud Cases", fraud)
col3.metric("Normal Cases", normal)

# ---------------- PIE CHART ----------------
st.subheader("Fraud vs Normal Distribution")

fig1, ax1 = plt.subplots()
df['Fraud_Label'].value_counts().plot.pie(
    autopct='%1.1f%%',
    labels=['Normal', 'Fraud'],
    ax=ax1
)
ax1.set_ylabel("")
st.pyplot(fig1)

# ---------------- FILTER FRAUD DATA ----------------
fraud_df = df[df['Fraud_Label'] == 1]

# ---------------- FRAUD BY LOCATION ----------------
st.subheader("Fraud by Location")

fig2, ax2 = plt.subplots()
fraud_df['Location'].value_counts().plot.bar(ax=ax2)
ax2.set_xlabel("Location")
ax2.set_ylabel("Fraud Count")
st.pyplot(fig2)

# ---------------- FRAUD BY TRANSACTION TYPE ----------------
st.subheader("Fraud by Transaction Type")

fig3, ax3 = plt.subplots()
fraud_df['Transaction_Type'].value_counts().plot.bar(ax=ax3)
ax3.set_xlabel("Transaction Type")
ax3.set_ylabel("Fraud Count")
st.pyplot(fig3)

# ---------------- FRAUD BY DEVICE TYPE ----------------
st.subheader("Fraud by Device Type")

fig4, ax4 = plt.subplots()
fraud_df['Device_Type'].value_counts().plot.bar(ax=ax4)
ax4.set_xlabel("Device Type")
ax4.set_ylabel("Fraud Count")
st.pyplot(fig4)

# ---------------- FOOTER ----------------
st.markdown("---")
st.write("✔ Model: Random Forest with SMOTE and Threshold Tuning (0.4)")

