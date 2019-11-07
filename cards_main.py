#TODO(ic3evi1) 名片管理系统【练习版】


action_str = input("请选择操作功能：")
print("您选择的功能是： %s " % action_str)

#针对 1、2、3输入的操作功能
if action_str in ["1","2","3"]:
    #代码未完成，用pass站位保证程序能够运行
    pass

#用户输入0，退出程序
elif action_str == "0":
    print("欢迎下次使用[名片管理系统]！")
    pass

#其他用户输入，提示输入错误
else:
    print("输入错误，请继续输入...")
