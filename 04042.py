import requests


class RequestSpider(object):
    def __init__(self):
        url = 'http://www.baidu.com'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/80.0.3987.149 Safari/537.36 '
        }
        self.response = requests.get(url, headers=headers)

    def run(self):
        data = self.response.content
        #  获取请求头，响应头，状态码，请求cookie，响应cookie
        request_headers = self.response.request.headers
        print(request_headers)
        response_headers = self.response.headers
        print(response_headers)
        code = self.response.status_code

        request_cookie = self.response.request._cookies
        print(request_cookie)


RequestSpider().run()


'''
# 1.记得安装 第三方 模块 requests
# pip install requests


import requests


class RequestSpider(object):
    def __init__(self):
        url = 'https://www.baidu.com'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'
        }
        self.response = requests.get(url, headers=headers)

    def run(self):
        data = self.response.content

        # 1.获取请求头
        request_headers = self.response.request.headers

        # 2.获取相应头
        coderesponse_headers = self.response.headers

        # 3.响应状态码
        code = self.response.status_code

        # 4. 请求的cookie 注意写法
        request_cookie = self.response.request._cookies
        print(request_cookie)

        # 5. 响应的cookie
        response_cookie = self.response.cookies

        print(response_cookie)


RequestSpider().run()

'''