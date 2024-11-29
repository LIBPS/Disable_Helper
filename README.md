# 禁用助手 - 使用说明

## 使用说明
  pass

## v3.3.3-beta+ 配置文件结构:

- display: 主界面
  - color: 一个字符串，控制颜色，效果同batch的`color `。可选
  - auto_next_line: 如果为真且`"text"`为数组那么在`"text"`每一项后加入`"\n"`。可选，默认否
  - text: 真正显示的内容。为一个数组或字符串。可以使用`"{version}"`显示禁用助手的版本
- actions: 操作
  - name : 要在输入name时执行的东西
    - end_output: name执行完成后的输出。可选
    - action: 执行的东西。一个数组，其中每一项均为一个字典
        - type: 操作类型。`copy`、`delete`、`disable`、`execute`(仅安装Python运行环境可用)
        - prefix: 为`files`每一项加上`prefix`
        - files: 一个列表
- lang: 文字
- settings: 设置(目前没啥用)
  - gui_mode: 没用。占位。可选
  - debug_mode：调试模式(在某些情况下引发崩溃)
  - language：在lang中调用的键名
  - confirm_execute_code：是否在执行`execute`操作前确认
  - confirm_file_delete 是否在执行`delete`操作前确认

## 待办

- [ ] 完整的说明文档
  - [x] 不完整的说明文档
- [ ] 更好的默认配置文件
  - [x] 默认配置文件
- [ ] 可自定义GUI界面
  - [ ] tkinter学习
  - [ ] 简易GUI界面
- [ ] 使用§控制颜色及样式
  - [ ] 可自定义GUI界面完成
  - [ ] ...
- [x] 不超过5个的待办

感谢[@槑头脑](https://github.com/Immortal-Sty)提出的程序架构[最初设想](https://github.com/Immortal-Sty/MC_resourcepacks_delHelper)
