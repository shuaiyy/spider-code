import sys
from optparse import OptionParser

from .task_to_app_queue import task_to_app_queue
from .run_mitmdump import run_mitmdump


def get_options():
    parser = OptionParser()
    parser.add_option('-e', '--environment', dest='environment', help='choose environment to run',
                      metavar='ENVIRONMENT')
    # 选择程序运行目标，appium for 操作手机，mitmdump for 数据拦截，mq for 队列合并
    parser.add_option('-t', '--type', dest='task_type',
                      help='choose a process to run: appium, mitmdump or mq', metavar='TASK_TYPE')

    # 队列合并，源队列的名称由内核名称构成
    parser.add_option('-s', '--spider', dest='spider_name', help='choose a queue to consume',
                      metavar='SPIDER')

    parser.add_option('-q', '--queue', dest='queue', help='choose meta or search', metavar='QUEUE')

    return parser.parse_args()


def bootstrap():
    (options, args) = get_options()
    # 获取环境
    if not options.environment:
        environment = 'local'
    else:
        environment = options.environment
    # 获取任务类型
    task_type = options.task_type
    # 获取队列环境 meta  or  search
    queue_env = options.queue
    # 获取爬虫名称
    spider = options.spider_name

    if task_type == 'mq':
        task_to_app_queue(spider_name=spider, environment=environment, queue_env=queue_env)

    if task_type == 'mitmdump':
        run_mitmdump(environment=environment, queue_env=queue_env)
