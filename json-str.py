import json

with open("disable_helper_config.json", encoding="utf-8") as f:
	data = json.load(f)

input(data)