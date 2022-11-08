# 保存学员信息
info = []
# 封装功能界面的函数
def print_info():
    print('1.添加学员')
    print('2.删除学员')
    print('3.修改学员信息')
    print('4.查询学员信息')
    print('5.显示所有学员信息')
    print('6.退出系统')
    print('*' * 20)
# 1.添加学员函数
def add_info():
    """添加学员"""
    while True:
        aa = input('请输入y添加或exit退出添加：')
        if aa == 'exit':
            break
        else:
            new_id = int(input("请输入学号:"))
            new_name = input("请输入姓名:")
            new_tal = int(input("请输入手机号:"))
            global info
            for i in info:
                if new_id == i["id"]:
                    print("该用户已存在！")
                    break
            else:
                info_dict = {}
                info_dict["id"] = new_id
                info_dict["name"] = new_name
                info_dict["tel"] = new_tal
                info.append(info_dict)
            print(f'当前信息{info}')


# 2.删除学员函数
def del_info1():
    """删除学员"""
    while True:
        print(f'当前信息{info}')
        del_id = input('请输入要删除的学员学号或exit退出删除：')
        global info
        if del_id == 'exit':
            break
        else:
            del_id = int(del_id)
            for i in info:
                if del_id == i['id']:
                    del_flag = input('确定要删除吗？yes or no: ')
                    if del_flag == 'yes' :
                        info.remove(i)
                        break
                    else:
                        break
            else:
                print('id不存在')
            # print(f'当前信息{info}')


# 3.修改学员信息
def modify_info1():
    """修改学员信息"""
    while True:
        print(f'当前信息{info}')
        modify_id = input('请输入要修改的学员学号或exit退出修改：')
        global info
        if modify_id == 'exit':
            break
        else:
            modify_id=int(modify_id)
            for i in info:
                if modify_id == i['id']:
                    print(f'该学员学号是:{i["id"]},姓名是:{i["name"]},手机号是:{i["tel"]}')
                    i['id'] = int(input('请输入新学号：'))
                    i['name'] = input('请输入新姓名：')
                    i['tel'] = int(input('请输入新tel：'))
                    print(info)
                    break
            else:
                print('id不存在')
            # print(f'当前信息{info}')

#4.查询学员信息
def search_info():
    while True:
        a=input('是否继续查询y/n')
        if a == 'y':
            '''查询学员信息'''
            search_name = int(input('请输入要查找学员id:    '))
            for i in info:
                if search_name == i['id']:
                    print('查询信息如下')
                    print(i)
                    break
            else:
                print('查无此人')
        else:
            break

#5.显示所有学员信息
def print_all():
    '''查询学员所有信息'''
    while True:
        a=input('是否进行查找所有学员操作 y/n')
        if a == 'y':
            print('学号\t姓名\t电话')
            for i in info:
                print(f'{i["id"]}\t{i["name"]}\t{i["tel"]}')
        else:
            break




while True:  # while True 无限循环
    print_info()
    # 用户手动输入序号,选择功能
    user = input('请输入您需要的功能序号:  ')
    # 根据用户的选额执行不同的功能(多重判断)
    if user == '1':
        add_info()
    elif user == '2':
        del_info1()
    elif user == '3':
        modify_info1()
    elif user == '4':
        search_info()
    elif user == '5':
        print_all()
    elif user == '6':
        print('6.退出系统')
        print('是否要退出')
        z = input('y/n')
        if z == 'y':
            print('系统已安全退出')
            break
        elif z == 'n':
            print('返回功能提示界面')
    else:
        print('输入错误,请重新输入!!!')