import os
import json
import logging
import tkinter as tk
from tkinter import messagebox

VERSION = "v4.0-beta"
LOG = "disable_helper.log"
SETTINGS_FILE = "disable_helper_settings.json"
DEFAULT_SETTINGS = {
    "assets": "./assets",
    "debug_mode": True,
    "language": "zh_cn",
    "confirm_file_delete": False,
    "msgbox_action_done": True
}

# Clear the log file before setting up logging
with open(LOG, 'w', encoding='utf-8') as file:
    file.write('')

def setup_logging(debug_mode):
    logging.basicConfig(
        level=logging.DEBUG if debug_mode else logging.INFO,  # Set the log level
        format="[%(asctime)s] [%(name)s/%(levelname)s]: %(message)s",  # Log format
        handlers=[
            logging.FileHandler(LOG, encoding="utf-8"),  # Write to a file with UTF-8 encoding
        ]
    )

class App:
    def __init__(self, config):
        self.config = config
        self.language_data = config.language_data
        self.root = tk.Tk()
        self.root.title(self.language_data["window_title"].format(version=VERSION))
        self.root.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):
        display_text = "\n".join([line.format(version=VERSION) for line in self.language_data["display"]])
        label = tk.Label(self.root, text=display_text)
        label.pack(pady=20)

        self.action_listbox = tk.Listbox(self.root)
        self.action_listbox.pack(pady=10)

        action_files = self.config.get_action_files()
        for action_file in action_files:
            self.action_listbox.insert(tk.END, action_file)

        run_button = tk.Button(self.root, text=self.language_data["button_run_action"], command=self.run_selected_action)
        run_button.pack(pady=10)

    def run_selected_action(self):
        selected_action = self.action_listbox.get(tk.ACTIVE) + ".json"
        if selected_action:
            try:
                actions = self.config.load_action_file(selected_action)
                if not isinstance(actions, list):
                    raise ValueError(f"Action file {selected_action} does not contain a list.")
                for action in actions:
                    if isinstance(action, dict):
                        self.config.execute_action(action, selected_action)
                logging.info(f"Action {selected_action} executed successfully.")
                if self.config.settings["msgbox_action_done"]:
                    messagebox.showinfo("Info", self.language_data["msgbox_action_done_message"].format(action=selected_action))
            except Exception as e:
                logging.error(f"Error executing action {selected_action}: {e}")
                messagebox.showerror("Error", f"An error occurred while executing the action: {e}")
        else:
            messagebox.showwarning("Warning", "No action selected.")

class Config:
    def __init__(self, settings_file):
        self.settings_file = settings_file
        self.settings = self.load_config()
        self.language_data = self.load_language_file()

    def load_config(self):
        settings = DEFAULT_SETTINGS.copy()
        
        # Override with disable_helper_settings.json if it exists
        if os.path.exists(self.settings_file):
            with open(self.settings_file, "r", encoding="utf-8") as file:
                settings_data = json.load(file)
                settings.update(settings_data)
        
        setup_logging(settings["debug_mode"])
        logging.info(f"Loaded configuration: {json.dumps(settings, indent=4, ensure_ascii=False)}")
        return settings

    def load_language_file(self):
        lang_file = os.path.join(self.settings["assets"], "disable_helper", "lang", f'{self.settings["language"]}.json')
        if not os.path.exists(lang_file):
            logging.error(f"Language file {lang_file} does not exist.")
            exit(1)
        with open(lang_file, "r", encoding="utf-8") as file:
            language_data = json.load(file)
        logging.info("Loaded language file")
        logging.debug(f"Language file data: {json.dumps(language_data, indent=4, ensure_ascii=False)}")
        return language_data

    def get_action_files(self):
        action_dir = os.path.join(self.settings["assets"], "disable_helper", "action")
        if not os.path.exists(action_dir):
            logging.error(f"Action directory {action_dir} does not exist.")
            exit(1)
        action_files = [os.path.splitext(f)[0] for f in os.listdir(action_dir) if f.endswith('.json') and not f.startswith("__")]
        return action_files

    def load_action_file(self, action_file):
        action_path = os.path.join(self.settings["assets"], "disable_helper", "action", action_file)
        try:
            with open(action_path, "r", encoding="utf-8") as file:
                actions = json.load(file)
                logging.info(f"Loaded action file {action_file}")
                logging.debug(f"Data inside {action_file}: {json.dumps(actions, indent=4, ensure_ascii=False)}")
                return actions
        except json.JSONDecodeError as e:
            logging.error(f"Failed to decode JSON from file {action_file}: {e}")
            return []

    def execute_action(self, action, action_file):
        action_type = action.get("type")
        method_name = f"execute_{action_type}"
        method = getattr(self, method_name, None)
        if method:
            logging.info(f"Executing action {action_type} from {action_file}")
            try:
                method(action, action_file)
            except Exception as e:
                logging.error(f"Error executing action {action_type} from {action_file}: {e}")
                raise
        else:
            logging.error(f"Unknown action type in {action_file}: {action_type}")

    def execute_check(self, action, action_file):
        prefix = action.get("prefix", "")
        assets = [prefix + asset for asset in action.get("assets", [])]
        logging.info(f"Checking assets: {assets}")
        if all(os.path.exists(asset) for asset in assets):
            logging.info(f"All assets exist, executing 'true' actions")
            for sub_action in action.get("true", []):
                self.execute_action(sub_action, action_file)
        else:
            logging.info(f"Not all assets exist, executing 'false' actions")
            for sub_action in action.get("false", []):
                self.execute_action(sub_action, action_file)

    def execute_copy(self, action, action_file):
        prefix = action.get("prefix", "")
        assets = [prefix + asset for asset in action.get("assets", [])]
        target = action.get("target", "")
        logging.info(f"Copying assets: {assets} to target: {target}")
        for asset in assets:
            if os.path.exists(asset):
                target_path = os.path.join(target, os.path.basename(asset))
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                try:
                    with open(asset, "rb") as src_file:
                        with open(target_path, "wb") as dst_file:
                            dst_file.write(src_file.read())
                    logging.info(f"Copied {asset} to {target_path}")
                except PermissionError as e:
                    logging.error(f"Permission denied while copying {asset} to {target_path}: {e}")
            else:
                logging.error(f"While running {action_file}, file not found: {asset}")

    def execute_delete(self, action, action_file):
        prefix = action.get("prefix", "")
        assets = [prefix + asset for asset in action.get("assets", [])]
        logging.info(f"Deleting assets: {assets}")
        if self.settings["confirm_file_delete"]:
            confirm = messagebox.askyesno(
                self.language_data["confirm_file_delete_title"],
                self.language_data["confirm_file_delete_message"]
            )
            if not confirm:
                logging.info("File deletion cancelled by user.")
                return
        for asset in assets:
            if os.path.exists(asset):
                try:
                    os.remove(asset)
                    logging.info(f"Deleted {asset}")
                except PermissionError as e:
                    logging.error(f"Permission denied while deleting {asset}: {e}")
            else:
                logging.error(f"While running {action_file}, file not found: {asset}")

    def execute_rename(self, action, action_file):
        prefix = action.get("prefix", "")
        assets = [prefix + asset for asset in action.get("assets", [])]
        sync = action.get("sync", False)
        logging.info(f"Renaming assets: {assets}")
        all_disabled = all(os.path.exists(asset) for asset in assets)
        all_enabled = all(os.path.exists(asset + ".disabled") for asset in assets)
        
        if sync:
            if all_disabled:
                for asset in assets:
                    new_name = asset + ".disabled"
                    try:
                        os.rename(asset, new_name)
                        logging.info(f"Renamed {asset} to {new_name}")
                    except PermissionError as e:
                        logging.error(f"Permission denied while renaming {asset} to {new_name}: {e}")
            elif all_enabled:
                for asset in assets:
                    new_name = asset
                    try:
                        os.rename(asset + ".disabled", new_name)
                        logging.info(f"Renamed {asset + '.disabled'} to {new_name}")
                    except PermissionError as e:
                        logging.error(f"Permission denied while renaming {asset + '.disabled'} to {new_name}: {e}")
            else:
                logging.error("Assets are not in a consistent state for sync rename.")
        else:
            for asset in assets:
                if os.path.exists(asset):
                    new_name = asset + ".disabled"
                    try:
                        os.rename(asset, new_name)
                        logging.info(f"Renamed {asset} to {new_name}")
                    except PermissionError as e:
                        logging.error(f"Permission denied while renaming {asset} to {new_name}: {e}")
                elif os.path.exists(asset + ".disabled"):
                    new_name = asset
                    try:
                        os.rename(asset + ".disabled", new_name)
                        logging.info(f"Renamed {asset + '.disabled'} to {new_name}")
                    except PermissionError as e:
                        logging.error(f"Permission denied while renaming {asset + '.disabled'} to {new_name}: {e}")
                else:
                    logging.error(f"While running {action_file}, file not found: {asset}")

    def execute_rewrite(self, action, action_file):
        prefix = action.get("prefix", "")
        assets = [prefix + asset for asset in action.get("assets", [])]
        data = action.get("data", "")
        if isinstance(data, list):
            data = "\n".join(data)
        logging.info(f"Rewriting assets: {assets} with data: {data}")
        for asset in assets:
            try:
                with open(asset, "w", encoding="utf-8") as file:
                    file.write(data)
                logging.info(f"While running {action_file}, rewrote {asset}")
            except PermissionError as e:
                logging.error(f"Permission denied while rewriting {asset}: {e}")

    def execute_log(self, action, action_file):
        level = action.get("level", "info").lower()
        msg = action.get("msg", "")
        if isinstance(msg, list):
            msg = "\n".join(msg)
        logging.info(f"Logging message at level {level}: {msg}")
        if level == "debug":
            logging.debug(msg)
        elif level == "info":
            logging.info(msg)
        elif level == "warning":
            logging.warning(msg)
        elif level == "error":
            logging.error(msg)
        elif level == "critical":
            logging.critical(msg)
        else:
            logging.error(f"Unknown log level in {action_file}: {level}")

    def execute_msgbox(self, action, action_file):
        level = action.get("level", "info").lower()
        msg = action.get("msg", "")
        if isinstance(msg, list):
            msg = "\n".join(msg)
        logging.info(f"Showing message box at level {level}: {msg}")
        if level == "info":
            messagebox.showinfo("Info", msg)
        elif level == "warning":
            messagebox.showwarning("Warning", msg)
        elif level == "error":
            messagebox.showerror("Error", msg)
        else:
            logging.error(f"Unknown message box level in {action_file}: {level}")

    def execute_run(self, action, action_file):
        for sub_action_file in action.get("action", []):
            sub_action_path = os.path.join(self.settings["assets"], "disable_helper", "action", sub_action_file)
            logging.info(f"Running sub-action file: {sub_action_file}")
            if os.path.exists(sub_action_path):
                sub_actions = self.load_action_file(sub_action_file)
                if not isinstance(sub_actions, list):
                    logging.error(f"Action file {sub_action_file} does not contain a list.")
                    continue
                for sub_action in sub_actions:
                    if isinstance(sub_action, dict):
                        self.execute_action(sub_action, sub_action_file)
                    else:
                        logging.error(f"Invalid sub-action format in {sub_action_file}: {sub_action}")
                logging.info(f"Action {sub_action_file} executed successfully.")
            else:
                logging.error(f"While running {action_file}, action file not found: {sub_action_path}")

if __name__ == "__main__":
    config = Config(SETTINGS_FILE)
    start_actions = config.load_action_file("__start__.json")
    if not isinstance(start_actions, list):
        logging.error(f"Action file __start__.json does not contain a list.")
    else:
        for action in start_actions:
            if isinstance(action, dict):
                config.execute_action(action, "__start__.json")
    logging.info("Action __start__.json executed successfully.")
    app = App(config)
    app.root.mainloop()