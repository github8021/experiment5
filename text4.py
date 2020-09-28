# -*- coding: utf-8 -*-
"""
-------------------------------------------------
# @Project  :experiment5
# @File     :text4
# @Date     :2020/9/28 19:37
# @Author   :施嘉伟
# @Email    :1138128021@qq.com
# @Software :PyCharm
-------------------------------------------------
"""
friend = []
while (True):
    print("""
-------------------------------------------------
==============欢迎使用好友管理系统==================
1.添加好友
2.删除好友
3.备注好友
4.展示好友
5.退出
-------------------------------------------------
    """)
    i = int(input("请输入您的选择："))
    if (i == 1):
        name=input("请输入要添加的好友姓名：")
        friend.append(name)
        print("添加成功！")
    elif (i == 2):
        name=input("请输入要删除好友姓名")
        if(friend.count(name)):
            print("对不起，此好友不存在")
        else:
            friend.remove(name)
            print("删除成功")
    elif (i == 3):
        name=input("请输入要修改的好友姓名：")
        name2=input("请输入备注名：")
        index_name=friend.index(name)
    elif (i == 4):
        print()
    elif (i == 5):
        print("您已退出")
        exit()
