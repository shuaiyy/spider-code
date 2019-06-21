#!/usr/bin/env bash
#两条命令通过&合写，启动rabbit和mitmproxy，ｄｅｖ环境
python manage.py -s apps-android-search_list-defaultsort -t mq -q meta -e local &
python manage.py -t mitmdump -q meta -e local


#nohup python manage.py -t mitmdump -q search -e beta