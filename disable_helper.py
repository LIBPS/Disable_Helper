import os

def clear_screen():
    """Clears the console screen."""
    os.system("cls")

def rename_file(old_name, new_name):
    """Renames a file and handles potential errors."""
    try:
        os.rename(old_name, new_name)
        print(f"\033[92m[提示] 已重命名项目至 {new_name}\033[0m")
    except FileNotFoundError:
        print(f"\033[91m[错误] 项目不存在: {old_name}\033[0m")
    except PermissionError:
        print(f"\033[91m[错误] 无法重命名项目，权限不足: {old_name}\033[0m")
    except Exception as e:
        print(f"\033[91m[错误] 未知错误: {e}\033[0m")

def create_default_config():
    """Creates a default configuration file if it doesn't exist."""
    config_content = ['\\\\\t\t\t\t\t使用说明\n', '\\\\\t"\\\\"开始为注释\n', '\\\\\t"."开始为直接输出\n', '\\\\\t最后一个"."为读取输入，"." 前面的数字为设置颜色或设置样式，如果要叠加设置用";"分隔\n', '\\\\\t输入"$"前的内容进行操作，操作"$"后的文件\n', '\\\\\t"$"后的文件下一行以"^"开头表示同时操作的文件\n', '\\\\\t"+"可以设置目录前 缀，如果"+"后为空那么清空前缀\n', '\\\\\t\n', '\\\\\t优先级 "\\\\" > "."(普通输出) > "+" > "$" > "^" > "."(设置颜色)\n', '\\\\\n', '\\\\\t第一次运行时报毒&卡顿是正常现象\n', '\\\\\t所有闪退均为bug\n', '\\\\\t如发现请在https://pd.qq.com/s/1d83nni17\n', '\\\\\t@指令小蛇_Cbscfe\n', '\\\\\t程序出现问题如修改配置文件需一并发送\n', '\\\\\n', '\\\\\t感谢@槑头脑提供的破损工具文件名和程序架构最初设想\n', '\\\\\n', '\\\\\t做GUI之前永远Beta!!!\n', '\\\\\t\t\t\t\t\t----(一个一个不会用tkinter的人)\n', '\n', '\n', '+assets\\minecraft\\models\\item\\\n', '\t1 $ mace.json\n', '\n', '+assets\\minecraft\\blockstates\\\n', '\t2 $ podzol.json\n', '\t\t^dirt_path.json\n', '\t\t^grass_block.json\n', '\t\t^mycelium.json\n', '\n', '+assets\\minecraft\\blockstates\\\n', '\t3 $ dead_bush.json\n', '\t+assets\\minecraft\\models\\block\\\n', '\t\t^dead_bush1.json\n', '\t\t^dead_bush2.json\n', '\t\t^dead_bush3.json\n', '\n', '+assets\\minecraft\\models\\item\\\n', '\t4 $ bow.json\n', '\t\t^bow0.json\n', '\t\t^bow_pulling0_0.json\n', '\t\t^bow_pulling0_1.json\n', '\t\t^bow_pulling0_2.json\n', '\t\t^bow_pulling_0.json\n', '\t\t^bow_pulling_1.json\n', '\t\t^bow_pulling_2.json\n', '\t\t^carrot_on_a_stick.json\n', '\t\t^carrot_on_a_stick0.json\n', '\t\t^diamond_axe.json\n', '\t\t^diamond_axe0.json\n', '\t\t^golden_axe.json\n', '\t\t^golden_axe0.json\n', '\t\t^iron_axe.json\n', '\t\t^iron_axe0.json\n', '\t\t^netherite_axe.json\n', '\t\t^netherite_axe0.json\n', '\t\t^stone_axe.json\n', '\t\t^stone_axe0.json\n', '\t\t^wooden_axe.json\n', '\t\t^wooden_axe0.json\n', '\t\t^diamond_hoe.json\n', '\t\t^diamond_hoe0.json\n', '\t\t^golden_hoe.json\n', '\t\t^golden_hoe0.json\n', '\t\t^iron_hoe.json\n', '\t\t^iron_hoe0.json\n', '\t\t^netherite_hoe.json\n', '\t\t^netherite_hoe0.json\n', '\t\t^stone_hoe.json\n', '\t\t^stone_hoe0.json\n', '\t\t^wooden_hoe.json\n', '\t\t^wooden_hoe0.json\n', '\t\t^diamond_pickaxe.json\n', '\t\t^diamond_pickaxe0.json\n', '\t\t^golden_pickaxe.json\n', '\t\t^golden_pickaxe0.json\n', '\t\t^iron_pickaxe.json\n', '\t\t^iron_pickaxe0.json\n', '\t\t^netherite_pickaxe.json\n', '\t\t^netherite_pickaxe0.json\n', '\t\t^stone_pickaxe.json\n', '\t\t^stone_pickaxe0.json\n', '\t\t^wooden_pickaxe.json\n', '\t\t^wooden_pickaxe0.json\n', '\t\t^diamond_shovel.json\n', '\t\t^diamond_shovel0.json\n', '\t\t^golden_shovel.json\n', '\t\t^golden_shovel0.json\n', '\t\t^iron_shovel.json\n', '\t\t^iron_shovel0.json\n', '\t\t^netherite_shovel.json\n', '\t\t^netherite_shovel0.json\n', '\t\t^stone_shovel.json\n', '\t\t^stone_shovel0.json\n', '\t\t^wooden_shovel.json\n', '\t\t^wooden_shovel0.json\n', '\t\t^diamond_sword.json\n', '\t\t^diamond_sword0.json\n', '\t\t^golden_sword.json\n', '\t\t^golden_sword0.json\n', '\t\t^iron_sword.json\n', '\t\t^iron_sword0.json\n', '\t\t^netherite_sword.json\n', '\t\t^netherite_sword0.json\n', '\t\t^stone_sword.json\n', '\t\t^stone_sword0.json\n', '\t\t^wooden_sword.json\n', '\t\t^wooden_sword0.json\n', '\t\t^fishing_rod.json\n', '\t\t^fishing_rod0.json\n', '\t\t^fishing_rod_cast.json\n', '\t\t^fishing_rod_cast0.json\n', '\t\t^flint_and_steel.json\n', '\t\t^flint_and_steel0.json\n', '\t\t^shears.json\n', '\t\t^shears0.json\n', '\t\t^warped_fungus_on_a_stick.json\n', '\t\t^warped_fungus_on_a_stick0.json   \n', '\n', '+assets\\minecraft\\optifine\\cit\\guangyixiangduilun\\\n', '\t5 $ guangyixiangduilun.properties\n', '\n', '+assets\\minecraft\\optifine\\cit\\\n', '\t6 $ suspicious_stew\\new\n', '\t\t^potions\\new1\n', '\t\t^potions\\new2\n', '\t\t^potions\\new3\n', '\t\t^painting\\new\n', '\n', '\n', '3;95.禁用助手 Beta 2.2.2 - LIB临时工作室出品\n', '95.---------------------------------\n', '.使用 方法\n', '.- 输入功能 前面的数字然后按回车\n', '.---------------------------------\n', '.功能列表:\n', '.1\t开关重锤\n', '.2\t开关泥土类\n', '.3\t开关枯木白骨\n', '.4\t开关工具与武器破损\n', '.5\t开关魔法护盾\n', '.6\tForge CIT!?\n', '.---------------------------------\n', '.选择功能:']
    try:
        with open("禁用助手配置文件.txt", "x", encoding="utf-8") as f:
            f.writelines(config_content)
    except FileExistsError:
        pass

def parse_config():
    """Parses the configuration file into a dictionary and a display list."""
    with open("禁用助手配置文件.txt", "r", encoding="utf-8") as f:
        raw_data = f.readlines()

    display_data = []
    file_data = {}
    current_key = None
    file_prefix = ""
    
    for line_num, line in enumerate(raw_data, start=1):
        line = line.strip()
        if not line or line.startswith("\\"):
            continue  # Skip empty or comment lines
        if line.startswith("."):
            display_data.append(line[1:] + "\n")
        elif line.startswith("+"):
            file_prefix = line[1:].strip()
        elif "$" in line:
            try:
                key, file = line.split("$", 1)
                key = key.strip()
                file = file_prefix + file.strip()
                if key not in file_data:
                    file_data[key] = []
                file_data[key].append(file)
                current_key = key
            except ValueError:
                raise ValueError(f"\033[91m[错误] 配置文件第{line_num}行格式错误: {line}\033[0m")
        elif line.startswith("^"):
            if not current_key:
                raise ValueError(f"\033[91m[错误] 配置文件第{line_num}行没有主键用于关联: {line}\033[0m")
            file = file_prefix + line[1:].strip()
            file_data[current_key].append(file)
        elif "." in line:
            display = line.split(".", 1)[1]
            color = line.split(".")[0]
            display_data.append(f"\033[{color}m{display}\n")
        else:
            raise ValueError(f"\033[91m[错误] 配置文件第{line_num}行无法识别: {line}\033[0m")

    return display_data, file_data

def main():
    """Main function to drive the program."""
    create_default_config()
    try:
        display_data, file_data = parse_config()
    except Exception as e:
        input(f"{e}")
        exit()

    input_prompt = display_data.pop(-1)[:-1]

    while True:
        clear_screen()
        for line in display_data:
            print(line, end="")
        user_input = input(input_prompt)
        enabled_files_cnt = 0
        disabled_files_cnt = 0

        if user_input in file_data:
            for file in file_data[user_input]:
                if os.path.exists(file) and enabled_files_cnt == 0:
                    rename_file(file, file + ".disabled")        
                    disabled_files_cnt += 1
                elif os.path.exists(file + ".disabled") and disabled_files_cnt == 0:
                    rename_file(file + ".disabled", file)
                    enabled_files_cnt += 1
                elif os.path.exists(file) or os.path.exists(file + ".disabled"):
                    print(f"\033[93m[提示] 略过了：{file}\033[0m")
                else:
                    print(f"\033[91m[错误] 项目不存在: {file}\033[0m")
            input(f"\033[92m[提示] 操作完成，启用了{enabled_files_cnt}个项目，禁用了{disabled_files_cnt}个项目。按回车继续...\033[0m")
        else:
            input("\033[93m[提示] 无效输入，请重试...\033[0m")

if __name__ == "__main__":
    main()
