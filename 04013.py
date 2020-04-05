import urllib.request
import urllib.parse
import string


def get_params():
    url = "https://www.baidu.com/s?"
# 字典传参 urlopen参数url，data服务器接收的数据

    params = {
        "wd": "中文",
        "key": "zhang",
        "value": "san"

    }
    str_params = urllib.parse.urlencode(params)
    print(str_params)
    final_url = url + str_params
    end_url = urllib.parse.quote(final_url, safe=string.printable)
    response = urllib.request.urlopen(end_url)
    data = response.read().decode("utf-8")
    print(data)


get_params()
