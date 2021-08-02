#ASDAN 商赛辅助分析程序
from core import CORE_DRIVE
import traceback

'''
1，分析器 加入数据选择功能
2，完善 写入表格 数据类型
3，加入表格读取 类型检测器
4, 加入缓存时间刷新显示
'''

def helper():
    print("""

    ASDAN_ToolKit V2.0 使用教程

    "Author：Lucycore"
    目前程序简化了大多数功能
    加入了更加智能快速的读表器
    于此同时　优化了数据结构

    -h -------------- 展示程序帮助
    load [path] ----- 读取已保存的数据（绝对路径）
    save [path] ----- 保存程序内存数据（绝对路径）
    memo ------------ 展示程序内存信息

    rd [path] ------- 读取ASDAN商赛报表（xls格式）
    ana ------------- 分析商赛原始数据
    wt [path] ------- 写入到excel表格中（xls格式）

    tf [group] [name] 从临时数据中转移数据至指定的组别
        group 具有两个值，分别对应memo中两个不同的数据结构
        "p" —— processed_data，"g" —— graphical_data

    tf [group] [name] [new_group] [new_name]
        将数据进行内部转移，在两个数据结构中相互转换
        group 和 new_group 可以是相同的，这样数据将进行复制
        但 name 不可重复

    del [group] [name] 删除指定组中的数据
        group 具有四个值，分别对应memo中两个不同的数据结构
        "p" —— processed_data，"g" —— graphical_data
        "o" —— original data， "t" —— temporary_data
        
    change_period [period] 修改周期至指定周期
    此命令将自动创建相对应的周期数据结构

    """)

def cmd_control(cmd,cmdlist,core):
    core.cmdlist = cmdlist
    if cmd == "-h":
        print("运行 帮助")
        helper()

    elif cmd == "load":
        core.load_data()

    elif cmd == "save":
        core.save_data()
    
    elif cmd == "memo":
        core.show_memory()

    elif cmd == "rd":
        core.load_table()
    
    elif cmd == "ana":
        core.analyze_data_normal()

    elif cmd == "wt":
        core.write_table()

    elif cmd == "tf":
        core.transfer_data()

    elif cmd == "del":
        core.del_data()
    
    elif cmd == "change_period":
        core.change_period()
    
    else:
        if cmd != "":
            print("命令无效")


def main():
    print("ASDAN 商赛辅助分析程序 v2.0 Beta")
    print("初始化核心")
    core = CORE_DRIVE()

    print("进入cmd 控制循环")
    while True:
        try:
            user_cmd = input(">>")
            if user_cmd == "q":
                print("程序退出！")
                break
            cmd_list = user_cmd.split("@")
            cmd = cmd_list[0]
            cmd_list = cmd_list[1:]
            cmd_control(cmd,cmd_list,core)
        except:
            print("\n程序发生致命错误！")
            traceback.print_exc()#错误捕捉器
            print("按下回车继续")


main()