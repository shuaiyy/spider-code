# -*- coding: utf-8 -*-
from urllib import request
from urllib import parse
from http import cookiejar
import re
import os
# 分析得到登陆请求的地址
url = 'https://accounts.douban.com/login'
# 审查元素network-all-login得到form_data
form_data = {'source':'index_nav',
             'redir':'https://www.douban.com/',
             'form_email':'17621989923',
             'form_password':'17621989923'}
# 构造马甲
cookie = cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cookie))
# 伪造头部信息
opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/63.0.3239.84 Safari/537.36')]
# 获取验证码
html = request.urlopen(url).read().decode('utf-8')
src = re.findall('"captcha_image" src="(.+?)" alt',html)[0]
if len(src) > 0:
    request.urlretrieve(src,'1.png')
    os.startfile('1.png')
    solution = input('请输入验证码：')
    id = re.findall('id=(.+?)&',src)[0]
    form_data = {'source': 'index_nav',
                 'redir': 'https://www.douban.com/',
                 'form_email': '17621989923',
                 'form_password': 'nishijiba22',
                 'captcha-solution':solution,
                 'captcha-id':id,
                 'login':'登录'}
# 披着cookie马甲向服务器发起请求
data = parse.urlencode(form_data).encode()
r = opener.open(url,data)
# 登陆后解析网页找到正则匹配自己的帐号
r = opener.open('https://www.douban.com').read().decode('utf-8')
pattern = re.compile('<span>(.+?)的帐号</span>')
result = re.findall(pattern,r)
print(result)
