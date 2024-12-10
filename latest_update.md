禁用助手配置文件
- 更改了默认文字
- 默认配置文件重命名为`disable_helper_config.json`
- 更改了`display`中`text`的逻辑
- 重命名了一些键
  - `source`键重命名为`assets`
  - `actions`键重命名为`action`
- 移除了一些键
  - 移除了`target`键
  - 移除了`gui_mode`键
  - 移除了`display`中的`auto_next_line`键，并
  - 移除了一些报错(可能会加回来)

禁用助手
- 未完成: 重写了代码 ~~(OOP - orz)~~
- 未完成: 当找不到配置文件时，会从同级目录的`pack.mcmeta`的`disable_helper_config_name`键的值查找配置文件名，如果没有再生成默认
  - ~~人话：可以自定义配置文件名~~
