import streamlit as st

st.markdown("""
<style>
    .metric-card {
        background-color: #ffffff;
        border-left: 5px solid #4CAF50;
        border-radius: 8px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 2px 10px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
    }
    .metric-card:hover {
        box-shadow: 0 4px 20px rgba(0,0,0,0.12);
        border-left-width: 8px;
    }
    .metric-title {
        color: #666;
        font-size: 14px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .metric-value {
        color: #333;
        font-size: 28px;
        font-weight: 700;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

def card(title, value="98%", color="#4CAF50"):
    with st.container():
        st.markdown(f'''
            <div class="metric-card" style="border-left-color: {color};">
                <div class="metric-title">{title}</div>
                <div class="metric-value">{value}</div>
            </div>
        ''', unsafe_allow_html=True)
        cols_inner = st.columns([1, 1])

cols = st.columns(3)
items = [
    ("销售额", "¥128K", "#4CAF50"),
    ("用户数", "1,234", "#2196F3"),
    ("完成率", "89%", "#FF9800"),
    ("新项目", "12", "#9C27B0")
]

for idx, (title, value, color) in enumerate(items):
    with cols[idx % 3]:
        card(title, value, color)