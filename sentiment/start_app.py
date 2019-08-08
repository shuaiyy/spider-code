"""
解决手机群控问题，每个进程控制一台手机，在设备不超过１０个的前提下线程池默认１０，超过需要调参
"""
from multiprocessing import Pool
from spiders.tasks_assignment import start_consume,port_list

if __name__ == '__main__':
    pool = Pool(10)
    # 每个进程启动一个独立的rabbit链接,独立消费，独立绑定一个设备爬虫
    pool.map(start_consume, port_list())
    pool.close()
    pool.join()