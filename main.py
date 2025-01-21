import sys
from PyQt5 import QtWidgets
from config import Config
from ui import App
from logger import logger

VERSION = "v4.0.3-beta"
SETTINGS_FILE = "disable_helper_settings.json"

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    config = Config(SETTINGS_FILE)
    start_actions = config.load_action_file("__start__.json")
    if not isinstance(start_actions, list):
        logger.error(f"Action file __start__.json does not contain a list.")
    else:
        for action in start_actions:
            if isinstance(action, dict):
                config.execute_action(action, "__start__.json")
    logger.info("Action __start__.json executed successfully.")
    main_app = App(config, VERSION)
    main_app.show()
    sys.exit(app.exec_())
