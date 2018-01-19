#coding: utf-8
# 程序开始打印提示信息
print('=============')
print('欢迎使用名片管理系统v1')
print('1.添加名片')
print('2.删除名片')
print('3.修改名片')
print('4.查找名片')
print('5.查看所有名片')
print ('6.清空所有名片')
print ('7.打印全部名片信息')
print('0.退出系统')
print('=============')
mp_list = [] #存放名字的列表一定要放在循环外
# 死循环执行代码，为了是现代代码的每一个功能，否则数据清空
while True:
    commend = input('请输入指令：')
    # 指令1的之行代码
    if commend == '1':
        while True:
            name = input('请输入名字：')
            sex = input('请输入性别：')
            tel = input('请输入电话号码：')
            if len(name) >= 6:
                if len(name) <= 20:
                    if len(tel) == 11:
                        if sex == '男' or '女':
                            print (name,sex,tel)
                            mp_list.append(name)
                            mp_list.append(tel)
                            mp_list.append(sex)
                            break
                        else:
                            print ('没有这个性别')
                    else:
                        print('号码不是11位')
                else:
                    print ('长度大了')
            else:
                print('长度小了')
            print('请重新输入')
        # name_list.append(name)
    #     指令2的代码
    if commend == '2':
        delete_name = input('请输入要删除的人名：')
        if delete_name in name_list:
            name_list.remove(delete_name)
        else:
            print('名片不存在')#误操作报错
    #     指令3的执行代码
    if commend == '3':
        rename1 = input('请输入要修改的名字：')
        if rename1 in name_list:
            rename2 = input('请输入改后的名字：')
            num = name_list.index(rename1)
            name_list[num] = rename2
        else:
            print ('不存在这个名片')#误操作报错
    #     指令4的执行代码
    if commend == '4':
        find_name = input('请输入要查找的名字')
        if find_name in name_list:
            print ('存在')
        else:
            print ('不存在')
    #         指令5的执行代码
    if commend == '5':
        for names in name_list:
            print(names)
    #         指令0的执行代码
    if commend == '6':
        if len(mp_list) > 0:
            mp_list.pop()
    if commend == '7':
        for i in len(mp_list):
            print (mp_list[i])
    if commend == 'o':
        break
# 编程, 使用[字典]来存储一个人的信息（姓名、年龄、学号、QQ、微信、住址等）
# dic = {}
# name = input('请输入姓名：')
# age = input('请输入年龄：')
# num = input('请输入学号：')
# qq = input('请输入QQ号：')
# wechat = input('请输入微信号：')
# address = input('请输入地址：')
# dic['姓名'] = name
# dic['年龄'] = age
# dic['学好'] = num
# dic['QQ'] = qq
# dic['微信'] = wechat
# dic['地址'] = address
# print(dic)
# 1. 完成字符串的长度统计以及逆序打印
#     * 设计一个程序，要求只能输入长度低于31的字符串，否则提示用户重新输入
#     * 打印出字符串长度
#     * 使用切片逆序打印出字符串
# while True:
#     str = input('请输入长度低于31的字符串：')
#     if len(str) < 31:
#         print(len(str))
#         print(str[::-1])
#         break
# #     print('请重新输入！')
# 2. 用户名和密码格式校验程序
#     * 要求从键盘输入用户名和密码
#     * 校验格式是否符合规则，用户名长度6-20，并且用户名必须以字母开头
#     # * 如果不符合，打印出不符合的原因，并再次提示输入
#
#
# while True:
#     name = input('请输入用户名：')
#     pass_word = input('请输入密码：')
#
#     if len(name) >= 6 :
#         if len(name) <= 20:
#             if name[0].isalpha():
#
#                 break
#             else:
#                 print('不是字母开头')
#         else:
#             print ('长度大了')
#     else:
#         print('长度小了')
#     print('请重新输入')
# while True:
#     name = input('请输入名字：')
#     sex = input('请输入性别：')
#     tel = input('请输入电话号码：')
#     if len(name) >= 6:
#         if len(name) <= 20:
#             if len(tel) == 11:
#                 if sex == '男' or '女':
#                     print (name, sex, tel)
#                     break
#                 else:
#                     print ('没有这个性别')
#             else:
#                 print('号码不是11位')
#         else:
#             print ('名字长度大了')
#     else:
#         print('名字长度小了')
#     print('请重新输入')
# import random
# i = 0
# name_list = []
# while i < 5:
#     name = input('请输入名字：')
#     # print (name[1])
#     name_list.append(name)
#     i += 1
# name2 = random.choice(name_list)
# print ('请%s去打扫卫生' % name2)
# dic = {}
# while True:
#     str = input('请输入长度低于31的字符串：')
#     if len(str) < 31:
#         print(len(str))
#         print(str[::-1])
#         for i in range(len(str)):
#             dic[str[i]] = str.count(str[i])
#         print (dic)
#         break
#     print('请重新输入！')
# *用户如果输入的字符长度超过1或者是除数字以外其他字符，提示
# "未收录该字符的含义，请重新输入"
# dic = {'1':'!','2':'@','3':'#','4':'$','5':'%','6':'^','7':'&','8':'*','9':'(','0':')'}
# while True:
#     key = input('请输入笔记本电脑的数字键1-0：')
#     if key in dic:
#         print (dic[key])
#         break
# #     print ('未收录该字符的含义，请重新输入')
# 3.
# 职员信息管理系统
# *使用列表来记录多个员工的信息
# *要求依次从键盘录入每位员工的信息，并使用字典来保存，
# 包括姓名、员工id、出生年月、籍贯、身份证号、入职时间
# *要求能随时查看已录入的员工信息
# import json
# dic = {}
# list1 = []
# while True:
#     name = input('请输入姓名：')
#     id = input('请输入ID:')
#     birthday = input('请输入出生年月：')
#     home_dress = input('请输入籍贯：')
#     num = input('请输入身份证号：')
#     work_time = input('请输入入职时间：')
#     dic[name] = id + birthday + home_dress + num + work_time
#     with open('yuangong.json','a') as f:
#         f.write(json.dumps(dic))
#     list1.append(dic)
#     print(dic)
#     print(list1)
# from urllib import request
# from urllib import parse
# key = {'wb':'你好啊'}
# key = parse.urlencode(key)
# print (key)
# import os
# print(os.getcwd())
# # os.mkdir('ceshi')
# os.chdir('C:/Users/Administrator/Desktop/ceshi')
# print(os.getcwd())