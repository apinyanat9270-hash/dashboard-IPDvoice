st.markdown("""
<h1 style='text-align: center; color: #2c3e50;'>
📊 ประเมินความพึงพอใจผู้ป่วยใน<br>โรงพยาบาลฝาง
</h1>
""", unsafe_allow_html=True)

import streamlit as st
import pandas as pd

# โหลดข้อมูล
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS8Iq6XEm88RNQa_TSr4D5TkcMCInqLHuI013bB398uAcvltsjN8xI2cypLsr3cCPR0WBq3xBSlDgPP/pub?gid=909440641&single=true&output=csv"
df = pd.read_csv(url)

# 🎨 CSS ทำกล่อง
st.markdown("""
<style>
.kpi-card {
    background-color: #ffffff;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    text-align: center;
}
.kpi-title {
    font-size: 16px;
    color: #666;
}
.kpi-value {
    font-size: 32px;
    font-weight: bold;
    color: #4A90E2;
}
</style>
""", unsafe_allow_html=True)

# 📊 ค่า KPI
avg = df['ร้อยละความพึงพอใจ'].mean()
total = df['จำนวนทั้งหมด'].sum()

# 🧱 layout 2 กล่อง
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">ความพึงพอใจเฉลี่ย</div>
        <div class="kpi-value">{avg:.2f}%</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">จำนวนผู้ตอบ</div>
        <div class="kpi-value">{int(total)}</div>
    </div>
    """, unsafe_allow_html=True)

import plotly.express as px
# เรียงเดือน
df_sorted = df.sort_values("เดือนลำดับ")

# 📈 กราฟแนวโน้ม
st.subheader("แนวโน้มรายเดือน")

fig = px.line(
    df_sorted,
    x="เดือนแสดงผล",
    y="ร้อยละความพึงพอใจ",
    markers=True
)

st.plotly_chart(fig)

# 📊 กราฟจำนวนผู้ตอบ
st.subheader("จำนวนผู้ตอบ")

fig2 = px.bar(
    df_sorted,
    x="เดือนแสดงผล",
    y="จำนวนทั้งหมด"
)

st.plotly_chart(fig2)
