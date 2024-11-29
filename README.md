# 禁用助手 - 使用说明

## 使用说明
  pass

## v3.3.3-beta+ 配置文件结构:

- display: 主界面
  - color: 一个字符串，控制颜色，效果同batch的`color`。可选
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

### 历史

- [v1.0-beta][v1.0-beta] 在[梧桐加减法交流群](https://pd.qq.com/s/1d83nni17)提出并制作了此项目 ([1.0改版][MC_resourcepacks_delHelper])
- [v2.0-beta][v2.0-beta] 受到[MC_resourcepacks_delHelper][MC_resourcepacks_delHelper]的启发，使用了配置文件。编程语言从`batch`变为`python`
- [v3.0-beta][v3.0-beta] 配置文件从txt变为json格式

感谢[@槑头脑](https://github.com/Immortal-Sty)提出的程序架构最初设想

[v1.0-beta]: https://github.com/LIBPS/Disable_Helper "被作者不小心删了"
[v2.0-beta]: https://github.com/LIBPS/Disable_Helper/releases/tag/Beta "v2.0-beta项目链接"
[v3.0-beta]: https://github.com/LIBPS/Disable_Helper/releases/tag/v3.3.2-beta "v3.0-beta项目链接"

[MC_resourcepacks_delHelper]: https://github.com/Immortal-Sty/MC_resourcepacks_delHelper "一个v1.0-beta的改版"
