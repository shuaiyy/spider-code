"""
爬取的源网页是https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=%E7%94%B5%E5%BD%B1
通过分析该页面展示的信息并没有在html源码中，来自于js，但是在js里面也没有找到相关信息，那么通过分析，就是js函数向服务器又请求了数据，通常来说
页面数据都是保存在json里的，通过谷歌开发工具的network的XHR找到了请求数据的连接，连接打开正是我们想要的json数据。beautiful.

数据提取:
把json格式的数据放到json解析工具里面能够清楚的看到数据结构，通过数据结构的特点，我们能够拿到我们想要的信息
本代码已经将电影名称，评分和海报连接保存到了默认路径的txt文档中
"""

import requests
class Craw:
    def __init__(self):
        self.url = 'https://movie.douban.com/j/new_search_subjects?sort=S&range=9,10&tags=%E7%94%B5%E5%BD%B1&start=0'
        self.headers = {
            "Connection": "keep-alive",
            "Host": "movie.douban.com",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"

        }

    def request(self):
        response = requests.get(self.url,headers = self.headers).json()["data"]
        with open('所有电影信息.txt','a') as f:

            for i in response:
                title = i["title"]
                rate = i["rate"]
                img_url = i["cover"]
                text = title + ' ' + rate + ' ' + img_url + '\n'
                f.write(text)
        print(type(response))

if __name__ == '__main__':
    craw = Craw()
    craw.request()
