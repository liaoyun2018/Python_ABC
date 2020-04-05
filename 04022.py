import urllib.request
import random


#  User-Agent：模拟真实的浏览器发送请求
def load_baidu():
    url = "http://www.baidu.com"
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 "
        "Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"
    ]
    #  每次请求的浏览器不一样
    random_user_agent = random.choice(user_agent_list)
    request = urllib.request.Request(url)
    #  增加对应的请求头信息
    request.add_header("User-Agent", random_user_agent)
    #  请求数据
    response = urllib.request.urlopen(request)
    print(request.get_header("User-agent"))


load_baidu()
