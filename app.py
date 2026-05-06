import streamlit as st
import pandas as pd

# 🔗 ใส่ลิงก์ Google Sheets (CSV)
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS8Iq6XEm88RNQa_TSr4D5TkcMCInqLHuI013bB398uAcvltsjN8xI2cypLsr3cCPR0WBq3xBSlDgPP/pub?gid=909440641&single=true&output=csv"
df = pd.read_csv(url)

st.title("📊 ความพึงพอใจผู้ป่วยใน โรงพยาบาลฝาง")

# KPI
col1, col2 = st.columns(2)

col1.metric("ความพึงพอใจเฉลี่ย", f"{df['ร้อยละความพึงพอใจ'].mean():.2f}%")
col2.metric("จำนวนผู้ตอบ", int(df['จำนวนทั้งหมด'].sum()))

# กราฟ
st.subheader("แนวโน้มรายเดือน")
st.line_chart(df.set_index("เดือนแสดงผล")["ร้อยละความพึงพอใจ"])

st.subheader("จำนวนผู้ตอบ")
st.bar_chart(df.set_index("เดือนแสดงผล")["จำนวนทั้งหมด"])
