import urllib.request


def load_baidu():
    url = "https://www.baidu.com/"
    # 添加请求头信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/80.0.3987.149 Safari/537.36 "
    }
    # 创建请求对象
    request = urllib.request.Request(url)
    # 动态的方法添加header的信息，与静态的区别urllib.request.Request(url, headers=headers)
    request.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                     "Chrome/80.0.3987.149 Safari/537.36 ")

    response = urllib.request.urlopen(request)  # 不能在此添加请求头信息，系统无参数
    print(response)
    data = response.read().decode("utf-8")
    #  获取完整的url
    final_url = request.get_full_url()
    print(final_url)

    # print(response.headers)  # 响应头
    # 获取请求头的信息
    request_headers = request.headers
    print(request_headers)
    request_headers = request.get_header("User-Agent")

    with open("02headers.html", "w", encoding="utf-8")as f:
        f.write(data)


#  print（），write（）函数的默认编码不是utf-8，需修改编码方式，否则会报错UnicodeEncodeError

# day02 41分钟
load_baidu()
