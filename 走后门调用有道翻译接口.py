# coding: utf-8
import requests
import time
import hashlib
if __name__== "__main__":
    # m = hashlib.md5()
    d = input('请输入您想翻译的文字：')
    u = 'fanyideskweb'
    # f = str(int(time.time()*1000))
    # c = "rY0D^0'nM0}g5Mm1z%1G4"
    # m.update((u + d + f + c).encode('utf-8'))
    data= {
        'i':d,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':u,
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_ENTER',
        'typoResult':'false'
    }
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Origin':'http://fanyi.youdao.com',
        'Referer':'http://fanyi.youdao.com/'
    }
    # url是核心，这是一个后门，只要url对了，不需要加盐，不需要sign,所以此代码走的是后门
    post_url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=null'
    youdaojson = requests.post(post_url,headers = headers,data=data).json()['translateResult'][0][0]
    print('翻译结果：%s' % youdaojson['tgt'])
