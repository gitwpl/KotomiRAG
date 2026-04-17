import streamlit as st
st.set_page_config(page_title="KotomiRAG", layout="wide")

# 添加 Logo 到导航栏
st.logo(
    "logo.png",  # 支持本地路径或 URL
    link="https://github.com/gitwpl/KotomiRAG",  # 点击跳转链接（可选）
    icon_image="logo.png"  # 导航栏折叠时显示的小图标（可选）
)

page1 = st.Page("app_qa.py", title="页面1")
page2 = st.Page("app_file_uploader.py", title="页面2")

pg = st.navigation([page1, page2])
pg.run()