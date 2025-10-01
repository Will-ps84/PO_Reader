import streamlit as st, requests, pandas as pd, datetime
API_URL = "http://localhost:8000/predict"

st.set_page_config(page_title="PO-Reader MVP", layout="centered")
st.title("📄 PO-Reader Demo")
uploaded = st.file_uploader("Sube PO (PDF)", type=["pdf"])
if uploaded:
    files = {"file": (uploaded.name, uploaded.getvalue(), "application/pdf")}
    res = requests.post(API_URL, files=files)
    st.json(res.json())

st.subheader("KPI últimos 7 días")
col1, col2, col3 = st.columns(3)
col1.metric("POs procesadas", 432, "+12")
col2.metric("Tiempo promedio", "18 s", "-70 %")
col3.metric("Error de captura", "0.4 %", "-2.6 pp")