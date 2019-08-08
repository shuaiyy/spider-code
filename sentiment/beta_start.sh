#!/usr/bin/env bash
#4条命令通过&合写，启动rabbitmq sever redis server   rabbit和mitmproxy，ｂｅｔａ环境
docker run -d -p 15672:15672 -p 5672:5672 8e69b73e98c9&docker run -d -p 6370:6379 d3e3588af517&python manage.py -s apps-android-search_list-defaultsort -t mq -q meta -e beta &
python manage.py -t mitmdump -q meta -e beta


#nohup python manage.py -t mitmdump -q search -e beta