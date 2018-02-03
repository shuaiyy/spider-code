import requests
from aip import AipOcr
# url = 'https://aip.baidubce.com/oauth/2.0/token?'
# grant = 'grant_type=client_credentials&'
# id = 'client_id=XPFfu1PWesIgRou2sMoTIuz5&'
# secret = 'client_secret=1Lq1Uw10sU884hNvN4Vrk2fXjGbSxPvY'
# new_url = url + grant + id + secret
# access_token = requests.post(new_url).json()['access_token']
# print(access_token)
# url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token='
# URL = url + access_token

""" 你的 APPID AK SK """
APP_ID = '10777720'
API_KEY = 'XPFfu1PWesIgRou2sMoTIuz5'
SECRET_KEY = '1Lq1Uw10sU884hNvN4Vrk2fXjGbSxPvY'
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
image = get_file_content('C:/Users/Administrator/Desktop/测试.jpg')
""" 调用通用文字识别（高精度标准版）, 图片参数为本地图片 """
content = client.basicAccurate(image)['words_result']
full = ''
for i in content:
   full = full + i['words'] + '\n'
print(full)

