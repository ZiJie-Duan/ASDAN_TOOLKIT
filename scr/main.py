#ASDAN 商赛辅助分析程序
from core import CORE_CONTROL
import traceback

def cmd_control(cmd,cmdlist,core):
    core.cmdlist = cmdlist
    if cmd == "-h":
        print("""
        ASDAN 商赛辅助程序
            
            """)
    if cmd == "initmemory":
        core.init_memory()
    if cmd == "rd_d":
        core.load_data()
    if cmd == "sv_d":
        core.save_data()
    if cmd == "TRA":
        core.read_table()
    if cmd == "initdata":
        core.init_data_structure()

def main():
    print("ASDAN 商赛辅助分析程序 v1.0 beta")
    core = CORE_CONTROL()
    while True:

        user_cmd = input(">>")
        user_cmd_list = user_cmd.split(" ")
        cmd = user_cmd_list[0]
        if len(user_cmd_list) < 2:
            cmdlist = []
        else:
            cmdlist = user_cmd_list[1:]
        cmd_control(cmd,cmdlist,core)

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
    '''

main()