import os
import re
import json
import yaml
import pika
import redis
import time
from copy import deepcopy

from logger.log import LogHandler
from .search_news import ControlBase
from config import configs
from threading import Thread



appium_setting = yaml.load(open('./config/appium.yaml'))
automation_setting = yaml.load(open('./config/automation.yaml'))
redis_setting = yaml.load(open('./config/appium.yaml'))['redis']
# rabbit_setting = yaml.load(open('./config/appium.yaml'))['rabbit']
prod_rabbit = configs['prod']['meta']
real_params = configs['real_params_for_connection']
devices_list = os.popen('adb devices')

redis_pool = redis.ConnectionPool(host=redis_setting['host'], port=int(redis_setting['port']), decode_responses=True)
r = redis.Redis(connection_pool=redis_pool)

log = LogHandler('spiders.tasks_assignment')


def port_list():
    """
    端口列表生成器
    :return: appium设置的与手机列表对应的端口号
    """
    for device in devices_list.readlines()[1:-1]:
        log.info('connect {}!'.format(device))
        yield {'port': appium_setting['port'], 'device': device}
        appium_setting['port'] += 2


def start_consume(param):
    consumer = AppConsumer(param)
    consumer.get_task()


class AppConsumer:
    """
    消费本地队列任务
    控制app执行
    """
    def __init__(self, param):
        self.port = param['port']
        self.udid = param['device'].replace('device', '').strip()
        # self.app = None
        self.channel = self.get_connection_channel()

    def get_connection_channel(self):
        credentials = pika.PlainCredentials(prod_rabbit.get('account'), prod_rabbit.get('password'))
        params = {**real_params,
                  **{'host': prod_rabbit.get('host'), 'port': prod_rabbit.get('port'), 'credentials': credentials}}
        log.warning(params)
        connection = pika.BlockingConnection(pika.ConnectionParameters(**params))
        channel = connection.channel()
        return channel

    def get_task(self):
        channel = self.channel
        # channel.basic_qos(prefetch_count=1)
        while True:
            try:
                channel.basic_consume(queue='spider.apps-android-search_list-defaultsort-starttasks.spider',
                                      on_message_callback=self.callback,auto_ack=True)
                break
            except:
                channel = self.get_connection_channel()
                channel.queue_declare(queue='spider.apps-android-search_list-defaultsort-starttasks.spider',
                                      durable=True, arguments={'x-max-priority': 10})

        channel.start_consuming()

    def callback(self,ch, method, properties,  body):
        """
        ch, method, properties, pika 标准形式必须加
        """

        message = json.loads(body.decode())

        scheduleTime = message['scheduleTime']
        # 队列数据小于8小时，才将其放入本地队列
        if (time.time() - scheduleTime/1000) < 8*60*60:
            messages = []
            for app_task in ['zaker', 'kuaibao']:
                message['app'] = app_task
                app_task = deepcopy(message)
                messages.append(app_task)
            for m in messages:
                self.spider_run(m)
                # t = Thread(target=self.spider_run,args=(m,))
                # t.start()
        else:
            log.warning('Task Time Expired')

    def spider_run(self,message):
        app_task = message['app']
        search_word = message['seedVal']
        log.info(app_task)
        name = app_task + '_' + message['seedVal'].replace(' ', '_')
        r.set(name, str(message))
        try:
            control = ControlBase(app_name=app_task, port=self.port, udid=self.udid)  # 实例化appium控制
            control.auto_control(keywords=search_word, app_name=app_task, port=self.port,
                                      udid=self.udid)
            name = app_task + '_' + search_word.replace(' ', '_')
            r.set(name, str(message))
            log.info('{} search {} success!'.format(app_task, search_word))

        except Exception as e:
            log.error('app {} 爬虫故障{}......'.format(app_task,self.udid))
            log.error(e)
