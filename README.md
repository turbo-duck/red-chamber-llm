# red-chamber-llm
🚧 对中国经典名著《红楼梦》处理，并利用该数据对 ChatGLM3-6B 进行微调，通过它来学习微调等。项目包括文本处理、模型训练和应用开发。This project focuses on processing the Chinese literary classic "Dream of the Red Chamber" and fine-tuning the ChatGLM3-6B model using this data. The goal is to enhance the model's capabilities in understanding and generating text related to the novel. The project encompasses text processing, model training, and application development.

# 先起草稿 后续整理

# 01-txt
下载到red-chamber.txt 红楼梦的小说全集。

# 02-split-txt
写一个脚本对数据进行切分，目前计划根据“。”进行切分。并保存成一个独立的文件。

# 03-翻译对照
取 02 中的数据，每条都使用 ChatGLM3-6B 进行翻译，并整理成对照的关系。

[{
    "user": "原文",
    "bot": "译文",
}...]

# 04-LoRA Config


# 05-训练

# 06-测试

