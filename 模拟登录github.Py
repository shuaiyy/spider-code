import requests
from lxml import etree
class Spider:
    def __init__(self):
        self.url = 'https://github.com/'
        self.loginurl = 'https://github.com/login'
        self.posturl = 'https://github.com/session'
        self.session = requests.session()
        self.headers = {
            "Connection":"keep-alive",
            "Host":"github.com",
            "Referer":"https://www.jianshu.com/p/1f8a45b3f20a",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.167 Safari/537.36"
            }
    def get_token(self):
        html = self.session.get(self.loginurl,headers = self.headers).text
        content = etree.HTML(html)
        token = content.xpath('//input[2]/@value')[0]
        return token
    def post(self):
        login = input('请输入您的帐号：')
        password = input('请输入您的密码：')
        form_data = {
            "commit":"签到",
            "utf8":"✓",
            "authenticity_token":self.get_token(),
            "login":login,
            "password":password
            }
        self.session.post(self.posturl,data = form_data,headers = self.headers)
    def verification(self):
        content = self.session.get(self.url,headers = self.headers).text
        html = etree.HTML(content)
        result = html.xpath('//img/@alt')[0]
        print(result)
    def main(self):
        self.post()
        self.verification()
if __name__ == '__main__':
    spider = Spider()
    spider.main()