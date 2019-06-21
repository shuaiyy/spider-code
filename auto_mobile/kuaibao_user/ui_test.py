"""
328个被封
如果项目中多个组件彼此有极强的唯一依赖性，
将启动组件等将命令行操作，集成到一个代码文件中
"""
import uiautomator2 as u2
import time
import os
import subprocess
from multiprocessing import Process

def run_proxy():
    # 启动代理服务
    # os.system('mitmdump -q -s /home/dragon/Documents/companyproject/DaZhongdianping/daZhongFood/spider/mitmdumps_script.py -p 8888')
    cmd = 'mitmdump -q -s mitmdumps_script.py -p 8888'
    subprocess.run(cmd.split())
    # subprocess.run(shell,shell=True)


def run_spider():
    """
    天天快报大字版

    需要注意的是如果手机息屏等问题导致，
    爬虫框架无法链接手机会有requests......connectiong ....timeout 之类的报错
    :return:
    """
    while True:
        try:
            # d = u2.connect_usb('2244261a')
            d = u2.connect_usb('6391064e7d25')
            break
        except:
            # 初始化uiautomator2 否则有可能连不上
            os.system('python -m uiautomator2 init')
    d.app_start('com.tencent.readingplus')
    d(resourceId="com.tencent.readingplus:id/search_btn").click()
    num = 0
    with open('media.txt', 'r') as f:
        for i in f.readlines():
            num += 1
            # 清缓存
            d.clear_text()
            d(resourceId='com.tencent.readingplus:id/inputSearch').send_keys(i)
            d(text='搜索').click()
            print('第 {} 个搜索词 {}'.format(num,i))
            # 据说有封锁
            time.sleep(1)

# 用多进程解决命令行阻塞的问题
for func in [run_proxy,run_spider]:
    p = Process(target=func)
    p.start()
    print('run,ok')
