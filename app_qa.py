import streamlit as st
from rag import RagService
import config_data as config

anime_name = st.session_state["anime_name"]
st.title(f"动漫名称: {anime_name}")
st.divider()
if "message" not in st.session_state:
    st.session_state["message"] = [{"role":"assistant","content":"hello"}]
if "rag_service" not in st.session_state:
    st.session_state["rag_service"] = RagService(True)
st.session_state["rag_service"].set_anime_name(anime_name)
for message in st.session_state["message"]:
    st.chat_message(message["role"]).write(message["content"])
user_input = st.chat_input()
if user_input:
    st.chat_message("user").write(user_input)
    st.session_state["message"].append({"role":"user","content":user_input})
    with st.spinner("AI thinking..."):
        st.session_state["rag_service"].make_chain()
        chain = st.session_state["rag_service"].chain
        # chain = st.session_state["rag_service"].chain
        res_stream = chain.stream({"user_input":user_input},config.session_config)
        full_response = st.chat_message("assistant").write_stream(res_stream)
        st.session_state["message"].append({"role":"assistant","content":full_response})
