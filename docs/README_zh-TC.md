# 禁用助手 - LIB 臨時工作室


[简体中文](../README.md) | [繁体中文](README_zh-CN.md) | [ENGLISH](README_EN.md)

## 介紹
材質包作者也可以將該腳本直接內置到材質包內，這樣就可以省去維護“附加包”、“附減包”之類的麻煩了。

**目前仍在測試階段，經常大改**\
不建議下載代碼，可以使用[Releases](https://github.com/LIBPS/Disable_Helper/releases)

## 特點

- **簡易操作**：無需掌握編程，僅需基本的材質包知識。
- **高擴展性**：支持多種操作類型，如複製、刪除、禁用、以及代碼執行（需要 Python 支持）。
- **可自定義配置**：配置文件採用 JSON 格式，易於編輯和擴展。	

---

## 使用方法
1. 將禁用助手腳本和配置文件添加到你的材質包文件夾中。
2. 編輯配置文件，根據需求定義需要管理的資源。
3. 運行腳本並選擇操作
4. 根據提示輸入功能以完成相應操作。

## v3.4-beta+ 配置文件結構:

- display: 主界面
  - color: 一個字符串，控制顏色，效果同batch的`color`。可選
  - text: 真正顯示的內容。為一個數組或字符串，如果為數組則在除了最後一項的每一項後加入`"\n"`。可以使用`{%s}`顯示禁用助手的版本
- action: 操作
  - action_name: 要在輸入action_name時執行的東西
    - end_output: action_name執行完成後的輸出。可選
    - action: 執行的東西。一個數組，其中每一項均為一個字典
        - type: 操作類型。`copy`、`delete`、`disable`、`execute`(僅安裝python可用)
        - prefix: 為`assets`每一項加上`prefix`。可選
        - assets: 一個列表，目前在此不做説明
- lang: 文字
  - language: 語言，目前在此不做説明
- settings: 設置(目前沒啥用)
  - debug_mode：調試模式(在某些情況下引發崩潰)
  - language：在`lang`中調用的鍵名
  - confirm_execute_code：是否在執行`execute`操作前確認
  - confirm_file_delete 是否在執行`delete`操作前確

## 待辦

- [ ] 完整的説明文檔
- [ ] 更好的默認配置文件
- [ ] GUI界面
- [ ] 使用§控制顏色及樣式
- [x] 不超過5個的待辦

## 版本

+1		不看代碼就看的出來的大更新
+0.1	看代碼才看的出來的大更新
+0.0.1	用來看作者還在更新的更新

-beta	測試中
-dev	可能無法運行但不小心發上去了

### 友鏈

[Immortal-Sty](https://github.com/Immortal-Sty)製作的[MC_resourcepacks_delHelper](https://github.com/Immortal-Sty/MC_resourcepacks_delHelper "一個v1.0-beta的改版")

##### 最近更新:24/12/9