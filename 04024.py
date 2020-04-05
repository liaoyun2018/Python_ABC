import urllib.request


def create_proxy_handler():
    url = "https://blog.csdn.net/qq_31598771/article/details/83180500"
    #  添加代理
    proxy = {
        #  "http": "http://120.77.249.46:8080"  # 免费的代理IP，可改端口
        "http": "120.77.249.46:8080"  # 不同写法，作用同上
        #  "http": "xiaoming": 123@115  #  付费代理IP代码
    }
    #  代理处理器
    proxy_handler = urllib.request.ProxyHandler(proxy)
    opener = urllib.request.build_opener(proxy_handler)
    data = opener.open(url).read()
    print(data)


create_proxy_handler()
