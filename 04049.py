import requests

r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(r.json())
#  返回的是json，不是HTML网页
