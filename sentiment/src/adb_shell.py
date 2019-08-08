# -*- coding: utf-8 -*-
import os
import subprocess
import time


class AutoAdb:
    def __init__(self):
        adb_path = os.path.join('adb')
        print(adb_path)
        try:
            subprocess.Popen(
                [adb_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            self.adb_path = adb_path
        except OSError:
            pass
        else:
            try:
                subprocess.Popen(
                    [adb_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            except OSError:
                pass

    def get_screen(self):
        process = os.popen(self.adb_path + ' shell wm size')
        output = process.read()
        return output

    def run(self, raw_command):
        print(raw_command)
        command = '{} {}'.format(self.adb_path, raw_command)
        print(command)
        process = os.popen(command)
        output = process.read()
        return output

    def test_device(self):
        print('检查设备是否连接...')
        command_list = [self.adb_path, 'devices']
        process = subprocess.Popen(command_list, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = process.communicate()
        if output[0].decode('utf8') == 'List of devices attached\n\n':
            print('未找到设备')
            print('adb 输出:')
            for each in output:
                print(each.decode('utf8'))
            exit(1)
        print('设备已连接')
        print('adb 输出:')
        for each in output:
            print(each.decode('utf8'))

    def test_density(self):
        process = os.popen(self.adb_path + ' shell wm density')
        output = process.read()
        return output

    def test_device_detail(self):
        process = os.popen(self.adb_path + ' shell getprop ro.product.device')
        output = process.read()
        return output

    def test_device_os(self):
        process = os.popen(self.adb_path + ' shell getprop ro.build.version.release')
        output = process.read()
        return output

    def adb_path(self):
        return self.adb_path


if __name__ == '__main__':
    c = AutoAdb()
    while True:
        c.run('shell input swipe 400 817 400 580')
        c.run('shell input tap 570 380')  # 点击一次列表页
        time.sleep(1)
        c.run('shell input tap 570 380')  # 点击一次详情页
        time.sleep(1)
        c.run('shell input keyevent 4')  # 退出
        time.sleep(1)
        c.run('shell input keyevent 4')  # 退出
