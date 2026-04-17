import streamlit as st
import get_anime_store as get_anime_store
def get_title(title):
    st.session_state["anime_name"]=title
def show_card(title, value="98%", color="#4CAF50"):
    with st.container():
        st.button(title,on_click=get_title,args=(title,))

cols = st.columns(3)
items = get_anime_store.get_anime_name_and_episode()
if len(items) == 0:
    st.write("暂无字幕文件上传")
else:
    for idx, (title, value, color) in enumerate(items):
        with cols[idx % 3]:
            show_card(title, value, color)