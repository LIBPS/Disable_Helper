import os
import json
import shutil

global VERSION, DEFAULT_DATA
VERSION = "v3.4-beta"
DEFAULT_DATA = {'display': {'color': '5', 'text': ['禁用助手 {version} - LIB 临时工作室出品\n', '---------------------------------\n', '只是一个演示json配置文件是否可行的版本\n', '>']}, 'action': {'1': {'end_output': "action '1' done\n", 'action': [{'type': 'disable', 'prefix': '', 'files': ['qwq']}, {'type': 'execute', 'code': ['for i in range(10):', '\tprint(i)']}, {'type': 'copy', 'prefix': '', 'source': ['qwq'], 'target': 'awa'}, {'type': 'delete', 'prefix': '', 'files': ['qwq']}]}}, 'lang': {'zh_cn': {'error_parse_config': '[错误] 解析配置文件时出现错误: {Error}\n删除配置文件可 能会解决此问题\n此输出无法在配置文件中更改', 'error_config_debug': '[错误] 引用配置文件时出现错误: {Error}\n\n删除配置文件可能会解决此问题\n按回车会试图复现并展示报错信息...\n', 'error_config_not_debug': '[错误] 引用配置文件时出现错误: {Error}\n\n删除配置文件可能会解决此问题\n按回车继续...\n', 'copy_file_not_found': '[错误] 项目不存在: {source_path}\n', 'copy_no_permission': '[错误] 无法复制或粘贴项目，权限不足: {source_path}\n', 'copy_succeeded': "[提示] 成功将 '{source_path}' 复制到 '{target_path}'\n", 'copy_unknown_error': '[错误] 复制项目时出现未知错误: {Error}\n', 'rename_file_not_found': '[错误] 项目不存在: {old_name}\n', 'rename_no_permission': '[错误] 无法重命名项目，权限不足: {old_name}\n', 'rename_succeeded': '[提示] 已重命名项目至 {new_name}\n', 'rename_unknown_error': '[错误] 重命名项目时出现未知错误: {Error}\n', 'delete_file_not_found': '[错误] 项目不存在: {file_path}\n', 'delete_no_permission': '[错误] 无法删除项目，权限不足: {file_path}\n', 'delete_succeeded': '[提示] 已删除项目 {file_path}\n', 'delete_unknown_error': '[错误] 重命名项目时出现未知错 误: {Error}\n', 'action_rename_complete': '[提示] 操作完成，启用了{enabled_assets_cnt}个项目，禁用了{disabled_assets_cnt}个项目。按回车继续...', 'action_copy_complete': '[提示] 操作完成，复制了项目，至{target_path}。按回车继续...', 'action_execute_complete': '[提示] 操作完成，运行了{run_code_cnt}行python代码。按回车继续...', 'action_delete_complete': '[提示] 操作完成，删了点东西懒得写了。按回车继续...', 'confirm_execute_code': '[提示] 你要执行的操作中包括运行未知的python代码 ，输入任意信息后按回车继续，按回车跳过该操作...', 'confirm_file_delete': '[提示] 你要执行的操作中包括删除文件，输入任意 信息后按回车继续，按回车跳过该操作...', 'file_not_found': '[错误] 项目不存在: {file}\n', 'skip_file': '[提示] 略过了：{file}\n', 'unknown_input': '[提示] 无效输入，请重试...', 'unknown_file_action': '[错误] 未知的文件操作: {action}。按回车 继续...'}}, 'settings': {'gui_mode': False, 'debug_mode': True, 'language': 'zh_cn', 'confirm_execute_code': True, 'confirm_file_delete': True}}

class Config:
	def __init__(self, file_content:dict=DEFAULT_DATA, file_name="disable_helper_config.json") -> None:
		self.raw = file_content
		self.name = file_name

		self.display_raw = file_content["display"]
		self.display_text = "\n".join(self.display_raw["text"]).format(version=VERSION)
		self.settings = file_content["settings"]
		self.action = file_content["action"]
		self.lang = self.settings["language"]
		self.keys = file_content["lang"][self.lang]
		
	
	def gen_config(self, file_content:dict=DEFAULT_DATA):
		with open(self.name, "w", encoding="utf-8") as f:
			json.dump(file_content, f, indent="\t", ensure_ascii=False)

	def parse_config(self, file_name="disable_helper_config.json"):
		with open(file_name, "r", encoding="utf-8") as f:
			new_content = json.load(f)
			self.raw = new_content			
			self.display_raw = new_content["display"]
			self.display_text = "\n".join(self.display_raw["text"]).format(version=VERSION)
			self.settings = new_content["settings"]
			self.action = new_content["action"]
			self.lang = self.settings["language"]
			self.keys = new_content["lang"][self.lang]

	def output_key(self, key="unknown_input", function=print):
		if key in self.keys:
			function(self.keys[key])
		

class App:
	def __init__(self, ) -> None:
		self.config = Config()
	
	def clear_screen(self): 
		os.system("cls" if os.name == "nt" else "clear")
	
	def start(self):
		if not os.path.exists(self.config.name):
			self.config.gen_config()
		self.config.parse_config()

		if "color" in self.config.display_raw:
			os.system("color " + self.config.display_raw["color"])
	
	def main(self):
		self.clear_screen()
		user_input = input(self.config.display_text).strip()
	
		if not user_input in self.config.action:
			self.config.output_key("unknown_input", input)
			return

		try:
			process_command(user_input, actions, keys, settings)
		except Exception as Error:
			if settings["debug_mode"]:
				if "error_config_debug" in keys:
					input(keys["error_config_debug"].format(Error=Error))
				else:
					input(DEFAULT_DATA["lang"]["zh_cn"]["error_config_debug"])
				process_command(user_input, actions, keys, settings)
			else:
				if "error_config_not_debug" in keys:
					input(keys["error_config_not_debug"].format(Error=Error))
				else:
					input(DEFAULT_DATA["lang"]["zh_cn"]["error_config_not_debug"])

class File(Config):
	def __init__(self, file_path, file_name) -> None:
		self.file_path = file_path
		self.file_name = file_name
		self.full_path = os.path.join(file_path, file_name)
	
	def disable(self, keys):
		for file in files:
			full_path = os.path.join(prefix, file)
			if os.path.exists(full_path):
				rename_assets(full_path, full_path + ".disabled", keys)
				disabled_assets_cnt += 1
			elif os.path.exists(full_path + ".disabled"):
				rename_assets(full_path + ".disabled", full_path, keys)
				enabled_assets_cnt += 1
			else:
				print(keys["file_not_found"].format(file=full_path), end="")
		
		input(keys["action_rename_complete"].format(
			enabled_assets_cnt=enabled_assets_cnt,
			disabled_assets_cnt=disabled_assets_cnt
		))
		
		return enabled_assets_cnt, disabled_assets_cnt

if __name__ == "__main__":
	main = App()
	main.start()

	while True:
		main.main()
