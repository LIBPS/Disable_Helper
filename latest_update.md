禁用助手配置文件
- 更改了默认主界面
- 默认配置文件重命名为`disable_helper_config.json`
- 文件操作中的`code`,`files`,`source`键重命名为`assets`，移除了`target`键
- `actions`键重命名为`action`
- 移除了`settings`中的`gui_mode`键
- 移除了`display`中的`auto_next_line`键，并更改了`display`中`text`的逻辑

禁用助手
- 未完成: 重写了代码 ~~(OOP - orz)~~
- 未完成: 当找不到配置文件时，会从同级目录的`pack.mcmeta`的`disable_helper_config_name`键的值查找配置文件名，如果没有再生成默认
  - ~~人话：可以自定义配置文件名~~