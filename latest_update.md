初始化并记录所有配置文件顺序如下：
如果相同目录的 `disable_helper_settings.json` 存在且存在
则用它覆盖 `DEFAULT_SETTINGS` 并记录在日志。
然后根据 settings 读取 
`settings["assets"]/disable_helper/lang` 的 `settings["language"].json`。如果不存在则记录在日志并关闭。
然后读取 `settings["assets"]/disable_helper/action` 的所有 json 文件，并与内容记录在日志。

action 目录下每一个`.json`文件装有一个列表, 装有字典(下称为"操作")

对于所有跟文件有关的都会有 `"assets"` `"prefix"` 会为每个 `"assets"` 加上 `"prefix"`
如: `"assets": ["qwq.md"]` `"prefix": "awa"` 那么 `[awaqwq.md]`

`"assets"` 为一个列表 装有文件目录
`"prefix"` 为一个字符串

`"type"` 为类型

- check
```json
{
    "type": "check",
    "prefix": <prefix>,
    "assets": <files>,
    "true": <action>,
    "false": <action>
}
```
如果每一个 `<files>` 存在那么执行 `"true"`
否则执行 `"false"`

`<action>` 是一个由若干操作组成的列表

- copy
```json
{
    "type": "copy",
    "prefix": <prefix>,
    "assets": <files>,
    "target": <folder>
}
```
吧每一个 `<files>` 粘贴到 `<folder>`

- delete
```json
{
    "type": "delete",
    "prefix": <prefix>,
    "assets": <files>
}
```
删除所有 `<files>`

- rename
```json
{
    "type": "rename",
    "prefix": <prefix>,
    "assets": <files>,
    "sync": <bool>
}
```
为所有 `<files>` 
如果这个文件存在 则在文件名后加上 ".disabled"
否则如果这个文件加上".disabled"存在 则在文件名后去掉 ".disabled"

如果 `"sync"` 为 `true`
那么执行时只能执行第一个文件所执行的

- rewrite
```json
{
    "type": "rewrite",
    "prefix": <prefix>,
    "assets": <files>,
    "data": <data>
}
```
`<data>` 为一个字符串或列表
如果为列表那么在列表每一项之间加入`\n`拼接为一个字符串

用 `<data>` 覆盖每一个 `<files>`

- log
```json
{
    "type": "log",
    "level": "debug"|"info"|"warning"|"error"|"critical",
    "msg": <data>
}
```
`<data>` 为一个字符串或列表
如果为列表那么在列表每一项之间加入`\n`拼接为一个字符串

`"level"` 等级

在日志里写入 `"level"` 级的 `<data>`

- msgbox
```json
{
    "type": "msgbox",
    "level": "info"|"warning"|"error",
    "msg": <data>
}
```
`<data>` 为一个字符串或列表
如果为列表那么在列表每一项之间加入`\n`拼接为一个字符串

`"level"` 等级
弹窗 `"level"` 级的 `<data>`



- run
```json
{
    "type": "log",
    "action": <action>
}
```
`<action>` 为一个列表, 装有操作的文件名