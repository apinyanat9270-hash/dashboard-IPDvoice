import streamlit as st
import pandas as pd

# โหลดข้อมูล
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS8Iq6XEm88RNQa_TSr4D5TkcMCInqLHuI013bB398uAcvltsjN8xI2cypLsr3cCPR0WBq3xBSlDgPP/pub?gid=909440641&single=true&output=csv"
df = pd.read_csv(url)

# หัวข้อ
st.markdown("""
<h1 style='text-align: center; color: #1f4e79; text-shadow: 1px 1px 2px #ccc;'>
📊 ประเมินความพึงพอใจผู้ป่วยใน<br>โรงพยาบาลฝาง
</h1>
""", unsafe_allow_html=True)

# 🎨 CSS ทำกล่อง
st.markdown("""
<style>
.kpi-card {
    background: linear-gradient(135deg, #e3f2fd, #ffffff);
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 6px 15px rgba(0,0,0,0.08);
    text-align: center;

    height: 140px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.kpi-title {
    font-size: 16px;
    color: #6c757d;
    margin-bottom: 5px;
}

.kpi-value {
    font-size: 36px;   /* 🔥 ทำให้ใหญ่ขึ้น */
    font-weight: bold;
    color: #1f4e79;
}

.kpi-unit {
    font-size: 14px;
    color: #6c757d;
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
        <div class="kpi-value">{int(total):,}</div>
        <div style="font-size:13px; color:#6c757d;">คน</div>
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
import plotly.express as px

# 🔽 เรียงเดือนก่อน
df_sorted = df.sort_values("เดือนลำดับ")

# 📊 กราฟจำนวนผู้ตอบ (เรียงเดือนชัวร์)
st.subheader("จำนวนผู้ตอบรายเดือน")

fig = px.bar(
    df_sorted,
    x="เดือนแสดงผล",
    y="จำนวนทั้งหมด",
    text="จำนวนทั้งหมด",
    color_discrete_sequence=["#4A90E2"]
)

fig.update_layout(
    plot_bgcolor="#ffffff",
    paper_bgcolor="#f5f7fb",
    font=dict(size=14),
    xaxis_title="เดือน",
    yaxis_title="จำนวนผู้ตอบ"
)

fig.update_traces(textposition="outside")

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
<style>
.emoji-float {
    position: fixed;
    bottom: 0;
    font-size: 30px;
    animation: floatUp 3s ease-out forwards;
}

@keyframes floatUp {
    0% {
        transform: translateY(0);
        opacity: 1;
    }
    100% {
        transform: translateY(-600px);
        opacity: 0;
    }
}
</style>

<div class="emoji-float">😊</div>
<div class="emoji-float" style="left:20%;">😄</div>
<div class="emoji-float" style="left:40%;">😁</div>
<div class="emoji-float" style="left:60%;">🥰</div>
<div class="emoji-float" style="left:80%;">😍</div>
""", unsafe_allow_html=True)
