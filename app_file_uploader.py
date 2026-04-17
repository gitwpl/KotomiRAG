import time
import streamlit as st
from knowledge_base import KnowledgeBaseService
import config_data as config
st.title(config.submit_subtitle)
uploader_file = st.file_uploader(
    f"请上传字幕文件",
    type=["txt"],
    accept_multiple_files=False,
)
if "service" not in st.session_state:
    st.session_state["service"] = KnowledgeBaseService()
if uploader_file is not None:
    file_name = uploader_file.name
    text:str = uploader_file.getvalue().decode("utf-8")
    anime_name = st.text_input("请输入动漫名称: ", file_name)
    if st.button("提交字幕以及动漫名称"):
    # st.write(text)
        with st.spinner("载入知识库中..."):
            time.sleep(1)
            result = st.session_state["service"].upload_by_str(text,file_name,anime_name)
            st.write(result)
st.subheader(f"字幕网站推荐{config.subtitle}")