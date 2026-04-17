from langchain_chroma import Chroma
import config_data as config
class VectorStoreService(object):
    def __init__(self,embedding):
        self.embedding = embedding
        self.vector_store= Chroma(
            collection_name=config.collection_name,
            embedding_function=self.embedding,
            persist_directory=config.persist_directory,
        )

    def get_retriever(self):
        return self.vector_store.as_retriever(
            search_kwargs={
                "k":config.similarity_threshold
            })

    def get_retriever_by_anime(self,anime_name):
        return self.vector_store.as_retriever(
            search_kwargs={
                "k": config.similarity_threshold,
                "filter": {"anime":anime_name}
            })

# if __name__ == "__main__":
#     from langchain_community.embeddings import DashScopeEmbeddings
#     retriever = VectorStoreService(DashScopeEmbeddings(model=config.embedding_model_name)).get_retriever()
#     res  = retriever.invoke("what is your major")
#     print(res)