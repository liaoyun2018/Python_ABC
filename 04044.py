import json

import requests

url = 'https://api.github.com/user'
#  这个网址返回的不是HTML，而是标准的json
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.149 Safari/537.36 '
}
response = requests.get(url, headers=headers)
# str
data = response.content.decode()
# str--dict
data_dict = json.loads(data)
data = response.json()
#  json 自动将json字符串转换成Python dict list
print(data)
print(data['message'])
