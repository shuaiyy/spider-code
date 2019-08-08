"""
抖音首页划屏,只对应一台专属手机
"""
from src.adb_shell import AutoAdb
import time

device = '18590ce37d22'

c = AutoAdb()


def tikttok_start():
    c.run('-s {} shell am start -n com.ss.android.ugc.aweme/.splash.SplashActivity'.format(device))
    time.sleep(10)
    c.run('-s {} shell input tap 200 1275'.format(device))
    c.run('-s {} shell input tap 200 1275'.format(device))
    c.run('-s {} shell input tap 200 1050'.format(device))
    for i in range(100):
        c.run('-s {} shell input swipe 400 900 400 300'.format(device))
    c.run('-s {} shell pm clear com.ss.android.ugc.aweme'.format(device))

if __name__ == '__main__':
    while True:
        tikttok_start()