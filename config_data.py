import os
import API as key


md5_path = "./config/md5.txt"
md5_folder = "./config"

collection_name = "rag"
persist_directory="./chroma_db"

chunk_size=1000
chunk_overlap=100
separators=['\n\n',"\n",".","!","?","。","！"," ",""]
max_split_char_number=1000
os.environ["DASHSCOPE_API_KEY"] = key.api_key

similarity_threshold=1

embedding_model_name = "text-embedding-v4"
chat_model_name = "qwen3-max"

session_config={
    "configurable":{
        "session_id":"user_001"
    }
}
from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings
chroma = Chroma(
    collection_name=collection_name,
    embedding_function=DashScopeEmbeddings(model=embedding_model_name),
    persist_directory=persist_directory
)

submit_subtitle="提交字幕文件"
anime="动漫选择"
chat = "聊天"

subtitle = "https://github.com/Ajatt-Tools/kitsunekko-mirror"