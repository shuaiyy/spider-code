import json
import time
import pika
from config.config import configs
# import logging
from logger import LogHandler

log = LogHandler('rabbitmq')

class QueueTransport:
    need_save_dict = {}

    def __init__(self, source_env=None, source_queue_name=None, source_queue_env=None):
        self.source_env = source_env
        # beta rabbit 队列名字
        self.source_queue_name = source_queue_name
        self.source_queue_env = source_queue_env
        self.destination_env = 'app_spider_queue_server'
        self.destination_queue_name = 'apps_queue'
        self.destination_queue_env = 'meta'

    def get_connection(self, env, queue_env='meta'):
        '''
        :param env: the key is params of config environment
        :return connection: the connection to rabbit_mq server
        '''
        real_params = configs.get('real_params_for_connection')
        env_params = configs.get(env).get(queue_env)
        # log.warning(env_params)
        credentials = pika.PlainCredentials(env_params.get('account'), env_params.get('password'))
        params = {**real_params,
                  **{'host': env_params.get('host'), 'port': env_params.get('port'), 'credentials': credentials}}
        # log.warning(params)
        connection = pika.BlockingConnection(pika.ConnectionParameters(**params))
        connection.process_data_events()
        channel = connection.channel()
        return channel

    def declare_queue(self, name, env, queue_env='meta'):
        '''
        :param name: queue name
        :param env:
        :return: None
        '''
        channel = self.get_connection(env=env, queue_env=queue_env)
        channel.queue_declare(queue=name, durable=True, arguments={'x-max-priority': 10})

    # 发布
    def publish(self, name, env, queue_env, body):
        '''
        将mitmproxy拦截到的url发送到线上队列
        :param name: queue name
        :param env:
        :param body:格式化后的json，包含新闻链接
        :return:
        '''
        channel = self.get_connection(env=env, queue_env=queue_env)
        channel.basic_publish(exchange='',
                              routing_key=name,
                              body=body)
        # 必须先声明队列
        channel.queue_declare(queue=name, durable=True,arguments={'x-max-priority': 10})
        channel.close()
        log.info('task published---{}'.format(json.loads(body)['app']))

    # 消费
    def consume(self, queue_env):
        '''
        从线上队列获取消息，获取后调用callback 函数对消息进行处理
        '''
        print(self.source_env,queue_env)

        channel = self.get_connection(env=self.source_env, queue_env=queue_env)

        channel.queue_declare(name=self.source_queue_name, durable=True, arguments={'x-max-priority': 10})

        channel.basic_consume(queue=self.source_queue_name, auto_ack=True, on_message_callback=self.callback)

        channel.start_consuming()

    def callback(self, ch, method, properties, body):
        """
        消费者默认回调
        拿到线上队列的消息体，连接接本地队列，将消息修改发送到本地队列
        """
        channel = self.need_save_dict.get('target_queue')
        if channel is None:
            channel = self.get_connection(
                env=self.destination_env)  # type pika.adapters.blocking_connection.BlockingChannel
            self.need_save_dict['target_queue'] = channel
        # 将app信息加入到任务中
        _body = json.loads(body)
        scheduleTime = _body['scheduleTime']
        # 队列数据小于8小时，才将其放入本地队列
        if (time.time() - scheduleTime/1000) < 8*60*60:

            for app in ['zaker','yidianzixun','kuaibao']:
                _body['app'] = app
                channel.queue_declare(name=self.destination_queue_name, durable=True, arguments={'x-max-priority': 10})
                channel.basic_publish(exchange='', routing_key=self.destination_queue_name, body=json.dumps(_body))
                log.info('Local Rabbitmq Message Pushed Success -- {}'.format(app))
        else:
            log.warning('Task Time Expired')


