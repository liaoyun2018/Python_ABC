import urllib.request


def proxy_user():
    proxy_list = [
        {"http": "218.59.193.14:47138"},
        {"http": "121.237.149.163:3000"},
        {"http": "117.88.177.34:3000"},
        {"http": "121.237.149.118:3000"},
        {"http": "121.237.149.160:3000"}
    ]
    for proxy in proxy_list:
        print(proxy)
        proxy_handler = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxy_handler)

        try:
            opener.open("https://www.baidu.com", timeout=1)
            print("haha")

        except Exception as e:
            print(e)


proxy_user()
'''
 各类handler：
    'Request', 'OpenerDirector', 'BaseHandler', 'HTTPDefaultErrorHandler',
    'HTTPRedirectHandler', 'HTTPCookieProcessor', 'ProxyHandler',
    'HTTPPasswordMgr', 'HTTPPasswordMgrWithDefaultRealm',
    'HTTPPasswordMgrWithPriorAuth', 'AbstractBasicAuthHandler',
    'HTTPBasicAuthHandler', 'ProxyBasicAuthHandler', 'AbstractDigestAuthHandler',
    'HTTPDigestAuthHandler', 'ProxyDigestAuthHandler', 'HTTPHandler',
    'FileHandler', 'FTPHandler', 'CacheFTPHandler', 'DataHandler',
    'UnknownHandler', 'HTTPErrorProcessor',
'''