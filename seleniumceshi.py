from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#上phantomjs的车
driver = webdriver.PhantomJS()
# 请求
driver.get('https://www.douban.com/')
# 截屏
driver.save_screenshot('douban.jpg')
# 输入账号
driver.find_element_by_name('form_email').send_keys('18721053605')
# 输入密码
driver.find_element_by_name('form_password').send_keys('nishijiba22')
# 点击登录
driver.find_element_by_class_name('bn-submit').click()
# 保存登陆后的截图
driver.save_screenshot('douban2.jpg')

