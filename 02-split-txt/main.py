import re
import json


# 读取文本数据
with open('../01-txt/red-chamber.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 数据清洗
cleaned_text = re.sub(r'\s+', ' ', text)

# 使用多种标点符号进行切分
split_pattern = r'[。]'
segments = re.split(split_pattern, cleaned_text)

# 去除空白段落
segments = [seg.strip() for seg in segments if seg.strip()]

# 转换为JSON格式并保存
data = [{'text': segment} for i, segment in enumerate(segments)]

with open('red-chamber-split-result.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("切割完毕: red-chamber-split-result.json")
