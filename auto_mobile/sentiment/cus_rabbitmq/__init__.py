import json
import random
from .queue_transport import QueueTransport

qt = QueueTransport()


def send_task(clone_task, env, queue_env):
    # name = 'spider.%(spider_name)s-starttasks.spider' % {'spider_name': clone_task['kernelCode']}
    name = 'spider.app-news-detail-starttasks.spider'
    body = json.dumps(clone_task)
    qt.publish(name, env, queue_env, body)


def send_item(clone_task, env, queue_env):
    name = 'spider.items-%(i)s.spider' % {'i': random.choice([1, 2, 3])}
    body = json.dumps(clone_task)
    qt.publish(name, env, queue_env, body)
