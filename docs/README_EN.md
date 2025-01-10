# Warning! This README is outdated!

# Disable Helper

Disable Helper is a Python application that helps manage and execute various actions based on configuration files. It uses `tkinter` for the GUI and supports actions like checking file existence, logging messages, copying files, and displaying message boxes.

## Features

- Load configuration from `disable_helper_settings.json` and `pack.mcmeta`.
- Execute actions defined in JSON files located in the `disable_helper/action` directory.
- Supported actions:
  - `check`: Check if files exist and execute corresponding actions.
  - `log`: Log messages at different levels.
  - `copy`: Copy files to a target directory.
  - `msgbox`: Display message boxes with different levels.

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/yourusername/disable_helper.git
   cd disable_helper
   ```

## Usage

1. Create a configuration file named [disable_helper_settings.json](http://_vscodecontentref_/1) in the same directory as the script. Example:

   ```json
   {
       "assets": "./assets",
       "debug_mode": true,
       "language": "zh_cn",
       "confirm_file_delete": false,
       "msgbox_action_done": true
   }
   ```
2. Create a language file in the [lang](http://_vscodecontentref_/2) directory. Example (`zh_cn.json`):

   ```json
   {
       "window_title": "Disable Helper {version}",
       "display": [
           "Welcome to Disable Helper {version}!",
           "---------------------------------",
           "Please select an action to run."
       ]
   }
   ```
3. Create action files in the [action](http://_vscodecontentref_/3) directory. Example (`__start__.json`):

   ```json
   [
       {
           "type": "check",
           "prefix": "awa",
           "assets": ["qwq.md", "example.txt"],
           "true": [
               {
                   "type": "log",
                   "level": "info",
                   "msg": "All files exist."
               },
               {
                   "type": "copy",
                   "prefix": "awa",
                   "assets": ["qwq.md", "example.txt"],
                   "target": "backup/"
               },
               {
                   "type": "msgbox",
                   "level": "info",
                   "msg": "All files exist and have been copied to the backup directory."
               }
           ],
           "false": [
               {
                   "type": "log",
                   "level": "error",
                   "msg": "One or more files are missing."
               },
               {
                   "type": "msgbox",
                   "level": "error",
                   "msg": "One or more files are missing."
               }
           ]
       },
       {
           "type": "log",
           "level": "info",
           "msg": "Action file executed successfully."
       }
   ]
   ```
4. Run the application:

   ```sh
   python disable_helper.py
   ```

## Logging

The application logs messages to [disable_helper.log](http://_vscodecontentref_/4). The log file is cleared each time the application starts.

## License

This project is licensed under the MIT License. See the [LICENSE](http://_vscodecontentref_/5) file for details.
