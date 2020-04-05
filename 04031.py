import urllib.request
#  先在网站上登录，直接加上cookie代码信息登录
url = 'http://i.baidu.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.149 Safari/537.36 ',
    'Cookie': 'BIDUPSID=56DC19455860CCCCF3655AD9E79AC8DD; PSTM=1585570076; '
              'BAIDUID=56DC19455860CCCC53CD78678FF19F99:FG=1; '
              'BDUSS=41VjVyMUdvbHRKaDlBU1NvZEllTVRwS3NmWGk3eWhoelJJZVE5SWttWjhicWxlRVFBQUFBJCQAAAAAAAAAAAEAAACe'
              '~CsEaG5seTE2AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHzhgV584YFeVm; '
              'BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; PSINO=1; ZD_ENTRY=baidu; '
              'H_PS_PSSID=1461_31169_21078_31186_30908_31228_30824_31085_26350_31164_22158; '
              'PHPSESSID=3jqcasst8mig5dfim6hroc6ga6; Hm_lvt_4010fd5075fcfe46a16ec4cb65e02f04=1585912232; '
              'Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04=1585912232 '

}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
data = response.read()
print(type(data))
#  data类型错误，可将'w'(字符串)改为'wb'(二进制)，或在data后加上decode()
with open('04031.html', 'wb') as f:
    f.write(data)

