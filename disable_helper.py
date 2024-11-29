import os
import json
import shutil

global VERSION, DEFAULT_DATA
VERSION = "v3.3.2-beta"
DEFAULT_DATA = {'display': {'auto_next_line': False, 'color': '5', 'text': ['禁用助手 {version} - LIB临时工作室出品\n', '---------------------------------\n', '只是一个演示json配置文件是否可行的版本\n', '>']}, 'actions': {'1': {'end_output': "action '1' done\n", 'action': [{'type': 'disable', 'prefix': '', 'files': ['qwq']}, {'type': 'execute', 'code': ['for i in range(10):', '\tprint(i)']}, {'type': 'copy', 'prefix': '', 'source': ['qwq'], 'target': 'awa'}, {'type': 'delete', 'prefix': '', 'files': ['qwq']}]}}, 'lang': {'zh_cn': {'error_parse_config': '[错误] 解析配置文件时出现错误: {Error}\n删除配置文件可 能会解决此问题\n此输出无法在配置文件中更改', 'error_config_debug': '[错误] 引用配置文件时出现错误: {Error}\n\n删除配置文件可能会解决此问题\n按回车会试图复现并展示报错信息...\n', 'error_config_not_debug': '[错误] 引用配置文件时出现错误: {Error}\n\n删除配置文件可能会解决此问题\n按回车继续...\n', 'copy_file_not_found': '[错误] 项目不存在: {source_path}\n', 'copy_no_permission': '[错误] 无法复制或粘贴项目，权限不足: {source_path}\n', 'copy_succeeded': "[提示] 成功将 '{source_path}' 复制到 '{target_path}'\n", 'copy_unknown_error': '[错误] 复制项目时出现未知错误: {Error}\n', 'rename_file_not_found': '[错误] 项目不存在: {old_name}\n', 'rename_no_permission': '[错误] 无法重命名项目，权限不足: {old_name}\n', 'rename_succeeded': '[提示] 已重命名项目至 {new_name}\n', 'rename_unknown_error': '[错误] 重命名项目时出现未知错误: {Error}\n', 'delete_file_not_found': '[错误] 项目不存在: {file_path}\n', 'delete_no_permission': '[错误] 无法删除项目，权限不足: {file_path}\n', 'delete_succeeded': '[提示] 已删除项目 {file_path}\n', 'delete_unknown_error': '[错误] 重命名项目时出现未知错 误: {Error}\n', 'action_rename_complete': '[提示] 操作完成，启用了{enabled_assets_cnt}个项目，禁用了{disabled_assets_cnt}个项目。按回车继续...', 'action_copy_complete': '[提示] 操作完成，复制了项目，至{target_path}。按回车继续...', 'action_execute_complete': '[提示] 操作完成，运行了{run_code_cnt}行python代码。按回车继续...', 'action_delete_complete': '[提示] 操作完成，删了点东西懒得写了。按回车继续...', 'confirm_execute_code': '[提示] 你要执行的操作中包括运行未知的python代码 ，输入任意信息后按回车继续，按回车跳过该操作...', 'confirm_file_delete': '[提示] 你要执行的操作中包括删除文件，输入任意 信息后按回车继续，按回车跳过该操作...', 'file_not_found': '[错误] 项目不存在: {file}\n', 'skip_file': '[提示] 略过了：{file}\n', 'unknown_input': '[提示] 无效输入，请重试...', 'unknown_file_action': '[错误] 未知的文件操作: {action}。按回车 继续...'}}, 'settings': {'gui_mode': False, 'debug_mode': True, 'language': 'zh_cn', 'confirm_execute_code': True, 'confirm_file_delete': True}}

def clear_screen():
	"""Clears the console screen."""
	os.system("cls" if os.name == "nt" else "clear")

def rename_assets(old_name, new_name, messages):
	"""Renames a file and handles potential errors."""
	try:
		os.rename(old_name, new_name)
		print(messages["rename_succeeded"].format(old_name=old_name, new_name=new_name), end="")
	except FileNotFoundError:
		print(messages["rename_file_not_found"].format(old_name=old_name, new_name=new_name), end="")
	except PermissionError:
		print(messages["rename_no_permission"].format(old_name=old_name, new_name=new_name), end="")
	except Exception as error:
		print(messages["rename_unknown_error"].format(old_name=old_name, new_name=new_name, error=error), end="")

def copy_assets(source_path, destination_path, messages):
	try:
		shutil.copytree(source_path, destination_path, dirs_exist_ok=True)
		print(messages["copy_succeeded"].format(source_path=source_path, destination_path=destination_path), end="")
	except FileNotFoundError:
		print(messages["copy_file_not_found"].format(source_path=source_path, destination_path=destination_path), end="")
	except PermissionError:
		print(messages["copy_no_permission"].format(source_path=source_path, destination_path=destination_path), end="")
	except Exception as error:
		print(messages["copy_unknown_error"].format(source_path=source_path, destination_path=destination_path, error=error), end="")

def delete_assets(file_path, messages):
	try:
		os.remove(file_path)
		print(messages["delete_succeeded"].format(file_path=file_path), end="")
	except FileNotFoundError:
		print(messages["delete_file_not_found"].format(file_path=file_path), end="")
	except PermissionError:
		print(messages["delete_no_permission"].format(file_path=file_path), end="")
	except Exception as error:
		print(messages["delete_unknown_error"].format(file_path=file_path, error=error), end="")


def parse_config(config_file="禁用助手配置文件.json"):
	"""Parses the configuration file and creates a default if missing."""
	# Load or create configuration
	if not os.path.exists(config_file):
		with open(config_file, "w", encoding="utf-8") as f:
			json.dump(DEFAULT_DATA, f, indent="\t", ensure_ascii=False)
		return DEFAULT_DATA

	with open(config_file, "r", encoding="utf-8") as f:
		return json.load(f)


def process_files_disable(action, keys):
	enabled_assets_cnt = 0
	disabled_assets_cnt = 0

	prefix = action["prefix"]
	files = action["files"]
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

def process_files_execute(user_input, action, keys):
	run_code_cnt = len(action["code"])
	code = "\n".join(action["code"])

	exec(code)

	input(keys["action_execute_complete"].format(
		run_code_cnt=run_code_cnt
	))
	
	return run_code_cnt

def process_files_copy(action, keys):
	prefix = action["prefix"]
	files = action["source"]
	target = action["target"]

	for file in files:
		full_path = os.path.join(prefix, file)
		if os.path.exists(full_path):
			copy_assets(full_path, target, keys)
		else:
			print(keys["file_not_found"].format(file=full_path), end="")
	
	input(keys["action_copy_complete"].format(
		target_path=target
	))

def process_files_delete(action, keys):
	prefix = action["prefix"]
	files = action["files"]

	for file in files:
		full_path = os.path.join(prefix, file)
		if os.path.exists(full_path):
			delete_assets(full_path, keys)
		else:
			print(keys["file_not_found"].format(file=full_path), end="")
	
	input(keys["action_delete_complete"])

def process_command(user_input, actions, keys, settings):
	"""Toggles file states based on user input."""

	if not user_input in actions:
		input(keys["unknown_input"])
		return
	
	for action in actions[user_input]["action"]:
		if not "type" in action or action["type"] == "disable":
			process_files_disable(action, keys)
		elif action["type"] == "copy":
			process_files_copy(action, keys)
		elif action["type"] == "execute":
			if not settings["confirm_execute_code"] or input(keys["confirm_execute_code"]):
				process_files_execute(user_input, action, keys)
		elif action["type"] == "delete":
			if not settings["confirm_file_delete"] or input(keys["confirm_file_delete"]):
				process_files_delete(action, keys)
		else:
			input(keys["unknown_file_action"].format(action=action["type"]))
	
	if "end_output" in actions[user_input]:
		input(actions[user_input]["end_output"])

def main_loop(display, actions, keys, settings):
	clear_screen()
	user_input = input(display.format(version=VERSION)).strip()

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
		
	
	main_loop(display, actions, keys, settings)

def setup():
	try:
		config = parse_config()
	except Exception as Error:
		input(f"[错误] 解析配置文件时出现错误: {Error}\n删除配置文件可能会解决此问题")	
	
	if "color" in config["display"]:
		os.system("color " + config["display"]["color"])
	
	if "auto_next_line" not in config["display"] or not config["display"]["auto_next_line"]:
		display = "".join(config["display"]["text"])
	else:
		display = "\n".join(config["display"]["text"])
	
	settings:dict = DEFAULT_DATA["settings"]; settings.update(config["settings"])
	actions:dict = DEFAULT_DATA["actions"]; actions.update(config["actions"])
	keys:dict = DEFAULT_DATA["lang"]; keys.update(config["lang"])

	main_loop(display, actions, keys[settings["language"]], settings)

if __name__ == "__main__":
	setup()
