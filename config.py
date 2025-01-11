import os
import json
import logging
from PyQt5 import QtWidgets

DEFAULT_SETTINGS = {
    "assets": "./assets",
    "debug_mode": True,
    "language": "zh_cn",
    "confirm_file_delete": False,
    "msgbox_action_done": True
}

LOG_FILE = "disable_helper.log"
logger = logging.getLogger("DisableHelper")
action_logger = logging.getLogger("Action")

def setup_logging(debug_mode):
    # Clear the log file before setting up logging
    with open(LOG_FILE, 'w', encoding='utf-8') as file:
        file.write('')
    
    logging.basicConfig(
        level=logging.DEBUG if debug_mode else logging.INFO,  # Set the log level
        format="[%(asctime)s] [%(name)s/%(levelname)s]: %(message)s",  # Log format
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),  # Write to a file with UTF-8 encoding
        ]
    )

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
        logger.info(f"Loaded configuration: {json.dumps(settings, indent=4, ensure_ascii=False)}")
        return settings

    def load_language_file(self):
        lang_file = os.path.join(self.settings["assets"], "disable_helper", "lang", f'{self.settings["language"]}.json')
        if not os.path.exists(lang_file):
            logger.error(f"Language file {lang_file} does not exist.")
            exit(1)
        with open(lang_file, "r", encoding="utf-8") as file:
            language_data = json.load(file)
        logger.info("Loaded language file")
        logger.debug(f"Language file data: {json.dumps(language_data, indent=4, ensure_ascii=False)}")
        return language_data

    def get_action_files(self):
        action_dir = os.path.join(self.settings["assets"], "disable_helper", "action")
        if not os.path.exists(action_dir):
            logger.error(f"Action directory {action_dir} does not exist.")
            exit(1)
        action_files = [os.path.splitext(f)[0] for f in os.listdir(action_dir) if f.endswith('.json') and not f.startswith("__")]
        return action_files

    def load_action_file(self, action_file):
        action_path = os.path.join(self.settings["assets"], "disable_helper", "action", action_file)
        try:
            with open(action_path, "r", encoding="utf-8") as file:
                actions = json.load(file)
                logger.info(f"Loaded action file {action_file}")
                logger.debug(f"Data inside {action_file}: {json.dumps(actions, indent=4, ensure_ascii=False)}")
                return actions
        except json.JSONDecodeError as e:
            logger.error(f"Failed to decode JSON from file {action_file}: {e}")
            return []

    def execute_action(self, action, action_file):
        action_type = action.get("type")
        method_name = f"execute_{action_type}"
        method = getattr(self, method_name, None)
        if method:
            action_logger.debug(f"Executing action {action_type} from {action_file}")
            try:
                method(action, action_file)
            except Exception as e:
                action_logger.error(f"Error executing action {action_type} from {action_file}: {e}")
                raise
        else:
            action_logger.error(f"Unknown action type in {action_file}: {action_type}")

    def execute_check(self, action, action_file):
        prefix = action.get("prefix", "")
        assets = [prefix + asset for asset in action.get("assets", [])]
        action_logger.debug(f"Checking assets: {assets}")
        if all(os.path.exists(asset) for asset in assets):
            action_logger.debug(f"All assets exist, executing 'true' actions")
            for sub_action in action.get("true", []):
                self.execute_action(sub_action, action_file)
        else:
            action_logger.debug(f"Not all assets exist, executing 'false' actions")
            for sub_action in action.get("false", []):
                self.execute_action(sub_action, action_file)

    def execute_copy(self, action, action_file):
        prefix = action.get("prefix", "")
        assets = [prefix + asset for asset in action.get("assets", [])]
        target = action.get("target", "")
        action_logger.debug(f"Copying assets: {assets} to target: {target}")
        for asset in assets:
            if os.path.exists(asset):
                target_path = os.path.join(target, os.path.basename(asset))
                os.makedirs(os.path.dirname(target_path), exist_ok=True)
                try:
                    with open(asset, "rb") as src_file:
                        with open(target_path, "wb") as dst_file:
                            dst_file.write(src_file.read())
                    action_logger.debug(f"Copied {asset} to {target_path}")
                except PermissionError as e:
                    action_logger.error(f"Permission denied while copying {asset} to {target_path}: {e}")
            else:
                action_logger.error(f"While running {action_file}, file not found: {asset}")

    def execute_delete(self, action, action_file):
        prefix = action.get("prefix", "")
        assets = [prefix + asset for asset in action.get("assets", [])]
        action_logger.debug(f"Deleting assets: {assets}")
        if self.settings["confirm_file_delete"]:
            confirm = QtWidgets.QMessageBox.question(
                None,
                self.language_data["confirm_file_delete_title"],
                self.language_data["confirm_file_delete_message"],
                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No
            )
            if confirm != QtWidgets.QMessageBox.Yes:
                action_logger.info("File deletion cancelled by user.")
                return
        for asset in assets:
            if os.path.exists(asset):
                try:
                    os.remove(asset)
                    action_logger.debug(f"Deleted {asset}")
                except PermissionError as e:
                    action_logger.error(f"Permission denied while deleting {asset}: {e}")
            else:
                action_logger.error(f"While running {action_file}, file not found: {asset}")

    def execute_rename(self, action, action_file):
        prefix = action.get("prefix", "")
        assets = [prefix + asset for asset in action.get("assets", [])]
        sync = action.get("sync", False)
        action_logger.debug(f"Renaming assets: {assets}")
        all_disabled = all(os.path.exists(asset) for asset in assets)
        all_enabled = all(os.path.exists(asset + ".disabled") for asset in assets)
        
        if sync:
            if all_disabled:
                for asset in assets:
                    new_name = asset + ".disabled"
                    try:
                        os.rename(asset, new_name)
                        action_logger.debug(f"Renamed {asset} to {new_name}")
                    except PermissionError as e:
                        action_logger.error(f"Permission denied while renaming {asset} to {new_name}: {e}")
            elif all_enabled:
                for asset in assets:
                    new_name = asset
                    try:
                        os.rename(asset + ".disabled", new_name)
                        action_logger.debug(f"Renamed {asset + '.disabled'} to {new_name}")
                    except PermissionError as e:
                        action_logger.error(f"Permission denied while renaming {asset + '.disabled'} to {new_name}: {e}")
            else:
                action_logger.error("Assets are not in a consistent state for sync rename.")
        else:
            for asset in assets:
                if os.path.exists(asset):
                    new_name = asset + ".disabled"
                    try:
                        os.rename(asset, new_name)
                        action_logger.debug(f"Renamed {asset} to {new_name}")
                    except PermissionError as e:
                        action_logger.error(f"Permission denied while renaming {asset} to {new_name}: {e}")
                elif os.path.exists(asset + ".disabled"):
                    new_name = asset
                    try:
                        os.rename(asset + ".disabled", new_name)
                        action_logger.debug(f"Renamed {asset + '.disabled'} to {new_name}")
                    except PermissionError as e:
                        action_logger.error(f"Permission denied while renaming {asset + '.disabled'} to {new_name}: {e}")
                else:
                    action_logger.error(f"While running {action_file}, file not found: {asset}")

    def execute_rewrite(self, action, action_file):
        prefix = action.get("prefix", "")
        assets = [prefix + asset for asset in action.get("assets", [])]
        data = action.get("data", "")
        if isinstance(data, list):
            data = "\n".join(data)
        action_logger.debug(f"Rewriting assets: {assets} with data: {data}")
        for asset in assets:
            try:
                with open(asset, "w", encoding="utf-8") as file:
                    file.write(data)
                action_logger.debug(f"While running {action_file}, rewrote {asset}")
            except PermissionError as e:
                action_logger.error(f"Permission denied while rewriting {asset}: {e}")

    def execute_log(self, action, action_file):
        level = action.get("level", "info").lower()
        msg = action.get("msg", "")
        if isinstance(msg, list):
            msg = "\n".join(msg)
        action_logger.debug(f"Logging message at level {level}: {msg}")
        if level == "debug":
            action_logger.debug(msg)
        elif level == "info":
            action_logger.info(msg)
        elif level == "warning":
            action_logger.warning(msg)
        elif level == "error":
            action_logger.error(msg)
        elif level == "critical":
            action_logger.critical(msg)
        else:
            action_logger.error(f"Unknown log level in {action_file}: {level}")

    def execute_msgbox(self, action, action_file):
        level = action.get("level", "info").lower()
        msg = action.get("msg", "")
        if isinstance(msg, list):
            msg = "\n".join(msg)
        action_logger.debug(f"Showing message box at level {level}: {msg}")
        if level == "info":
            QtWidgets.QMessageBox.information(None, "Info", msg)
        elif level == "warning":
            QtWidgets.QMessageBox.warning(None, "Warning", msg)
        elif level == "error":
            QtWidgets.QMessageBox.critical(None, "Error", msg)
        else:
            action_logger.error(f"Unknown message box level in {action_file}: {level}")

    def execute_run(self, action, action_file):
        for sub_action_file in action.get("action", []):
            sub_action_path = os.path.join(self.settings["assets"], "disable_helper", "action", sub_action_file)
            action_logger.debug(f"Running sub-action file: {sub_action_file}")
            if os.path.exists(sub_action_path):
                sub_actions = self.load_action_file(sub_action_file)
                if not isinstance(sub_actions, list):
                    action_logger.error(f"Action file {sub_action_file} does not contain a list.")
                    continue
                for sub_action in sub_actions:
                    if isinstance(sub_action, dict):
                        self.execute_action(sub_action, sub_action_file)
                    else:
                        action_logger.error(f"Invalid sub-action format in {sub_action_file}: {sub_action}")
                action_logger.debug(f"Action {sub_action_file} executed successfully.")
            else:
                action_logger.error(f"While running {action_file}, action file not found: {sub_action_path}")
