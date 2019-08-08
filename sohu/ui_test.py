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


def run_spider(deviceid,keyword):
    """
    天天快报大字版

    需要注意的是如果手机息屏等问题导致，
    爬虫框架无法链接手机会有requests......connectiong ....timeout 之类的报错
    :return:
    """
    while True:
        try:
            d = u2.connect_usb(deviceid)
            # d = u2.connect_usb('6391064e7d25')
            break
        except:
            # 初始化uiautomator2 否则有可能连不上
            os.system('python -m uiautomator2 init')
    d.app_start('com.sohu.newsclient')
    # 点击首页的+号展开搜索框
    d(resourceId="com.sohu.newsclient:id/right_more_img").click()
    d(text='搜索新闻').click()
    # 清缓存
    d.clear_text()
    d(resourceId='com.sohu.newsclient:id/ed_keywords').send_keys(keyword)
    # 自带输入法
    d.send_action('search')
    # d.swipe("down", steps=20)
    d(scrollable=True).scroll.toEnd()


run_spider('2775f5377d28','郭台铭啊')