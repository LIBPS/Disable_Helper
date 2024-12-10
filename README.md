# 禁用助手 - LIB 临时工作室

[简体中文](README.md) | [繁体中文](docs/README_zh-TC.md) | [ENGLISH](docs/README_EN.md)

## 介绍
材质包作者也可以将该脚本直接内置到材质包内，这样就可以省去维护“附加包”、“附减包”之类的麻烦了。

**目前仍在测试阶段，经常大改**\
不建议下载代码，可以使用[Releases](https://github.com/LIBPS/Disable_Helper/releases)

## 特点

- **简易操作**：无需掌握编程，仅需基本的材质包知识。
- **高扩展性**：支持多种操作类型，如复制、删除、禁用、以及代码执行（需要 Python 支持）。
- **可自定义配置**：配置文件采用 JSON 格式，易于编辑和扩展。	

---

## 使用方法
1. 将禁用助手脚本和配置文件添加到你的材质包文件夹中。
2. 编辑配置文件，根据需求定义需要管理的资源。
3. 运行脚本并选择操作
4. 根据提示输入功能以完成相应操作。

## v3.4-beta+ 配置文件结构:

- display: 主界面
  - color: 一个字符串，控制颜色，效果同batch的`color`。可选
  - text: 真正显示的内容。为一个数组或字符串，如果为数组则在除了最后一项的每一项后加入`"\n"`。可以使用`{%s}`显示禁用助手的版本
- action: 操作
  - action_name: 要在输入action_name时执行的东西
    - end_output: action_name执行完成后的输出。可选
    - action: 执行的东西。一个数组，其中每一项均为一个字典
        - type: 操作类型。`copy`、`delete`、`disable`、`execute`(仅安装python可用)
        - prefix: 为`assets`每一项加上`prefix`。可选
        - assets: 一个列表，目前在此不做说明
- lang: 文字
  - language: 语言，目前在此不做说明
- settings: 设置(目前没啥用)
  - debug_mode：调试模式(目前没啥用)
  - language：在`lang`中调用的键名
  - confirm_execute_code：是否在执行`execute`操作前确认(目前没啥用)
  - confirm_file_delete 是否在执行`delete`操作前确(目前没啥用)

## 待办

- [ ] 完整的说明文档
- [ ] 更好的默认配置文件
- [ ] GUI界面
- [ ] 使用§控制颜色及样式
- [x] 不超过5个的待办

### 友链

[Immortal-Sty](https://github.com/Immortal-Sty)制作的[MC_resourcepacks_delHelper](https://github.com/Immortal-Sty/MC_resourcepacks_delHelper "一个v1.0-beta的改版")

##### 最近更新:24/12/7
