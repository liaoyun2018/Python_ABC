import requests
#  ssl认证
url = 'https://www.12306.cn'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.149 Safari/537.36 '
}
response = requests.get(url, headers=headers, verify=False)  # verify=False 忽略证书访问
data = response.content.decode()
with open('0404612306.html', 'w', encoding='utf-8') as f:  # UnicodeEncodeError: 'gbk' codec
    f.write(data)