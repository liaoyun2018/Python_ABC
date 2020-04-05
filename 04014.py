import urllib.request


def load_baidu():
    url = "https://www.baidu.com/"
# 创建请求对象
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    print(response)
    data = response.read().decode("utf-8")

    # print(response.headers)  # 响应头
    # 获取请求头的信息
    request_headers = request.headers
    print(request_headers)
    with open("02headers.html", "w")as f:
        f.write(data)


load_baidu()
