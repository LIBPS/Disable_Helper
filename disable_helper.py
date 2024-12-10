import os
import json
import shutil

global VERSION, DEFAULT_DATA
VERSION = "v3.4-beta.1  "
DEFAULT_DATA = {'display': {'color': '5', 'text': ['禁用助手 {version} - LIB 临时工作室出品\n', '---------------------------------\n', '只是一个演示json配置文件是否可行的版本\n', '>']}, 'action': {'1': {'end_output': "action '1' done\n", 'action': [{'type': 'disable', 'prefix': '', 'files': ['qwq']}, {'type': 'execute', 'code': ['for i in range(10):', '\tprint(i)']}, {'type': 'copy', 'prefix': '', 'source': ['qwq'], 'target': 'awa'}, {'type': 'delete', 'prefix': '', 'files': ['qwq']}]}}, 'lang': {'zh_cn': {'error_parse_config': '[错误] 解析配置文件时出现错误: {Error}\n删除配置文件可 能会解决此问题\n此输出无法在配置文件中更改', 'error_config_debug': '[错误] 引用配置文件时出现错误: {Error}\n\n删除配置文件可能会解决此问题\n按回车会试图复现并展示报错信息...\n', 'error_config_not_debug': '[错误] 引用配置文件时出现错误: {Error}\n\n删除配置文件可能会解决此问题\n按回车继续...\n', 'copy_file_not_found': '[错误] 项目不存在: {source_path}\n', 'copy_no_permission': '[错误] 无法复制或粘贴项目，权限不足: {source_path}\n', 'copy_succeeded': "[提示] 成功将 '{source_path}' 复制到 '{target_path}'\n", 'copy_unknown_error': '[错误] 复制项目时出现未知错误: {Error}\n', 'rename_file_not_found': '[错误] 项目不存在: {old_name}\n', 'rename_no_permission': '[错误] 无法重命名项目，权限不足: {old_name}\n', 'rename_succeeded': '[提示] 已重命名项目至 {new_name}\n', 'rename_unknown_error': '[错误] 重命名项目时出现未知错误: {Error}\n', 'delete_file_not_found': '[错误] 项目不存在: {file_path}\n', 'delete_no_permission': '[错误] 无法删除项目，权限不足: {file_path}\n', 'delete_succeeded': '[提示] 已删除项目 {file_path}\n', 'delete_unknown_error': '[错误] 重命名项目时出现未知错 误: {Error}\n', 'action_rename_complete': '[提示] 操作完成，启用了{enabled_assets_cnt}个项目，禁用了{disabled_assets_cnt}个项目。按回车继续...', 'action_copy_complete': '[提示] 操作完成，复制了项目，至{target_path}。按回车继续...', 'action_execute_complete': '[提示] 操作完成，运行了{run_code_cnt}行python代码。按回车继续...', 'action_delete_complete': '[提示] 操作完成，删了点东西懒得写了。按回车继续...', 'confirm_execute_code': '[提示] 你要执行的操作中包括运行未知的python代码 ，输入任意信息后按回车继续，按回车跳过该操作...', 'confirm_file_delete': '[提示] 你要执行的操作中包括删除文件，输入任意 信息后按回车继续，按回车跳过该操作...', 'file_not_found': '[错误] 项目不存在: {file}\n', 'skip_file': '[提示] 略过了：{file}\n', 'unknown_input': '[提示] 无效输入，请重试...', 'unknown_file_action': '[错误] 未知的文件操作: {action}。按回车 继续...'}}, 'settings': {'gui_mode': False, 'debug_mode': True, 'language': 'zh_cn', 'confirm_execute_code': True, 'confirm_file_delete': True}}

"""
## 版本

+1		不看代码就看的出来的大更新
+0.1	看代码才看的出来的大更新(重新上传默认配置文件)
+0.0.1	用来看作者还在更新的更新

-beta	测试中
-dev	可能无法运行但不小心发上去了
"""


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

		try:
			self.config.process_command(user_input)
		except Exception as Error:
			# TODO
			"""if settings["debug_mode"]:
				if "error_config_debug" in keys:
					input(keys["error_config_debug"].format(Error=Error))
				else:
					input(DEFAULT_DATA["lang"]["zh_cn"]["error_config_debug"])
				process_command(user_input, actions, keys, settings)
			else:
				if "error_config_not_debug" in keys:
					input(keys["error_config_not_debug"].format(Error=Error))
				else:
					input(DEFAULT_DATA["lang"]["zh_cn"]["error_config_not_debug"])"""

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
	
	def process_command(self, user_input):
		if not user_input in self.action:
			input(self.keys["unknown_input"])
			return
		
		for action in self.action[user_input]["action"]:
			action = Action(action, self.keys)
			action.execute_action()

		input(self.action[user_input]["end_output"] if "end_output" in self.action[user_input] else "")

class Action:
    def __init__(self, action_data, keys):
        """
        Initialize the Action class with action data and localized keys for messages.
        """
        self.action_data = action_data
        self.keys = keys

    def execute_action(self):
        """
        Executes the action based on its type.
        """
        action_type = self.action_data.get("type").lower()

        if action_type == "disable":
            return self.disable()
        elif action_type == "execute":
            return self.execute_code()
        elif action_type == "copy":
            return self.copy_files()
        elif action_type == "delete":
            return self.delete_files()
        else:
            print(self.keys["unknown_file_action"].format(action=action_type))
            return None

    def disable(self):
        """
        Renames files to enable/disable them by adding/removing `.disabled`.
        """
        prefix = self.action_data.get("prefix", "")
        files = self.action_data.get("assets", [])
        enabled_assets_cnt = 0
        disabled_assets_cnt = 0

        for file in files:
            full_path = os.path.join(prefix, file)
            if os.path.exists(full_path):
                new_name = full_path + ".disabled"
                os.rename(full_path, new_name)
                print(self.keys["rename_succeeded"].format(old_name=full_path, new_name=new_name), end="")
                disabled_assets_cnt += 1
            elif os.path.exists(full_path + ".disabled"):
                new_name = full_path[:-9]  # Remove `.disabled`
                os.rename(full_path + ".disabled", new_name)
                print(self.keys["rename_succeeded"].format(old_name=full_path + ".disabled", new_name=new_name), end="")
                enabled_assets_cnt += 1
            else:
                print(self.keys["file_not_found"].format(file=full_path), end="")

        print(self.keys["action_rename_complete"].format(
            enabled_assets_cnt=enabled_assets_cnt,
            disabled_assets_cnt=disabled_assets_cnt
        ), end="")

    def execute_code(self):
        """
        Executes Python code provided in the configuration.
        """
        code_lines = self.action_data.get("assets", [])
        code = "\n".join(code_lines)

        try:
            exec(code)
            print(self.keys["action_execute_complete"].format(run_code_cnt=len(code_lines)), end="")
        except Exception as e:
            print(self.keys["rename_unknown_error"].format(error=str(e)), end="")

    def copy_files(self):
        """
        Copies files or directories to the specified target.
        """
        prefix = self.action_data.get("prefix", "")
        files = self.action_data.get("assets", [])
        target = self.action_data.get("target", "")

        for file in files:
            source_path = os.path.join(prefix, file)
            target_path = os.path.join(prefix, target, file)

            try:
                shutil.copytree(source_path, target_path, dirs_exist_ok=True)
                print(self.keys["copy_succeeded"].format(source_path=source_path, target_path=target_path), end="")
            except FileNotFoundError:
                print(self.keys["copy_file_not_found"].format(source_path=source_path), end="")
            except PermissionError:
                print(self.keys["copy_no_permission"].format(source_path=source_path), end="")
            except Exception as e:
                print(self.keys["copy_unknown_error"].format(error=str(e)), end="")

    def delete_files(self):
        """
        Deletes files or directories specified in the configuration.
        """
        prefix = self.action_data.get("prefix", "")
        files = self.action_data.get("assets", [])

        for file in files:
            full_path = os.path.join(prefix, file)

            try:
                if os.path.isfile(full_path):
                    os.remove(full_path)
                elif os.path.isdir(full_path):
                    shutil.rmtree(full_path)
                print(self.keys["delete_succeeded"].format(file_path=full_path), end="")
            except FileNotFoundError:
                print(self.keys["delete_file_not_found"].format(file_path=full_path), end="")
            except PermissionError:
                print(self.keys["delete_no_permission"].format(file_path=full_path), end="")
            except Exception as e:
                print(self.keys["delete_unknown_error"].format(error=str(e)), end="")

		

if __name__ == "__main__":
	main = App()
	main.start()

	while True:
		main.main()
