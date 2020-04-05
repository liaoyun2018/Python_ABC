import urllib.request

url = 'https://www.sdfsag.cn'

try:
    response = urllib.request.urlopen(url)

except urllib.request.HTTPError as error:
    print(error.code)

except urllib.request.URLError as error:
    print(error)

#  HTTPError and URLError http的状态码
