import os
import re
import json
import yaml
import pika
import redis
from logger.log import LogHandler
from .search_news import ControlBase

appium_setting = yaml.load(open('./config/appium.yaml'))
automation_setting = yaml.load(open('./config/automation.yaml'))
redis_setting = yaml.load(open('./config/appium.yaml'))['redis']
rabbit_setting = yaml.load(open('./config/appium.yaml'))['rabbit']

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
        self.control = ControlBase() # 实例化appium控制
        # self.app = None
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=rabbit_setting['host'], port=int(rabbit_setting['port']),heartbeat=0))

    def get_task(self):
        channel = self.connection.channel()
        # channel.basic_qos(prefetch_count=1)
        while True:
            try:
                channel.basic_consume(queue='apps_queue', on_message_callback=self.callback,auto_ack=True)
                break
            except:
                channel = self.connection.channel()
                channel.queue_declare(queue='apps_queue')

        channel.start_consuming()

    def callback(self, ch, method, properties, body):
        """
        关于app的切换，当前存在疑问，部分代码基于当前的理解没有必要性，注释掉
        :param ch:
        :param method:
        :param properties:
        :param body:
        :return:
        """

        message = json.loads(body.decode())
        search_word = message['seedVal']
        app_task = message['app']
        log.info(app_task)
        name = app_task + '_' + message['seedVal'].replace(' ', '_')
        r.set(name, body.decode())
        try:
            self.control.auto_control(keywords=search_word, app_name=app_task, port=self.port,
                                      udid=self.udid)
            name = app_task + '_' + message['seedVal'].replace(' ', '_')
            r.set(name, body.decode())
            log.info('{} search {} success!'.format(app_task, search_word))

        except Exception as e:
            log.error('app {}  device_id {}爬虫故障......'.format(app_task,self.udid))
            log.error(e)
