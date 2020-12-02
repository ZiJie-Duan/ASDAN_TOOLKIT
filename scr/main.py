#ASDAN 商赛辅助分析程序
from core import CORE_CONTROL
import traceback

def helper():
    print("""

ASDAN 商赛辅助程序 使用教程
    EX：[/parameter] 方框内带有左斜线的参数，是可选填参数

程序内部控制：
    initmemory [/type] ---- 清除指定程序内存
        如不传入参数，将自动清除全部内存。
        type包含由["path","data","period","variate"]

    rd_d [/path] ------ 指定读取数据文件（json文件）
        path 为json的绝对路径，包含文件名称以及后缀
        如不填写参数，将在相对目录下读取 data.json
    
    sv_d [/path] ------ 指定保存数据文件（json文件）
        path 为json的绝对路径，包含文件名称以及后缀
        如不填写参数，将在相对目录下保存 data.json

    memo [schema] [name] ---- 操作程序内部存储器 memo
        memo 可以将程序最后一次运算/表格样式渲染的数据保存下来
        schema 操作模式，具有 ["add","del"] 两种模式
        name 为保存的名称，添加模式时，将由此name作为数据结构的键
        删除模式时，将删除由此名称组成的数据结构
    
    ls_memory [schema] [/type] ------ 输出程序内部数据
        schema 操作模式 具有 ["general","detail"] 两种运行模式
        type 为指定的变量，包含由["path","data","period","variate"]
        默认全选



    """)

def cmd_control(cmd,cmdlist,core):
    core.cmdlist = cmdlist
    if cmd == "-h":
        helper()
    if cmd == "initmemory":
        core.init_memory()

    if cmd == "rd_d":
        core.load_data()

    if cmd == "sv_d":
        core.save_data()
    
    if cmd == "memo":
        core.memo()
    
    if cmd == "ls_memory":
        core.list_memory()

    if cmd == "set_p":
        core.set_period()

    if cmd == "TRA":
        core.read_table()

    if cmd == "initdata":
        core.init_data_structure()
    
    if cmd == "ANA":
        core.analyzer()

    if cmd == "TSR":
        core.table_style_rendering()


def main():
    print("ASDAN 商赛辅助分析程序 v1.0 beta")
    print("作者：Peter Duan")
    core = CORE_CONTROL()
    '''
    while True:
        user_cmd = input(">>")
        user_cmd_list = user_cmd.split(" ")
        cmd = user_cmd_list[0]
        if len(user_cmd_list) < 2:
            cmdlist = []
        else:
            cmdlist = user_cmd_list[1:]
        cmd_control(cmd,cmdlist,core)
        print("finish")
    '''
    
    while True:
        try:
            user_cmd = input(">>")
            user_cmd_list = user_cmd.split(" ")
            cmd = user_cmd_list[0]
            if len(user_cmd_list) < 2:
                cmdlist = []
            else:
                cmdlist = user_cmd_list[1:]
            cmd_control(cmd,cmdlist,core)
        except:
            traceback.print_exc()#错误捕捉器
        print("finish")

main()