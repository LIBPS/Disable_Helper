import sys
import logging
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout, QLabel, QListWidget, QPushButton
from config import Config, logger

VERSION = "v4.0.1-beta"
SETTINGS_FILE = "disable_helper_settings.json"

class App(QtWidgets.QWidget):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.language_data = config.language_data
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.language_data["window_title"].format(version=VERSION))
        self.setGeometry(400, 400, 650, 425)

        layout = QVBoxLayout()

        display_text = "\n".join([line.format(version=VERSION) for line in self.language_data["display"]])
        label = QLabel(display_text)
        label.setAlignment(QtCore.Qt.AlignLeft)
        label.setFont(QtGui.QFont("Consolas", 10))
        layout.addWidget(label)

        self.action_listbox = QListWidget()
        self.action_listbox.setFont(QtGui.QFont("Consolas", 10))
        layout.addWidget(self.action_listbox)

        action_files = self.config.get_action_files()
        for action_file in action_files:
            self.action_listbox.addItem(action_file)

        run_button = QPushButton(self.language_data["button_run_action"])
        run_button.setFont(QtGui.QFont("Consolas", 10))
        run_button.clicked.connect(self.run_selected_action)
        layout.addWidget(run_button)

        self.setLayout(layout)

    def run_selected_action(self):
        selected_action = self.action_listbox.currentItem().text() + ".json"
        if selected_action:
            try:
                actions = self.config.load_action_file(selected_action)
                if not isinstance(actions, list):
                    raise ValueError(f"Action file {selected_action} does not contain a list.")
                for action in actions:
                    if isinstance(action, dict):
                        self.config.execute_action(action, selected_action)
                logger.info(f"Action {selected_action} executed successfully.")
                if self.config.settings["msgbox_action_done"]:
                    QMessageBox.information(self, "Info", self.language_data["msgbox_action_done_message"].format(action=selected_action))
            except Exception as e:
                logger.error(f"Error executing action {selected_action}: {e}")
                QMessageBox.critical(self, "Error", f"An error occurred while executing the action: {e}")
        else:
            logger.warning("No action selected.")

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
    main_app = App(config)
    main_app.show()
    sys.exit(app.exec_())