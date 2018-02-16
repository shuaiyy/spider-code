# -*- coding:UTF-8 -*-
import itchat
itchat.auto_login(hotReload = True)
users = itchat.get_friends()
for i in range(len(users)):
    user = itchat.get_friends()[i]
    msc = itchat.get_friends()[i]['NickName'] + '老铁:圣诞节快乐哦噢噢噢噢哦'
    user.send(msc)
