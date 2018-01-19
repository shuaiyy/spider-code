#coding:utf-8
from queue import Queue
from lxml import etree
import threading
import requests
import json
# 类的继承
class ThreadCrawl(threading.Thread):
    def __init__(self,threadName,pageQueue,dataQueue):
        # 继承类的初始化
        super(ThreadCrawl,self).__init__()
        self.threadName = threadName
        self.pageQueue = pageQueue
        self.dataQueue = dataQueue
        self.headers = {"User-Agent":" Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    def run(self):
        print('启动'+ self.threadName)
        while not CRAWL_EXIT:
            try:
                # 如果队列为空，block参数为True的话，不会结束，会进入阻塞状态，知道队列有新的数据
                # 如果对列为空，block参数位False的话，会弹出一个Queue.empty()异常，
                page = self.pageQueue.get(False)
                url = 'https://www.lagou.com/zhaopin/Python/{}/?filterOption={}'.format(page,page)
                html = requests.get(url,headers = self.headers).text
                self.dataQueue.put(html)
            except:
                pass
        print('结束'+self.threadName)
class ThreadParse(threading.Thread):
    def __init__(self,threadName,dataQueue,f):
        super(ThreadParse,self).__init__()
        #线程名
        self.threadName = threadName
        # 数据队列
        self.dataQueue = dataQueue
        # 解析后数据的文件名
        self.f = f
    def run(self):
        while not PARSE_EXIT:
            try:
                html = self.dataQueue.get(False)
                self.parse(html)
            except:
                pass
        print('结束' + self.threadName)
    def parse(self,html):
        tree = etree.HTML(html)
        contents = tree.xpath('//h3/text()')

        for content in contents:
            content2 = json.dumps(content,ensure_ascii = False)
            f.write(content2)
            f.close()
        print('写入完成')
global CRAWL_EXIT
global PARSE_EXIT

CRAWL_EXIT = False
PARSE_EXIT = False
def main():
    # 页码的队列，表示10个页面
    pageQueue = Queue(10)
    for i in range(1,11):
        pageQueue.put(i)
    dataQueue = Queue()  #为空表示不限制
    f = open('duanzi.json','a')
    # 三个采集线程的名字
    crawList = ['采集线程1号','采集线程2号','采集线程3号']
    threadcrawl = []
    for threadName in crawList:
        thread = ThreadCrawl(threadName,pageQueue,dataQueue)
        thread.start()
        threadcrawl.append(thread)
    while not pageQueue.empty():
        pass
    global CRAWL_EXIT
    CRAWL_EXIT = True
    print('pageQueue为空')
    for thread in threadcrawl:
        thread.join()
        print('1')
    # 三个解析线程的名字
    parseList = ['解析线程1号','解析线程2号','解析线程3号']
    # 存储三个解析线程
    threadparse = []
    for threadName in parseList:
        thread = ThreadParse(threadName,dataQueue,f)
        thread.start()
        threadparse.append(thread)
    while not dataQueue.empty():
        pass
    global PARSE_EXIT
    PARSE_EXIT = True
    print('dataQueue为空')
    for thread in threadparse:
        thread.join()
        print('2')
    # global CRAWL_EXIT
    # CRAWL_EXIT = True

if __name__ == '__main__':
    main()