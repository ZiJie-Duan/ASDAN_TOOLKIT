#ASDAN 商赛辅助分析程序
from core import CORE_CONTROL
import traceback
import sys

def helper():
    print("""

ASDAN_ToolKit V2.0 使用教程
    "作者：Lucycore"
    Eg：[/parameter] 方框内带有左斜线的参数，是可选填参数

程序内部控制：
    im [/type] ---- 清除指定程序内存
        如不传入参数，将自动清除全部内存。
        type包含由["path","data","period","variate"]

    red [/path] ------ 指定读取数据文件（json文件）
        path 为json的绝对路径，包含文件名称以及后缀
        如不填写参数，将在相对目录下读取 data.json
    
    svd [/path] ------ 指定保存数据文件（json文件）
        path 为json的绝对路径，包含文件名称以及后缀
        如不填写参数，将在相对目录下保存 data.json

    memo [schema] [name] ---- 操作程序内部存储器 memo
        memo 可以将程序最后一次运算/表格样式渲染的数据保存下来
        schema 操作模式，具有 ["add","del"] 两种模式
        name 为保存的名称，添加模式时，将由此name作为数据结构的键
        删除模式时，将删除由此名称组成的数据结构
    
    lsm [schema] [/type] ------ 输出程序内部数据
        schema 操作模式 具有["g","d"] #general,detail 两种运行模式
        type 为指定的变量，包含由["path","data","period","variate"]
        默认全选

    setp [period] ------ 用于设置程序时间（游戏周期）的函数
        period 为一个数字

    initd ------- 根据周期生成数据结构

    TRA [path] [translator] ------- 通过路径加载数据表
        path 为数据表的绝对路径，包含文件的后缀
        translator 为读取数据表所指定的数据加载器（翻译器）
    
    ANA [analyzer] ------- 对数据执行算法操作
        analyzer 为指定的算法

    TSR [rendering] ------- 使用表格渲染器对数据进行处理
        rendering 为指定的渲染器

    ct [path] [/memo]------- 生成报表
        path 为指定文件的生成路径
        memo 只有 memo一个值，加入即可选择内存中的其他结果

    """)

def cmd_control(cmd,cmdlist,core):
    core.cmdlist = cmdlist
    if cmd == "-h":
        print("运行 帮助")
        helper()
    elif cmd == "im":
        print("运行 初始化记忆")
        core.init_memory()

    elif cmd == "red":
        print("运行 读取数据")
        core.load_data()

    elif cmd == "svd":
        print("运行 保存数据")
        core.save_data()
    
    elif cmd == "memo":
        print("运行 运行memo记忆")
        core.memo()
    
    elif cmd == "lsm":
        print("运行 memory查看器")
        core.list_memory()

    elif cmd == "setp":
        print("运行 周期设置函数")
        core.set_period()

    elif cmd == "TRA":
        print("运行 TRA 表格加载器")
        core.read_table()

    elif cmd == "initd":
        print("运行 初始化数据结构函数")
        core.init_data_structure()
    
    elif cmd == "ANA":
        print("运行 ANA 核心算法")
        core.analyzer()

    elif cmd == "TSR":
        print("运行 TSR 表格样式渲染器")
        core.table_style_rendering()

    elif cmd == "ct":
        print("运行 表格导出程序")
        core.table_writer()
    
    else:
        if cmd != "":
            print("命令无效")


def main():
    print("ASDAN 商赛辅助分析程序 v1.0 Beta")
    print("初始化核心")
    core = CORE_CONTROL()
    if core.start_verify() == False:
        print("按下回车退出程序")
        sys.exit()

    print("进入cmd 控制循环")
    while True:
        try:
            user_cmd = input(">>")
            if user_cmd == "q":
                print("程序退出！")
                break
            user_cmd_list = user_cmd.split(" ")
            cmd = user_cmd_list[0]
            if len(user_cmd_list) < 2:
                cmdlist = []
            else:
                cmdlist = user_cmd_list[1:]
            cmd_control(cmd,cmdlist,core)
        except:
            print("\n程序发生致命错误！")
            traceback.print_exc()#错误捕捉器
            print("按下回车继续")


main()