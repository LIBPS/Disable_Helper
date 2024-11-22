# 禁用助手 - 使用说明
### 简体中文（中国大陆） 原文版本
**"\\"开始为注释**

**"."开始为直接输出**

**最后一个"."为读取输入，"." 前面的数字为设置颜色或设置样式**

**输入"\$"前的内容进行操作，操作"\$"后的文件**

**"$"后的文件下一行以"^"开头表示同时操作的文件**

**"+"可以设置目录前 缀，如果"+"后为空那么清空前缀**
	
**优先级 "\\" > "."(普通输出) > "+" > "$" > "^" > "."(设置颜色)**

**第一次运行时报毒&卡顿是正常现象**

**软件如果发生闪退时，请提交 Issues**

**LIB 临时工作室 - Cbscfe[Lucas] 制作**

**程序出现问题 （如修改配置文件）需提交 Issues**

感谢 **@槑头脑**提供的破损工具文件名和程序架构最初设想

**做GUI之前永远Beta！[ 你们这些（一个一个的）不会用tkinter的人 ]**

### 配置文件如下所示：
~~~
+assets\minecraft\models\item\
	1 $ mace.json

+assets\minecraft\blockstates\
	2 $ podzol.json
		^dirt_path.json
		^grass_block.json
		^mycelium.json

+assets\minecraft\blockstates\
	3 $ dead_bush.json
	+assets\minecraft\models\block\
		^dead_bush1.json
		^dead_bush2.json
		^dead_bush3.json

+assets\minecraft\models\item\
	4 $ bow.json
		^bow0.json
		^bow_pulling0_0.json
		^bow_pulling0_1.json
		^bow_pulling0_2.json
		^bow_pulling_0.json
		^bow_pulling_1.json
		^bow_pulling_2.json
		^carrot_on_a_stick.json
		^carrot_on_a_stick0.json
		^diamond_axe.json
		^diamond_axe0.json
		^golden_axe.json
		^golden_axe0.json
		^iron_axe.json
		^iron_axe0.json
		^netherite_axe.json
		^netherite_axe0.json
		^stone_axe.json
		^stone_axe0.json
		^wooden_axe.json
		^wooden_axe0.json
		^diamond_hoe.json
		^diamond_hoe0.json
		^golden_hoe.json
		^golden_hoe0.json
		^iron_hoe.json
		^iron_hoe0.json
		^netherite_hoe.json
		^netherite_hoe0.json
		^stone_hoe.json
		^stone_hoe0.json
		^wooden_hoe.json
		^wooden_hoe0.json
		^diamond_pickaxe.json
		^diamond_pickaxe0.json
		^golden_pickaxe.json
		^golden_pickaxe0.json
		^iron_pickaxe.json
		^iron_pickaxe0.json
		^netherite_pickaxe.json
		^netherite_pickaxe0.json
		^stone_pickaxe.json
		^stone_pickaxe0.json
		^wooden_pickaxe.json
		^wooden_pickaxe0.json
		^diamond_shovel.json
		^diamond_shovel0.json
		^golden_shovel.json
		^golden_shovel0.json
		^iron_shovel.json
		^iron_shovel0.json
		^netherite_shovel.json
		^netherite_shovel0.json
		^stone_shovel.json
		^stone_shovel0.json
		^wooden_shovel.json
		^wooden_shovel0.json
		^diamond_sword.json
		^diamond_sword0.json
		^golden_sword.json
		^golden_sword0.json
		^iron_sword.json
		^iron_sword0.json
		^netherite_sword.json
		^netherite_sword0.json
		^stone_sword.json
		^stone_sword0.json
		^wooden_sword.json
		^wooden_sword0.json
		^fishing_rod.json
		^fishing_rod0.json
		^fishing_rod_cast.json
		^fishing_rod_cast0.json
		^flint_and_steel.json
		^flint_and_steel0.json
		^shears.json
		^shears0.json
		^warped_fungus_on_a_stick.json
		^warped_fungus_on_a_stick0.json

+assets\minecraft\optifine\cit\guangyixiangduilun\
	5 $ guangyixiangduilun.properties

+assets\minecraft\optifine\cit\
	6 $ suspicious_stew\new
		^potions\new1
		^potions\new2
		^potions\new3
		^painting\new
~~~

#### 95.禁用助手 Beta 2.2.1 - LIB 临时工作室出品

.---------------------------------

.使用方法

.- 输入功能 前面的数字然后按回车

.---------------------------------

.功能列表:

.1	开关重锤

.2	开关泥土类

.3	开关枯木白骨

.4	开关工具与武器破损

.5	开关魔法护盾

.6	Forge CIT!?

.---------------------------------

.选择功能:
