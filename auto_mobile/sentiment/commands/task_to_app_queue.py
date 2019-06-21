from cus_rabbitmq.queue_transport import QueueTransport

def task_to_app_queue(spider_name, environment, queue_env):
    """
    线上队列中的关键词任务进入到本地队列
    """
    q_n = 'spider.%(spider_name)s-starttasks.spider' % {'spider_name': spider_name}
    qm = QueueTransport(source_env=environment, source_queue_name=q_n, source_queue_env=queue_env)
    qm.consume(queue_env=queue_env)
