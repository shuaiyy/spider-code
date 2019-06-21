import json


def response(flow):
    origin_request_url = flow.request.url
    if 'http://r.cnews.qq.com/search' in origin_request_url:
        res = json.loads(flow.response.text)
        try:
            for i in res['new_list']['data']:
                if 'channellist' in i:
                    medias = i['channellist']['media']
                    with open('result.txt', 'a') as f:

                        for media in medias:
                            chlid = media.get('chlid')
                            chlname = media.get('chlname')
                            content = '{}---{}\n'.format(chlname,chlid)
                            print('媒体结果：  {}'.format(content))
                            f.write(content)
        except:
            pass
