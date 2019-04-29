# -*- encoding=utf-8 -*-
__author__ = 'neo'

from airtest.core.api import *

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco

import redis

redis_connect = redis.StrictRedis(host='192.168.1.10', port=6379, db=0)
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

while True:
    try:
        title_obj_list = poco(name='cn.com.askparents.parentchart:id/text_partynmae')
        title_list = [title.get_text() for title in title_obj_list]
        for title in title_list:
            print(title)
        poco.swipe([1 / 2, 9 / 10], [1 / 2, 3 / 10], duration=0.5)
    except:
        continue
