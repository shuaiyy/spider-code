"""
    与Appium服务端通信
    客户端基本操作指令（automation配置文件）
"""
import time
import yaml
import os
from appium import webdriver
from .swipe import swiping,tap_search
from logger import LogHandler
automation = yaml.load(open('./config/automation.yaml'), Loader=yaml.FullLoader)
host = yaml.load(open('./config/appium.yaml'), Loader=yaml.FullLoader)['host']

log = LogHandler('app_spider')

class ControlBase:
    """
    与appium连接控制手机
    """
    def __init__(self, app_name=None, port=None, udid=None):
        self.app_name = app_name
        self.port = port
        self.platformName = 'Android'
        self.deviceName = 'MI'
        self.noReset = True
        self.unicodeKeyboard = True
        self.resetKeyboard = True
        if app_name is not None:
            self.appPackage = automation[app_name]['appPackage']
            self.appActivity = automation[app_name]['appActivity']
        if udid is not None:
            self.udid = udid

    def __start_driver(self):
        print(self.__dict__)

        self.driver = webdriver.Remote('http://{}:{}/wd/hub'.format(host, self.port), self.__dict__)
        print(self.__dict__)
        time.sleep(6)

    def auto_control(self, keywords, app_name, port, udid):
        """
        顺序执行automation配置文件中的操作方法
        :param keywords: 搜索关键词
        :param app_name: app名称与配置文件中的名称相对应
        :param port: 与appium服务端口对应
        :param udid: 手机id
        :return:
        """
        logtext = '调用关键词--{}--操作--{}--APP'.format(keywords,app_name)
        log.info(logtext)

        self.app_name = app_name
        self.port = port
        self.udid = udid
        self.appPackage = automation[app_name]['appPackage']
        self.appActivity = automation[app_name]['appActivity']
        step_1 = automation[self.app_name]['steps'][0]
        step_2 = automation[self.app_name]['steps'][1]
        try:
            self.__control_way(keywords, **step_2)
        except:
            self.__start_driver()
            # self.__ignore_elements()
            self.___swipe()
            self.__control_way(keywords, **step_1)
            self.__control_way(keywords, **step_2)
        for step in automation[self.app_name]['steps'][2:]:
            self.__control_way(keywords, **step)

    def __find_element(self, **kwargs):
        """
        元素类型,包括 id,xpath
        :param kwargs:
        :return: 返回driver的元素查找方法
        """
        if kwargs.get('select_type') == 'id':
            return self.driver.find_element_by_id(kwargs.get('selector'))
        if kwargs.get('select_type') == 'xpath':
            print(kwargs.get('selector'))
            return self.driver.find_element_by_xpath(kwargs.get('selector'))

    def __control_way(self, keywords, **kwargs):
        """
        主要控制方法获取,包括search,click,clear,send_keys,swipe
        :param keywords: 搜索关键词
        :param kwargs:
        :return:
        """
        if kwargs.get('action') == 'search':  # 调用搜狗键盘进行点击搜索,需要 x , y 坐标
            self.driver.activate_ime_engine('com.sohu.inputmethod.sogou.xiaomi/.SogouIME')
            time.sleep(kwargs.get('sleep'))
            # self.driver.tap([(kwargs.get('x'), kwargs.get('y'))])
            tap_search(self.driver)
            time.sleep(kwargs.get('sleep'))
        if kwargs.get('action') == 'click':
            self.__find_element(**kwargs).click()
        if kwargs.get('action') == 'clear':
            self.__find_element(**kwargs).clear()
        if kwargs.get('action') == 'send_keys':  # 需要手机安装虚拟键盘(adbkeyboard)
            self.__find_element(**kwargs).click()
            self.driver.activate_ime_engine('com.android.adbkeyboard/.AdbIME')
            keywords = keywords.replace(' ', ',')
            self.__find_element(**kwargs).clear()
            os.system("adb -s {} shell am broadcast -a ADB_INPUT_TEXT --es msg {}".format(self.udid, keywords))
            time.sleep(2)
            # self.__find_element(**kwargs).send_keys('{}'.format(keywords))
        if kwargs.get('action') == 'swipe':
            try:
                times = kwargs.get('times', 3)
                for i in range(times):
                    swiping(self.driver, kwargs.get('direction'))
                    time.sleep(kwargs.get('sleep'))
            except:
                print('滑页失败')

    def __ignore_elements(self):  # 目前未使用
        """
        部分元素点击忽略，例如‘跳过’，‘下一步’
        :return:
        """
        if 'ignore_words' in automation[self.app_name]:
            text = automation[self.app_name].get('ignore_words')
            self.driver.find_element_by_android_uiautomator(text).click()
        else:
            return

    def ___swipe(self):  # 向下滑动
        swiping(self.driver, 'down')
        time.sleep(2)
