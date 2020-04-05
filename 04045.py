#  day05
import requests

url = 'http://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.149 Safari/537.36 '
}
free_proxy = {'http': '114.224.210.187:8118'}

response = requests.get(url=url, headers=headers, proxies=free_proxy)

print(response.status_code)

'''
# 发送post请求
data = {
    
}
response = requests.post(url, data=data)
#  内网需要认证
auth = (user, pwd)
response = requests.get(url, auth=auth)
'''
