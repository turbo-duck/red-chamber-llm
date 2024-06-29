import re
from tqdm import tqdm
import json
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms.chatglm3 import ChatGLM3


def translate_llm(messages: str) -> str:
    template = """
    {{ {input} }}
    """
    prompt = PromptTemplate.from_template(template)
    endpoint_url = "http://10.10.7.160:8000/v1/chat/completions"
    chat_glm = ChatGLM3(
        endpoint_url=endpoint_url,
        temperature=0.7,
    )
    llm = LLMChain(prompt=prompt, llm=chat_glm)
    llm_resp = llm.invoke({"input": messages})
    # print(f"input: {llm_resp['input']}")
    # print(f"text: {llm_resp['text']}")
    # print("===")
    return llm_resp['text']


# 读取文本数据
with open('../04-test/red-hat.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 数据清洗
cleaned_text = re.sub(r'\s+', ' ', text)

# 使用多种标点符号进行切分
split_pattern = r'[。]'
segments = re.split(split_pattern, cleaned_text)
segments = [seg.strip() for seg in segments if seg.strip()]

for each_seg in segments:
    result = translate_llm(each_seg)
    print(result)
