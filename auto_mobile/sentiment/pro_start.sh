#!/usr/bin/env bash
#两条命令通过&合写，启动rabbit和mitmproxy　　线上环境
python manage.py -s apps-android-search_list-defaultsort -t mq -q meta -e prod &
python manage.py -t mitmdump -q meta -e prod