configs = {
    'real_params_for_connection': {
        'socket_timeout': 600,
        'heartbeat': 600,
        'blocked_connection_timeout': 30,
        'connection_attempts': 1,
        'retry_delay': 10
    },
    # 本地连接app任务队列
    # 'app_spider_queue_server': {
    #     # RabbitMQ Meta
    #     'meta': {
    #         'account': 'guest',
    #         'password': 'guest',
    #         'host': '127.0.0.1',
    #         'port': 5672,
    #     },
    #     # RabbitMQ Search Engine
    #     'search': {
    #         'account': 'guest',
    #         'password': 'guest',
    #         'host': '127.0.0.1',
    #         'port': 12764,
    #     }
    # },
    'local': {
        # RabbitMQ Meta
        'meta': {
            'account': 'guest',
            'password': 'guest',
            'host': '192.168.1.209',
            'port': 12673,
        },

        # RabbitMQ Search Engine
        'search': {
            'account': 'guest',
            'password': 'guest',
            'host': '192.168.1.209',
            'port': 12674,
        }
    },
    'dev': {
        # RabbitMQ Meta
        'meta': {
            'account': 'guest',
            'password': 'guest',
            'host': '192.168.0.103',
            'port': 10672,
        },

        # RabbitMQ Search Engine
        'search': {
            'account': 'guest',
            'password': 'guest',
            'host': '192.168.0.104',
            'port': 10672,
        }
    },
    'beta': {
        # RabbitMQ Meta
        'meta': {
            'account': 'themis',
            'password': 'themis@123',
            'host': '192.168.1.209',
            'port': 32672,
        },

        # RabbitMQ Search Engine
        'search': {
            'account': 'guest',
            'password': 'beta',
            'host': '192.168.1.209',
            'port': 30673,
        }
    },
    'prod': {
        # RabbitMQ Meta
        'meta': {
            'account': 'guest',
            'password': '1datainfo',
            'host': '192.168.1.209',
            'port': 13674,
        },

        # RabbitMQ Search Engine
        'search': {
            'account': 'guest',
            'password': '1datainfo',
            'host': '192.168.1.56',
            'port': 13675,
        }
    }

}
