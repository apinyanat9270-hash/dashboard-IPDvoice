import streamlit as st
import pandas as pd

# โหลดข้อมูล
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vS8Iq6XEm88RNQa_TSr4D5TkcMCInqLHuI013bB398uAcvltsjN8xI2cypLsr3cCPR0WBq3xBSlDgPP/pub?gid=909440641&single=true&output=csv"
df = pd.read_csv(url)

# หัวข้อ
st.markdown("""
<h1 style='text-align: center; color: #1f4e79; text-shadow: 1px 1px 2px #ccc;'>
📊 ผลการประเมินความพึงพอใจผู้ป่วยใน ปีงบประมาณ 2569<br>โรงพยาบาลฝาง
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
    font-size: 28px;
    animation: floatUp 4s linear forwards;
    pointer-events: none;
}

@keyframes floatUp {
    0%   { transform: translateY(0); opacity: 1; }
    100% { transform: translateY(-800px); opacity: 0; }
}
</style>

<!-- แถวที่ 1 -->
<div class="emoji-float" style="left:5%;  bottom:0%;  animation-delay:0s;">😊</div>
<div class="emoji-float" style="left:25%; bottom:0%;  animation-delay:0.3s;">😄</div>
<div class="emoji-float" style="left:45%; bottom:0%;  animation-delay:0.6s;">😁</div>
<div class="emoji-float" style="left:65%; bottom:0%;  animation-delay:0.9s;">🥰</div>
<div class="emoji-float" style="left:85%; bottom:0%;  animation-delay:1.2s;">😍</div>

<!-- แถวที่ 2 -->
<div class="emoji-float" style="left:10%; bottom:10%; animation-delay:0.2s;">😊</div>
<div class="emoji-float" style="left:30%; bottom:10%; animation-delay:0.5s;">😆</div>
<div class="emoji-float" style="left:50%; bottom:10%; animation-delay:0.8s;">😁</div>
<div class="emoji-float" style="left:70%; bottom:10%; animation-delay:1.1s;">🥰</div>
<div class="emoji-float" style="left:90%; bottom:10%; animation-delay:1.4s;">😍</div>

<!-- แถวที่ 3 -->
<div class="emoji-float" style="left:5%;  bottom:20%; animation-delay:0.4s;">😊</div>
<div class="emoji-float" style="left:25%; bottom:20%; animation-delay:0.7s;">😄</div>
<div class="emoji-float" style="left:45%; bottom:20%; animation-delay:1.0s;">😁</div>
<div class="emoji-float" style="left:65%; bottom:20%; animation-delay:1.3s;">🥰</div>
<div class="emoji-float" style="left:85%; bottom:20%; animation-delay:1.6s;">😍</div>

<!-- แถวที่ 4 -->
<div class="emoji-float" style="left:10%; bottom:30%; animation-delay:0.6s;">😊</div>
<div class="emoji-float" style="left:30%; bottom:30%; animation-delay:0.9s;">😆</div>
<div class="emoji-float" style="left:50%; bottom:30%; animation-delay:1.2s;">😁</div>
<div class="emoji-float" style="left:70%; bottom:30%; animation-delay:1.5s;">🥰</div>
<div class="emoji-float" style="left:90%; bottom:30%; animation-delay:1.8s;">😍</div>

<!-- แถวที่ 5 -->
<div class="emoji-float" style="left:5%;  bottom:40%; animation-delay:0.8s;">😊</div>
<div class="emoji-float" style="left:25%; bottom:40%; animation-delay:1.1s;">😄</div>
<div class="emoji-float" style="left:45%; bottom:40%; animation-delay:1.4s;">😁</div>
<div class="emoji-float" style="left:65%; bottom:40%; animation-delay:1.7s;">🥰</div>
<div class="emoji-float" style="left:85%; bottom:40%; animation-delay:2.0s;">😍</div>
""", unsafe_allow_html=True)
