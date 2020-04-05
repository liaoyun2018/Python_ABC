import urllib.request
from http import cookiejar  # 自动保存cookie
from urllib import parse  # 转译

login_url = 'https://passport.csdn.net/login'
#  登录之前登录页的网址，找登录参数
#  后台：get（登录页面），post（登录结果）
#  登录参数
login_from_data = {
    'username': '13781113770',
    'password': 'kfcc164362@',
    # 'formhash': '',  # 前端的隐藏域
    # 'backurl': 'https'
}
#  更改用户名和密码则可登录其他网址
cook_jar = cookiejar.CookieJar()  # 保存cookie
cook_handler = urllib.request.HTTPCookieProcessor(cook_jar)  # HTTPCookieProcessor有cookie功能的处理器
opener = urllib.request.build_opener(cook_handler)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.149 Safari/537.36 '
}
#  参数需要转译；post请求的data是bytes
login_str = parse.urlencode(login_from_data).encode('utf-8')
login_request = urllib.request.Request(login_url, headers=headers, data=login_str)
#  登录成功，cookjar自动保存cookie
opener.open(login_request)
#  代码带着cookie去访问
center_url = 'https://passport.csdn.net/login'
center_request = urllib.request.Request(center_url, headers=headers)
response = opener.open(center_url)
data = response.read().decode()  # bytes-->str

with open('04032.html', 'w') as f:
    f.write(data)
#  反爬，可以多个IP，多个账户，防止封号
