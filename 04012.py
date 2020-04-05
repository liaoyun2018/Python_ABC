import urllib.request
import urllib.parse
import string


def get_method_params():
    url = "https://www.baidu.com/s?wd="  # 拼接字符串（汉字）
    name = "美女"
    # https://www.baidu.com/s?wd=%E7%BE%8E%E5%A5%B3
    final_url = url + name  # 包含汉字的网址转译
    print(final_url)
    encode_nwe_url = urllib.parse.quote(final_url, safe=string.printable)
    print(encode_nwe_url)
    response = urllib.request.urlopen(encode_nwe_url)
    print(response)
    data = response.read().decode()
    print(data)
    with open("02-encode.html", "w", encoding="utf-8")as f:
        f.write(data)


get_method_params()
# UnicodeEncodeError: 'ascii' codec can't encode characters in position 10-11: ordinal not in range(128)
# Python是解释型语言，只支持ascii 0-127 ，不支持中文
