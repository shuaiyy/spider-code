import sys
import json
import time
from cus_rabbitmq import send_item
from common import *
from logger import LogHandler

log = LogHandler('mitmproxy')

def response(flow):
    origin_url = flow.request.url
    environment = sys.argv[-1]
    # 抖音
    if 'aweme-hl.snssdk.com' in origin_url:
        print('request URL:' + origin_url)
        # 解析返回json
        response_json = json.loads(flow.response.text)

        # 构建任务
        task_body = get_task(environment, 'douyin_index_lancher')
        task = json.loads(task_body.decode('utf-8'))
        # 获取数据
        video_list = response_json.get('aweme_list')

        #
        for video in video_list:
            video_item = {}

            video_item['uuid'] = video['aweme_id']
            video_item['title'] = '@' + video['author']['nickname']
            video_item['content'] = video['desc']
            video_item['url'] = video['share_url']

            video_item['praiseNum'] = video['statistics']['digg_count']  # 点赞数
            video_item['commentNum'] = video['statistics']['comment_count']  # 评论数
            video_item['forwardNum'] = video['statistics']['share_count']  # 分享数[转发数]
            video_item['author'] = video['author']['nickname']
            video_item['uid'] = video['author']['uid']

            video_item['pubTime'] = video['create_time'] * 1000
            video_item['origin'] = task

            video_item['type'] = 'video'
            video_item['fetchTime'] = int(time.time() * 1000)
            send_item(video_item, environment, 'search')
        #
        #     send_task(video_item, routing_key='spider.items-1.spider')
