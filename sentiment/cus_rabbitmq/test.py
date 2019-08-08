
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

def callback( ch, method, properties, body):
    print(body)


# publish('test','beta','meta','dragon')
pika.ConnectionParameters(host='127.0.0.1',port=5672)
credentials = pika.PlainCredentials('guest', 'guest')
params = {
          **{'host': '127.0.0.1', 'port': 5672, 'credentials': credentials}}
connection = pika.BlockingConnection(pika.ConnectionParameters(**params))
channel = connection.channel()
# channel.queue_declare(queue='apps_queue')
# while True:
#     try:
# 如果队列不存在，那么会包404错误，信道会关闭，重新建立需要重新建立信道，并且申明队列
channel.basic_consume(auto_ack=True,queue='apps_queue',on_message_callback=callback)
body = channel.basic_get(auto_ack=True,queue='apps_queue')
print(body[2])
    #     break
    # except Exception as e:
    #     print(e)
    #     if e.args[0] == 404:
    #         print('队列不存在，新建（申明）')
    #         channel.queue_declare(queue='apps_queue')
# print('1')
# channel.start_consuming()
# print(2)


