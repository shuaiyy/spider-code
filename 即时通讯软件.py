import socket
from threading import Thread
import time
def send():
    ip = ('192.168.1.103',8585)
    so = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    while True:
        # time.sleep(1)
        content = input('请输入您想发送的内容：').encode('utf-8')
        so.sendto(content,ip)
        if content == 'exit':
            break
    so.close()
def recieve():
    #创建端口
    ip = ('',8080)
    #创建socket
    so = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    so.bind(ip)
    while True:
        content = so.recvfrom(1024)[0].decode('gbk')
        if content == 'exit':
            break
        print('\n对方发来的消息是：%s' % content)
    so.close()
if __name__ == '__main__':
    # while True:
    """需要注意的是线程的创建不能写在循环内否则同一时间内存在多个发送或者接受的函数对象，那么就会存在同一时间内
    有多个相同端口的存在，这与计算机端口分配原则相冲突"""
    send1 = Thread(target=send)
    recieve1 = Thread(target=recieve)
    recieve1.start()
    send1.start()
    # while True:
    #     zhiling = input('请输入您要执行的执行接受or发送')
    #     if zhiling == '发送':
    # send()
    #     else:
    # recieve()