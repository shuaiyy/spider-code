#
# 1. 使用进程池完成如下要求:
# 	* 将/usr/lib/python3.5文件夹下的所有py结尾的文件copy到 桌面上的Test文件夹中
# 	* 用多任务（多进程或者多线程）的方式完成Test文件夹中的所有内容复制
# 	* 新的文件夹的名字为“Test-附件”
# 	* 在复制文件的过程中，实时显示复制的进度
"""此项目一共用到了四个模块：
os，获取列表中所有的文件，并且判断路径是否创建
Pool，循环创建多个进程，并且控制同时并发的数量
Queue，获取
"""
import os
from multiprocessing import Pool
from multiprocessing import Process
from multiprocessing import Manager
def copy(oldpath,newpath,queue):
    with open(oldpath,'rb') as old:
        content = old.read()
    with open(newpath,'wb') as new:
        new.write(content)
    queue.put(newpath)


# for
# def process():
#     print()
if __name__ == '__main__':
    p = Pool(10)
    # 新的文件夹路径
    dir = 'C:/Users/Administrator/Desktop/Test-附件'
    if not os.path.exists(dir):
        os.mkdir(dir)
    # 所有文件夹中的文件
    names = os.listdir('C:/Users/Administrator/Desktop/test')
    # print(names)
    path = 'C:/Users/Administrator/Desktop/test'
    queue = Manager().Queue()
    # 在此循环中创建进程，有多少个文件就创建多少个进程
    for name in names:
        oldpath = path + '/' + name
        newpath = dir + '/' + name
        p.apply_async(copy,(oldpath,newpath,queue))
        # copy(oldpath,newpath)

    num = 0
    while True:
        queue.get()
        num = num + 1
        print('\r现在已经复制了%.2d%%' % (num*100/len(names)),end='')
        if num == len(names):
            break
    p.close()
    p.join()
