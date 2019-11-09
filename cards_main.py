#TODO(ic3evi1) 名片管理系统【练习版】
import cards_tools
#主程序无限循环，用户输入0时，执行退出
while True:
    #TODO(ic3evi1) 显示功能选项
    cards_tools.show_menu()
    action_str = input("请选择操作功能：")
    print("您选择的功能是：%s " % action_str)

    #TODO(ic3evi1) 针对 1、2、3输入的操作功能
    if action_str in ["1","2","3"]:
        #代码未完成，用pass站位保证程序能够运行
        # 1.新建名片
        if action_str == "1":
            cards_tools.new_card()
        # 2.显示全部
        elif action_str == "2":
            cards_tools.show_all()
        # 3.查询名片
        else:
            cards_tools.search_card()

    #TODO(ic3evi1) 用户输入0，退出程序
    elif action_str == "0":
        print("欢迎下次使用[名片管理系统]！")
        break

    #其他用户输入，提示输入错误
    else:
        print("输入错误，请继续输入...")
