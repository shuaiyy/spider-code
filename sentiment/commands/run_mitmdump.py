import sys
from mitmproxy.tools.main import mitmdump

def run_mitmdump(environment, queue_env):
    """
    -q参数屏蔽mitmdump自身日志打印，-s 处理脚本
    """
    if queue_env == 'meta':
        sys.argv = [
            '',
            '-p',
            '8888',
            '-q',
            '-s', 'cus_mitmdump/meta_mitmdump_script.py', environment
            # '-s', '/home/app/spider_man_app/cus_mitmdump/meta_mitmdump_script.py', environment

        ]
        mitmdump()
    if queue_env == 'search':
        sys.argv = [
            '',
            '-p',
            '8081',
            '-q',
            '-s', 'cus_mitmdump/search_mitmdump_script.py', environment
        ]
        mitmdump()
