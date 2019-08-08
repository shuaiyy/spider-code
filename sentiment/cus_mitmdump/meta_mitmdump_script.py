import sys
import gc
import json
from urllib import parse
from cus_rabbitmq import send_task
from common import *
# from logger.log import LogHandler
# log = LogHandler('mitmproxy')


def request_flow_2_dict(flow):
    query_text = flow.request.get_text()
    query_dict = parse.parse_qs(query_text)
    for key in query_dict:
        query_dict[key] = query_dict.get(key)[0]
    return query_dict


def _get_task(pattern, flow, app_name, environment, search_word):
    '''
    根据app关键词从本地redis中获取task,
    该task 在推入本地队列的时候放进去的，
    为了解决爬到的数据必须带有原始任务的特征的问题
    '''
    if 'url' == pattern:
        # 获取请求参数，并将其转为dict
        origin_request_url = flow.request.url
        query_text = origin_request_url.split('?')[1]
    else:
        query_text = flow.request.get_text()
    query_dict = parse.parse_qs(query_text)
    for key in query_dict:
        query_dict[key] = query_dict.get(key)[0]
    # keyword and app_name
    # get task body
    keyword = query_dict[search_word].replace(',','_')
    task_key = '%(app_name)s_%(keyword)s' % {'app_name': app_name, 'keyword': parse.unquote(keyword)}
    task_body = get_task(environment, task_key)
    # print(type(task_body),task_body)
    if not task_body:
        print(task_key)
        return None
    task = eval(task_body.decode('utf-8'))
    return task


def response(flow):
    """
    从mitmproxy拦截的返回数据中提取详情页链接
    提取链接放入解析队列
    :param flow:
    :return:
    """
    environment = sys.argv[-1]
    origin_request_url = flow.request.url
    # try:
    #     res = json.loads(flow.response.text)
    #     # print(res)
    #     with open('json.txt','a')as f:
    #         f.write(origin_request_url+str(res)+'\n')
    # except:
    #     print('解析错误  {}'.format(origin_request_url))
    #

    if '//newsapi.sina.cn/' in origin_request_url and 'index-search' in origin_request_url:  # 新浪
        '''
        1.获取任务体
        2.获取请求数据
        '''
        # 1.获取任务体
        task = _get_task('url', flow, 'sina', environment, search_word='keyword')

        # 2.获取请求数据
        res = json.loads(flow.response.text)
        res_list = res.get('data').get('list')
        # 获取数据体中所有kwy中包含'feed' 的数据
        res_rows = []
        for k in res_list.keys():
            if 'feed' in k:
                if res_list.get(k):
                    res_rows.extend(res_list.get(k))
        seeds = []
        for row in res_rows:
            seeds.append(row.get('url'))
        return _sent_task(task, seeds, environment)

    elif '//a1.go2yd.com/Website/channel/news-list-for-keyword?' in origin_request_url:  # 一点资讯
        task = _get_task('url', flow, 'yidianzixun', environment, search_word='display')

        # 2.获取请求数据
        res = json.loads(flow.response.text)
        result_list = res.get('result', [])
        rows = []
        for result in result_list:
            detail_url = 'http://www.yidianzixun.com/article/' + result.get('docid')
            rows.append(detail_url)
        return _sent_task(task, rows, environment)

    elif '//r.inews.qq.com/search' in origin_request_url:  # 腾讯
        task = _get_task('body', flow, 'tencent', environment, search_word='query')
        res = json.loads(flow.response.text)
        rows = []
        for sec in res.get('secList', []):
            for i in sec.get('newsList', []):
                detail_url = i.get('url')
                rows.append(detail_url)
        return _sent_task(task, rows, environment)

    elif 'api.k.sohu.com/api/search/v5/search.go' in origin_request_url:  # 搜狐
        task = _get_task('url', flow, 'sohu', environment, search_word='keyword')
        res = json.loads(flow.response.text)
        rows = []
        for i in res.get('resultList', []):
            detail_id = i.get('newsId')
            url = 'https://3g.k.sohu.com/t/n' + str(detail_id)
            rows.append(url)
        return _sent_task(task, rows, environment)

    elif '//r.cnews.qq.com/searchByType?' in origin_request_url:  # 天天快报
        task = _get_task('body', flow, 'kuaibao', environment, search_word='query')
        res = json.loads(flow.response.text)
        rows = []
        news_data = res['new_list']['data']
        for news in news_data:
            try:
                detail = news['article']['short_url']
                print(detail)
                rows.append(detail)
            except:
                pass
        return _sent_task(task, rows, environment)

    elif 'app.peopleapp.com/Api/622/HomeApi/searchHotWord' in origin_request_url:  # 人民日报
        task = _get_task('url', flow, 'renmin', environment, search_word='keyword')
        res = json.loads(flow.response.text)
        rows = []
        article_list = res.get('data').get('article_list', [])
        for article in article_list:
            url = article.get('share_url')
            rows.append(url)
        return _sent_task(task, rows, environment)

    # elif '/api/?c=main&act=getArticles&keyword' in origin_request_url:  # ZAKER新闻
    elif '/api/?c=main&act=getArticles&keyword' in origin_request_url:  # ZAKER新闻

        task = _get_task('url', flow, 'zaker', environment, search_word='keyword')
        try:
            res = json.loads(flow.response.text)
            rows = []
            for ids in res.get('data').get('article_ids'):
                rows.append('http://www.myzaker.com/article/' + str(ids))
            return _sent_task(task, rows, environment)
        except:
            print('ZAKER新闻',flow.response.text,'ZAKER新闻')
    else:
        # print('拦截不到任何数据')
        del flow
        return
    # except Exception as e:
    #     print(e)


def _sent_task(task, res_rows, environment, target_kernel_code='news-detail'):
    """
    将详情页链接发送到解析队列
    :param task:
    :param res_rows:
    :param environment:
    :param target_kernel_code:
    :return:
    """
    clone_task = task
    if clone_task:
        clone_task['kernelCode'] = target_kernel_code
        clone_task['keyword'] = None
        clone_task['originUrl'] = None
        for seed_val in res_rows:
            clone_task['seedVal'] = seed_val
            send_task(clone_task, environment, 'meta')
