import config_data as config
from collections import defaultdict
def get_anime_name_and_episode():
    db = config.chroma
    # 2. 获取所有文档（不限制数量）
    all_docs = db.get()
    metadatas = all_docs["metadatas"]

    # 3. 构建去重后的 anime -> sources 映射
    anime_source_map = defaultdict(set)  # set 自动给 source 去重

    for meta in metadatas:
        # 安全获取字段
        anime = meta.get("anime")
        source = meta.get("source")

        # 过滤空值
        if anime and source:
            anime_source_map[anime].add(source)


    colors = ["#4CAF50", "#2196F3", "#FF9800", "#9C27B0", "#FF5722", "#607D8B", "#3F51B5"]

    result_tuples = []
    for idx, (anime, sources) in enumerate(anime_source_map.items()):
        count = str(len(sources))  # 数量转字符串
        color = colors[idx % len(colors)]
        result_tuples.append((anime, count, color))

    # 返回元组列表
    return result_tuples


# get_anime_name_and_episode()