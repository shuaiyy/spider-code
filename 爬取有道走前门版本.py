import requests
import time
import random
import hashlib
ss = requests.Session()

# 合成盐
salt = int(time.time() * 1000) + random.randint(1,9)
n = input('请输入您要翻译的内容')

# 合成sign
sign = 'fanyideskweb' + n + str(salt) + "ebSeFb%=XZ%T[KZ)c(sy!"
mm = hashlib.md5()
mm.update(sign.encode('utf-8'))
sign = mm.hexdigest()

# post表单数据，通过分析只有salt和sign是变动的，通过js代码能够查到加密方法；
formdata = {
"i":n,
"from":"AUTO",
"to":"AUTO",
"smartresult":"dict",
"client":"fanyideskweb",
"salt":salt,
"sign":sign,
"doctype":"json",
"version":"2.1",
"keyfrom":"fanyi.web",
"action":"FY_BY_REALTIME",
"typoResult":"false"
}

# 通过分析需要提交这些头部信息，cookie的值每次都是变动的不一样的，但是服务器并不审查值的具体内容，只要有即可
headers = {
# 'Cookie': 'OUTFOX_SEARCH_USER_ID=-2022895048@10.168.8.76;',
"Cookie":"OUTFOX_SEARCH_USER_ID=1660767496@10.168.8.63; JSESSIONID=aaaWHiSuUEECp5jcWeZiw; OUTFOX_SEARCH_USER_ID_NCOO=1085528731.0395057; fanyi-ad-id=41685; fanyi-ad-closed=1; ___rl__test__cookies=%d" % int(time.time()*1000),
"Referer":"http://fanyi.youdao.com/",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36"
}

# post地址
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
# post返回的数据是json格式的（可以在chrome-network中查看该请求的response），通过解析得到翻译结果，
response = ss.post(url,data=formdata,headers=headers).json()
# print(response)
# 打印翻译结果
print(response["translateResult"][0][0]["tgt"])