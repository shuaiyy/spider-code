import requests
import time
import json
import re
import base64
import rsa
import binascii
import execjs

# 模拟新浪微博登录的完整请求过程，包括预登录，重定向，和最后返回个人主页；
# 该项目的难点再与破解js加密的post数据，在此基础上，还需要多次对服务器发起多个请求，
# 完整的流程走下来，微博才鞥够成功的登录上


# 整体的框架梳理：  全程用session保存cookie 哦
#                  第一：通过抓包可以发现，我们在登录微博首页的时候，客户端向服务器发起的请求并不是首页的地址，而是/vistor/vistor
# 为了全真模拟，那么我们也必须先请求这个地址，然后再；
#                  第二：请求微博的首页，似乎没什么意思，就是要走这个流程，也许不需要，代码还没有优化；
#                  第三：预登录，这一步就很重要了，因为在后面的post登录请求中会有很多的表单数据，预登录的响应信息有很多我们想要的；
#                  第四：找到加密password等数据的加密js，在js中找到加密的方式，破解加密；
#                  第五：发起post登录请求；
#                  第六：发起多次的重定向请求
#                  第七：打开个人首页，到此便大功告成；perfect！！！！！
class WeiBo:

    def __init__(self,name,password):
        self.start_url = 'https://passport.weibo.com/visitor/visitor'
        self.user_name = name
        self.user_password = password

    def vister(self):
        headers1 = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        }
        data1 = {
            "entry": "miniblog",
            "a": "enter",
            "url": "https://weibo.com/",
            "domain": ".weibo.com",
            "ua": "php-sso_sdk_client-0.6.23",
            "_rand": round(time.time(), 4),
        }
        self.ss = requests.Session()
        self.r = self.ss.get(self.start_url,headers = headers1,params = data1)
        self.url = self.r.url

    def first(self):
        # 打开微博首页；
        first_page_url = 'https://weibo.com/'
        headers2 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        "Referer": self.url,
    }
        content = self.ss.get(first_page_url,headers = headers2)

    def prelogin(self):
        # 预登陆，拿到服务器返回的加密信息；
        prelogin_url = 'https://login.sina.com.cn/sso/prelogin.php'
        params = {
            "entry": "weibo",
            "callback": "sinaSSOController.preloginCallBack",
            'su': '',
            "rsakt":"mod",
            "client": "ssologin.js(v1.4.19)",
            "_": int(time.time()*1000)
        }
        content = self.ss.get(prelogin_url,params=params)

        try:
            pattern = re.compile(r'sinaSSOController.preloginCallBack\((.+?)\)')
            content = re.findall(pattern,content.text)[0]
            js = json.loads(content)
            self.servertime = js['servertime']
            self.nonce = js['nonce']
            self.pubkey = js['pubkey']
            self.rsakv = js['rsakv']
            self.exectime = js['exectime']
            print('服务器返回的密码提取成功！')

        except:
            print('json解析不了')

    def password(self):
        # 解密js加密后的用户密码；用python rsa库加密用户密码(这是解密的第一种方式)
        rsakey = rsa.PublicKey(int(self.pubkey,16),int('10001',16))
        strall = str(self.servertime) + '\t' + self.nonce + '\n' + self.user_password
        content = rsa.encrypt(strall.encode('utf-8'),rsakey)
        self.sp = binascii.b2a_hex(content)
    def password2(self):
        # 解密的第二种方式，通过execjs 调用PhantomJs,直接执行js代码，难道函数的返回值（密码）；
        with open('totall.js','r',encoding='utf-8') as f:
            source = f.read()
        phantom = execjs.get('PhantomJs')
        phantom_compile = phantom.compile(source)
        call = phantom_compile.call('get_pass', 'nishijiba22', self.nonce, self.servertime, self.pubkey)
        return call
    def login(self):
        form_data = {
        "entry": "weibo",
        "gateway": "1",
        'from':'',
        "savestate": "7",
        "qrcode_flag": "false",
        "useticket": "1",
        "pagerefer":self.url,
        "su": base64.b64encode(self.user_name.encode('utf-8')),
        "service": "miniblog",
        "servertime": int(time.time()),
        "nonce": self.nonce,
        "pwencode": "rsa2",
        "rsakv": self.rsakv,
        "sp": self.password2(),
        "sr": "1366*768",
        "encoding": "UTF-8",
        "prelt": int(time.time()*1000)-self.exectime,
        "url":"https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack",
        "returntype": "META"
        }
        url = 'https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.19)'
        headers = {
            "Origin": "https://weibo.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
            "Referer": "https://weibo.com/",
        }
        content = self.ss.post(url,headers=headers,data=form_data).content.decode('gbk')
        pattern = re.compile(r'location.replace\("(.+?)"\)')
        self.cross_url = re.findall(pattern,content)[0]
    # 别急别急你得到的还不是最终结果，新浪就是这么变态

    def home(self):
        # 获取个人主页的地址

        # 处理第一个重定向
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
        }
        content = self.ss.get(self.cross_url,headers=headers).content.decode('GBK')
        url2 = re.findall(r"location.replace\('(.+?)'\)",content)[0]
        self.ss.get(url2,headers=headers)
        # 处理第二个重定向；
        url = 'https://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack&sudaref=weibo.com'
        content = self.ss.get(url,headers=headers).content.decode('gbk')
        pattern = r'"uniqueid":"(\d+?)"'
        try:
            uuid = re.findall(pattern, content)[0]
        except:
            print('没有匹配到uniquid')
        else:
            # 处理第三个重定向
            url3 = 'https://weibo.com/nguide/interest'
            self.ss.get(url3,headers=headers)
            # 处理第四个重定向
            url4= 'https://weibo.com/nguide/interests'
            self.ss.get(url4,headers=headers)
            # 拼接个人主页
            url = 'https://weibo.com/u/{}/home'.format(uuid)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36",
                "Referer": "https://weibo.com/",

            }
            home_page = self.ss.get(url,headers=headers).text
            print('出结果了哦'*9)
            print(home_page)

    def main(self):
        self.vister()
        self.first()
        self.prelogin()
        # self.password()
        self.login()
        self.home()

if __name__ == '__main__':
    name = 'your user name'
    password = 'your password'
    weibo = WeiBo(name,password)
    weibo.main()