
# from ..config import configs
import pika

import json


def get_connection( env, queue_env='meta'):
    '''
    :param env: the key is params of config environment
    :return connection: the connection to rabbit_mq server
    '''
    real_params = {
        'socket_timeout': 600,
        'heartbeat': 600,
        'blocked_connection_timeout': 30,
        'connection_attempts': 1,
        'retry_delay': 10
    }
    env_params = {
            'account': 'themis',
            'password': 'themis@123',
            'host': '192.168.1.209',
            'port': 32672,
        }
    # log.warning(env_params)
    credentials = pika.PlainCredentials(env_params.get('account'), env_params.get('password'))
    params = {**real_params,
              **{'host': env_params.get('host'), 'port': env_params.get('port'), 'credentials': credentials}}
    # log.warning(params)
    connection = pika.BlockingConnection(pika.ConnectionParameters(**params))
    # connection.process_data_events()
    channel = connection.channel()
    return channel


def publish(name, env, queue_env, body):
    '''
    将mitmproxy拦截到的url发送到线上队列
    :param name: queue name
    :param env:
    :param body:格式化后的json，包含新闻链接
    :return:
    '''
    print(env, queue_env, name)
    channel = get_connection(env=env, queue_env=queue_env)
    channel.queue_declare(queue=name,durable=True)
    channel.basic_publish(exchange='',
                          routing_key=name,
                          body=body)

publish('test','beta','meta','dragon')