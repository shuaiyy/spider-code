import requests
from urllib import request
from lxml import etree
import threading
import time

class Spider:
    """定义一个爬虫类"""
    def __init__(self):
        """初始化地址和头"""
        self.url = 'http://cn-proxy.com/'
        self.headers = {"user-agent":
               "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    def get_html(self):
        """"拿到html源码"""
        while True:
            try:
                html = requests.get(self.url, headers=self.headers).text
                return html
                break
            except:
                print('请求错误')
                time.sleep(5)
    def parse(self):
        """拿到字符串类型的列表"""
        tree = etree.HTML(self.get_html())
        ips = tree.xpath('//tbody/tr/td[1]/text()')
        dks = tree.xpath('//tbody/tr/td[2]/text()')
        full = []
        if len(ips) == len(dks):
            for ip, dk in zip(ips, dks):
                full.append(ip + ':' + dk)
        full = str(full)
        return full
    def save(self):
        """将ip端口列表保存到本地txt文档中"""
        with open('代理ip.txt', 'w') as f:
            f.write(self.parse())

class ProxyCheck(threading.Thread):
    def __init__(self,proxy_list):
        super().__init__()
        self.proxy_list = proxy_list
        self.timeout = 5
        self.url = 'http://www.ip.cn/'
        self.checked_list = []
    def check(self):
        """通过访问检测ip的网站看看自己的代理是否成功，拿到网站的ip识别信息"""
        for proxy in self.proxy_list:
            p = request.ProxyHandler({'http':proxy})
            opener = request.build_opener(p)
            opener.addheaders = [('user-agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')]
            t1 = time.time()
            try:
                result = opener.open(self.url,timeout=self.timeout).read().decode('utf-8')
                t2 = time.time() - t1
                tree = etree.HTML(result)
                the_ip = tree.xpath('//code/text()')[0]
                if the_ip in proxy:
                    self.checked_list.append((proxy,t2))
            except:
                print('打不开这个网址')
        return self.checked_list
    def sort(self):
       new_list = sorted(self.check(),key=lambda x:x[1])
       return new_list
    def run(self):
        with open('newip.txt','w') as f:
            f.write(str(self.sort()))

if __name__ == '__main__':
    proxy = Spider()
    proxy_list = eval(proxy.parse())
    print(proxy_list)
    mm = ProxyCheck(proxy_list)
    mm.start()