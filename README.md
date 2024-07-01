# red-chamber-llm
🚧 对中国经典名著《红楼梦》处理，并利用该数据对 ChatGLM3-6B 进行微调，通过它来学习微调等。项目包括文本处理、模型训练和应用开发。This project focuses on processing the Chinese literary classic "Dream of the Red Chamber" and fine-tuning the ChatGLM3-6B model using this data. The goal is to enhance the model's capabilities in understanding and generating text related to the novel. The project encompasses text processing, model training, and application development.


# 先起草稿 后续整理


# 01-txt
下载到red-chamber.txt 红楼梦的小说全集。


# 02-split-txt
写一个脚本对数据进行切分，目前计划根据“。”进行切分。并保存成一个独立的文件。
```python
# 使用多种标点符号进行切分
split_pattern = r'[。]'
segments = re.split(split_pattern, cleaned_text)
```

# 03-翻译对照
取 02 中的数据，每条都使用 ChatGLM3-6B 进行翻译，并整理成对照的关系。


```json lines
{"conversations": [{"role": "user", "content": "袭人看到这个情况，知道黛玉心里很困惑，就像宝玉一样。于是她对紫鹃说：“黛玉刚才病了，我让秋纹妹妹扶她回去休息一下。”"}, {"role": "assistant", "content": "袭人见了这样，知道黛玉此时心中迷惑，和宝玉一样，因悄和紫鹃说道：“姑娘才好了，我叫秋纹妹妹同着你搀回姑娘，歇歇去罢"}]}
{"conversations": [{"role": "user", "content": "因为回头对秋纹说：“你和紫鹃姐姐送林姑娘去吧，你不能乱说话哦。”"}, {"role": "assistant", "content": "”因回头向秋纹道：“你和紫鹃姐姐送林姑娘去罢，你可别混说话"}]}
```

# 04-test
训练结束后，把 checkpoint-2500 LoRA的结果加载到模型中进行测试：

- red-hat.txt 小红帽原版
- red-hat-result.txt ChatGLM3-6B + checkpoint-2500 的测试结果


原文
```
有一天，小红帽的母亲让她去看望生病的祖母，并送上一篮子食物。
母亲叮嘱她要小心，不要在森林里和陌生人说话。
小红帽出发了，在森林里，她遇到了一只大灰狼。
大灰狼知道小红帽要去看望祖母，于是决定先一步到达祖母的家。
他装成小红帽，骗祖母打开了门，然后把她吞了下去。
狼穿上祖母的衣服，躺在床上等待小红帽的到来。
小红帽来到祖母的家，看到“祖母”躺在床上，感到很奇怪。
她问：“祖母，你的耳朵怎么这么大？”
狼回答：“为了更好地听你说话。”
小红帽又问：“祖母，你的眼睛怎么这么大？”
狼回答：“为了更好地看你。”
最后，小红帽问：“祖母，你的嘴巴怎么这么大？”
狼回答：“为了更好地吃掉你！”
说完，狼从床上跳起来，把小红帽也吞了下去。
幸运的是，一个猎人在森林里听到了动静，他赶到祖母家，把狼的肚子剖开，救出了小红帽和她的祖母。
猎人把狼带走了，从此，小红帽吸取了教训，再也不在森林里和陌生人说话了。

```

译文
```
一日便叫了小红来问安，又命人持一篮子礼物来看祖母。
母忙嘱道：“不可在林内与生人言语“。
小红果便起身往林中走，遇见一个老底子大灰狼。
大灰狼便知道那小丫头去给老太太拜年去了，便也先进了门。
他便假作小红的模样，骗着老娘子开了门，一径吞进去。
说着，脱了衣裳，上床安歇，候着那小丫头。
小丫头忙到祖母房里来见，只见床上躺着个老奶奶。
她便说：“祖母的耳鼓子怎么生的这样大？“
狼道：“为着好叫”
小红便道：“祖母，你那眼睛怎么这样大“
狼道：“为着好瞧你“
说着，便又问道：“祖母的嘴儿怎么这大的？”
狼便道：“为报应你”
说着，那狼便从床上跳起，连同小红帽一齐吃去了“
幸亏一猎人从林内经过，听得哭声，赶忙到祖母家来，将狼肚割破，救出小红儿与老奶奶。
因将狼带来，自那日与小郎君说了这番话后，便不再往林中去了。
```

# 05-result
LoRA的训练节点文件，其实有很多，我就留了一个 2500 的。在 3090 上训练还是非常快的。

- checkpoint-2500

