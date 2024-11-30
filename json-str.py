import json

with open("禁用助手配置文件.json", encoding="utf-8") as f:
	data = json.load(f)

input(data)