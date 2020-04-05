import requests

#  url = 'http://www.baidu.com/s?wd=美女'  # 参数自动转译
url = 'http://www.baidu.com/s'
params = {
    'wd': '美女'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.149 Safari/537.36 '
}
response = requests.get(url, headers=headers, params=params)
data = response.content.decode()

with open('baidu04043.html', 'w', encoding='utf-8') as f:  # UnicodeEncodeError: 'gbk' codec
    f.write(data)
#  发送post，添加参数
#  requests.post(url, data=(参数{}),json=(参数))
