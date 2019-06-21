"""
    多个Appium服务根据当前设备手机数量启动
    指定Appium端口，bp端口以及服务对应手机设备号
"""
import os
import subprocess
import re
import yaml
from multiprocessing import Pool

setting = yaml.load(open('../config/appium.yaml'))
adb_commands = 'adb devices'
devices_list = os.popen(adb_commands)


def start_server(start_command):
    subprocess.run(start_command, shell=True)


def multi_servers():
    """
    读取当前adb设备号，根据设备数量开启appium相应端口
    :return:
    """
    for i in devices_list.readlines()[1:-1]:
        try:
            device = re.search('(.*?)	device', i).group(1)
        except:
            print('f{i}')
            continue
        start_command = 'appium -p {} -U {} -bp {}'.format(setting["port"],device,setting["bootstrap_port"])

        setting['bootstrap_port'] += 2
        setting['port'] += 2
        yield start_command


if __name__ == '__main__':
    pool = Pool(10)
    pool.map(start_server, multi_servers())
    pool.close()
    pool.join()
