# Disable_Helper - LIB Provisional Studio

[简体中文](../README.md) | [繁体中文](README_zh-CN.md) | [ENGLISH](README_EN.md)

## Introduction
Texture pack authors can also directly embed this script into their texture packs, which eliminates the hassle of maintaining "add-ons" and "subtraction packs".

**Currently in the testing phase, with frequent major changes**\
It is not recommended to download the code; instead, use the [Releases](https://github.com/LIBPS/Disable_Helper/releases) 

## Features

- **Easy Operation**: No programming knowledge is required, only basic texture pack knowledge is needed.
- **High Extensibility**: Supports various operation types, such as copy, delete, disable, and code execution (requires Python support).
- **Customizable Configuration**: The configuration file uses JSON format, which is easy to edit and extend.

---

## Usage
1. Add the Disable_Helper script and configuration file to your texture pack folder.
2. Edit the configuration file to define the resources you need to manage according to your requirements.
3. Run the script and select the operation.
4. Follow the prompts to input the function to complete the corresponding operation.

## v3.4-beta+ Configuration File Structure:

- display: Main interface
  - color: A string that controls the color, with the same effect as `color` in batch. Optional.
  - text: The actual content displayed. It can be an array or a string; if it's an array, add `"\n"` after each item except the last one. You can use `{%s}` to display the version of Disable_Helper.
- action: Operations
  - action_name: What to execute when inputting action_name
    - end_output: The output after action_name is executed. Optional.
    - action: What to execute. An array where each item is a dictionary
        - type: The type of operation. `copy`, `delete`, `disable`, `execute` (only available if Python is installed)
        - prefix: Add `prefix` to each item of `assets`. Optional.
        - assets: A list, which is not explained here at the moment.
- lang: Text
  - language: The language, which is not explained here at the moment.
- settings: Settings (currently not very useful)
  - debug_mode: Debug mode (may cause crashes in certain situations)
  - language: The key name called in `lang`
  - confirm_execute_code: Whether to confirm before executing `execute` operations
  - confirm_file_delete: Whether to confirm before executing `delete` operations

## To-Do

- [ ] Complete documentation
- [ ] Better default configuration files
- [ ] GUI interface
- [ ] Use § to control color and style
- [x] No more than 5 to-dos

## Versioning

+1		A major update that is obvious without looking at the code
+0.1	A major update that is only obvious when looking at the code
+0.0.1	An update to show that the author is still updating

-beta	In testing
-dev	May not run but was accidentally published

### Friends Links

[MC_resourcepacks_delHelper](https://github.com/Immortal-Sty/MC_resourcepacks_delHelper "A v1.0-beta revision") made by [Immortal-Sty](https://github.com/Immortal-Sty)

##### Last Update: 24/12/7
