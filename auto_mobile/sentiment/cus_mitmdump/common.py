import redis

redis_connect_dev = redis.StrictRedis(host='127.0.0.1', port=6370, db=0)
redis_connect_beta = redis.StrictRedis(host='127.0.0.1', port=6370, db=0)
redis_connect_prod = redis.StrictRedis(host='127.0.0.1', port=6370, db=0)


def get_task(environment, task_key):
    """
    redis中获取task_assignment保存的任务
    :param environment:
    :param task_key: app与关键词组成的key
    :return:
    """
    if environment in ['local', 'dev']:
        task_body = redis_connect_dev.get(task_key)
    elif environment in ['beta']:
        task_body = redis_connect_beta.get(task_key)
    else:
        task_body = redis_connect_prod.get(task_key)
    return task_body
