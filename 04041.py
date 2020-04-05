import requests

url = 'http://www.baidu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.149 Safari/537.36 '
}
response = requests.get(url, headers=headers)

#  content属性，返回的类型是bytes
data = response.content.decode()
data = response.text
#  text 返回文本str，优先使用content
print(type(data))
