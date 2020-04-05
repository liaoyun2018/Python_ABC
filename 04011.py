import urllib.request


def load_data():
    url = "https://www.baidu.com/"
    response = urllib.request.urlopen(url)
    print(response)
    data = response.read()
    print(data)
    str_data = data.decode("utf-8")  # 编码
    print(str_data)
    with open("baidu.html", "w", encoding="utf-8")as f:
        f.write(str_data)
    str_name = "baidu"
    bytes_name = str_name.encode("utf-8")
    print(bytes_name)


load_data()
