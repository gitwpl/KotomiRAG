import config_data as config
db = config.chroma

# 2. 获取所有文档（不限制数量）
all_docs = db.get()  # 会返回 ids, embeddings, metadatas, documents 四个字段
print(all_docs)
# 3. 提取所有 anime_name（自动处理不存在的字段）
anime_names = []
for meta in all_docs["metadatas"]:
    if "anime" in meta:
        anime_names.append(meta["anime"])
unique_anime_names = sorted(list(set(anime_names)))
print("所有动漫名称：")
for name in unique_anime_names:
    print(name)