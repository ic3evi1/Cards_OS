#所有名片列表变量
card_list = []

def show_menu():
    """显示系统菜单"""
    print("♤" * 50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1. 新建名片")
    print("2. 显示全部")
    print("3. 查询名片")
    print("")
    print("0. 退出系统")
    print("♤" * 50)

def new_card():
    """新建名片"""
    print("-" * 50)
    print("新建名片")

    # 1.提示用户输入内容
    name_str = input("请输入姓名：")
    phone_str = input("请输入电话号码：")
    qq_str = input("请输入QQ号码：")
    mail_str = input("请输入邮箱：")

    # 2.把用户的输入信息保存字典里
    card_dict = {
        "name": name_str,
        "phone": phone_str,
        "qq": qq_str,
        "mail": mail_str
    }

    # 3.把用户的字典添加到名片列表里
    card_list.append(card_dict)
    #print(card_list)
    # 4.提示用户信息添加成功
    print("%s 的名片信息添加成功" % name_str)
    print("姓名\t\t电话\t\tQQ\t\t邮箱")
    print("-" * 50)
    print("%s\t\t%s\t\t%s\t\t%s" % (
        card_dict["name"],
        card_dict["phone"],
        card_dict["qq"],
        card_dict["mail"]
    ))

def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    # 如果用户信息为空，提示用户，返回
    if len(card_list) == 0:
        print("没有任何名片记录信息，请新建名片！")
        return
    #显示表头
    for list_head in ["姓名","电话","QQ","邮箱"]:
        print(list_head,end="\t\t")
    print("")
    print("-"*50)

    #显示列表字典信息
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (
            card_dict["name"],
            card_dict["phone"],
            card_dict["qq"],
            card_dict["mail"]
        ))

def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    #提示用户输入要搜索的用户姓名
    find_name = input("请输入要查找名片的姓名：")

    #遍历字典，查找用户，找到输出名片信息，没找到，提示用户
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱")
            print("-"*50)
            print("%s\t\t%s\t\t%s\t\t%s" % (
                card_dict["name"],
                card_dict["phone"],
                card_dict["qq"],
                card_dict["mail"]
            ))
            deal_card(card_dict)
            break

    else:
        print("没有找到 %s" % find_name)

def deal_card(find_dict):
    action_str = input("请选择要执行的操作"
                       "【1】删除用户 【2】修改用户 "
                       "【0】返回上级菜单：")
    if action_str == "1":
        card_list.remove(find_dict)
        print("%s 的名片删除成功" % find_dict["name"])

    elif action_str == "2":
        find_dict["name"] = input_card_info(find_dict["name"],"姓名：")
        find_dict["phone"] = input_card_info( find_dict["phone"] ,"电话：")
        find_dict["qq"] = input_card_info(find_dict["qq"],"QQ：")
        find_dict["mail"] = input_card_info(find_dict["mail"],"邮箱：")
        print("%s 的名片修改完毕" % find_dict["name"])


def input_card_info(card_value,tip_message):
    input_str = input(tip_message)

    if len(input_str) > 0:
        return input_str
    else:
        return card_value