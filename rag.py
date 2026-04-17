from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory, RunnableLambda
from file_history_store import get_history
import config_data as config
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from vector_stores import VectorStoreService
from langchain_community.chat_models.tongyi import ChatTongyi

class RagService(object):
    def __init__(self,is_anime=False,anime_name=None):
        self.vector_service = VectorStoreService(
            embedding=DashScopeEmbeddings(model=config.embedding_model_name)
        )
        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system","以我提供的参考资料为主,"
                 "回答用户的问题, 参考资料{context}"),
                ("system","并且提供用户的对话历史记录如下"),
                MessagesPlaceholder("history"),
                ("human","请回答用户提问:{input}")
            ]
        )
        self.anime_name = anime_name
        self.chat_model = ChatTongyi(model=config.chat_model_name,streaming=True)
        if is_anime is True:
            self.chain=self.__get_chain(is_anime=is_anime)
        else:
            self.chain = self.__get_chain()

    def set_anime_name(self,anime_name):
        self.anime_name = anime_name

    def make_chain(self):
        self.chain = self.__get_chain(is_anime=True)

    def __get_chain(self,is_anime=False):
        if is_anime is True:
            retriever = self.vector_service.get_retriever_by_anime(anime_name=self.anime_name)
        else:
            retriever = self.vector_service.get_retriever()
        def format_document(docs:list[Document]):
            if not docs:
                return "无相关参考资料"
            formatted_str = ""
            for doc in docs:
                formatted_str += f"文档片段: {doc.page_content}\n文档元数据:{doc.metadata}\n\n"
            return formatted_str

        def debug_chain(value):
            print("=" * 20)
            print(f"内容:{value}")
            print(f"类型:{type(value)}")
            return value
        def dict_to_str(value:dict):
            return value["user_input"]
        def split_userinput_and_history(value:dict):
            new_value = {}
            new_value["input"] = value["input"]["user_input"]
            new_value["history"] = value["input"]["history"]
            new_value["context"] = value["context"]
            return new_value

        chain = (
            {
                "input":RunnablePassthrough(),
                "context":RunnableLambda(dict_to_str)|retriever | format_document
            } |RunnableLambda(split_userinput_and_history)| self.prompt_template | self.chat_model| StrOutputParser()
        )

        conversation_chain = RunnableWithMessageHistory(
            chain,
            get_history,
            input_messages_key="user_input",
            history_messages_key="history"
        )
        return conversation_chain



# if __name__ == '__main__':
#     session_config={
#         "configurable":{
#             "session_id":"user_001"
#         }
#     }
#     chain = RagService().chain
#     result = chain.stream({"user_input":"输出100个字"},session_config)
#     for chunk in result:
#         print(chunk,end="",flush=True)
#     print("模型输出")
#     print(result)
