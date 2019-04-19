import zlib
import base64
import time
import json
import requests

class GetToken:
    def __init__(self,user,password):
        """
        :param user: 你的电话号
        :param password: 你的密码
        """
        self.password = password
        self.user = user

    def BirthToken(self):
        """
        生成加密的token
        :return:
        """
        userdata = '"riskChannel=202&user={}"'.format(self.user).encode()
        sign = base64.b64encode(zlib.compress(userdata)).decode('utf-8')
        now = int(time.time()*1000)
        ip = {
                "rId":"100049",
                "ver":"1.0.6",
                "ts":now,
                "cts":now+906489,#保证比ts大
                "brVD":[290, 375],
                "brR":[
                    [1366, 768],
                    [1366, 728], 24, 24
                ],
                "bI":["https://account.dianping.com/account/iframeLogin?callback=EasyLogin_frame_callback0&wide=false&protocol=https:&redir=http%3A%2F%2Fwww.dianping.com", "https://account.dianping.com/login?redir=http://www.dianping.com"],
                "mT":["220,156", "220,156", "220,157", "219,158", "219,159", "219,161", "219,162", "217,163", "217,165", "215,166", "214,167", "214,169", "213,169", "213,171", "212,172", "211,173", "211,175", "210,177", "210,179", "210,182", "210,184", "210,185", "210,186", "210,188", "210,189", "210,191", "209,193", "208,196", "208,199", "208,200"],
                "kT":["3,INPUT", "2,INPUT", "9,INPUT", "9,INPUT", "8,INPUT", "9,INPUT", "1,INPUT", "2,INPUT", "6,INPUT", "7,INPUT", "1,INPUT", "\\b,INPUT", "\\b,INPUT", "\\b,INPUT", "\\b,INPUT", "6,INPUT", "3,INPUT", "1,INPUT"],
                "aT":["220,156,BUTTON", "100,163,INPUT", "99,160,INPUT", "181,113,INPUT", "275,20,DIV"],
                "tT":[],
                "aM":"",
                "sign":sign
            }
        info = json.dumps(ip, separators=(',', ':')).encode('utf-8')
        token = base64.b64encode(zlib.compress(info)).decode('utf-8')
        token = token.replace('+',' ')
        print(token)
        return token

    def GetPhonecode(self):
        """
        调用发送手机验证码的接口
        :return:
        """
        # 拿到加密参数
        _token = self.BirthToken()
        url = "https://account.dianping.com/account/ajax/checkRisk"
        headers = {'Referer':"https://account.dianping.com/account/iframeLogin?callback=EasyLogin_frame_callback0&wide=false&protocol=https:&redir=http%3A%2F%2Fwww.dianping.com",
                   'Accept-Encoding':'gzip, deflate, br',
                   'Content-type':'application/x-www-form-urlencoded',
                   'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
                   }
        formdata = {
            'riskChannel':'202',
            'user':self.user,
            '_token':_token
        }
        response = requests.post(url,data=formdata,headers=headers)
        # 请求发验证码的接口
        headers.update({'X-Requested-With':'XMLHttpRequest'})
        formdata = {'mobileNo':self.user,
                    'uuid':response.json()['msg']['uuid'],
                    'type':'304',
                    'countrycode':'86'
                    }
        url = 'https://account.dianping.com/account/ajax/mobileVerifySend'
        response = requests.post(url,data=formdata,headers=headers)
        print(response.text)


if __name__ == '__main__':
    gettoken = GetToken('phone','password')
    gettoken.GetPhonecode()


