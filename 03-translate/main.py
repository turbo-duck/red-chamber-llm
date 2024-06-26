from tqdm import tqdm
import json
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms.chatglm3 import ChatGLM3


def translate_llm(messages: str) -> str:
    template = """
    请把下面内容翻译成中文7岁小孩子能听懂的大白话，大白话结果必须是中文，不可出现英语，且不要出现“这段话是说”、“这句话的意思是”等语句，直接返回结果就好:
    {{ {input} }}
    """
    prompt = PromptTemplate.from_template(template)
    endpoint_url = "http://10.10.7.160:8000/v1/chat/completions"
    chat_glm = ChatGLM3(
        endpoint_url=endpoint_url,
        temperature=0,
    )
    llm = LLMChain(prompt=prompt, llm=chat_glm)
    llm_resp = llm.invoke({"input": messages})
    print(f"input: {llm_resp['input']}")
    print(f"text: {llm_resp['text']}")
    print("===")
    return llm_resp['text']


with open("../02-split-txt/red-chamber-split-result.json", "r") as file:
    data_list = json.load(file)
    print("文件读入并加载JSON")

json_result = []
process_bar = tqdm(data_list)
n = 0
for each_json in process_bar:
    if n > 10:
        break
    n = n + 1
    origin_text = each_json['text']
    # 调用 ChatGLM 对内容进行翻译
    translated_text = translate_llm(origin_text)
    # user 为翻译结果
    # assistant 为原文内容
    item = {
        'conversations': [
            {'role': 'user', 'content': str(translated_text)},
            {'role': 'assistant', 'content': str(origin_text)}
        ]
    }
    json_result.append(item)

# 保存文件
split_index = int(len(json_result) * 0.8)
# 训练集 前80%
with open("translate-result-train.json", "w", encoding='utf-8') as train_file:
    for each_item in json_result[:split_index]:
        train_file.write(json.dumps(each_item, ensure_ascii=False) + '\n')

# 验证集 后20%
with open("translate-result-dev.json", "w", encoding='utf-8') as dev_file:
    for each_item in json_result[split_index:]:
        dev_file.write(json.dumps(each_item, ensure_ascii=False) + '\n')

