import requests

member_url = 'https://www.yaozh.com/member/'

cookies = 'acw_tc=2f624a3415860048929125885e77cb5639a3840b0ff09296ccfcb4d5eae124; ' \
          'PHPSESSID=a7teg5rti91gefgi34rcjspub3; Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94=1586004902; ' \
          '_ga=GA1.2.176298213.1586004902; _gid=GA1.2.1361882340.1586004902; yaozh_logintime=1586004958; ' \
          'yaozh_user=903296%09hnly16; yaozh_userId=903296; ' \
          'yaozh_jobstatus' \
          '=kptta67UcJieW6zKnFSe2JyXnoaaZ5hnnpqHnKZxanJT1qeSoMZYoNdzbZtamtHR25Kahpyqn26fhtHCpquUrJrOnlNu1HCWlHNZkm1qmZW548b258ff609D55e046e713953447961SlZ2ZmVmgqJ%2BYn4OnoKKdU5ysa2SUcIeVbm%2BXaGKXnpiRlZuYWaCy9ad17ef87b413691bb2d0da2261ed543; _gat=1; Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94=1586004963; yaozh_uidhas=1; yaozh_mylogin=1586004964; acw_tc=2f624a3415860048929125885e77cb5639a3840b0ff09296ccfcb4d5eae124 '

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/80.0.3987.149 Safari/537.36 '
}
#  字典类型

'''
cook_dict = {
"acw_tc":"2f624a3415860048929125885e77cb5639a3840b0ff09296ccfcb4d5eae124",
"PHPSESSID":"a7teg5rti91gefgi34rcjspub3",
"Hm_lvt_65968db3ac154c3089d7f9a4cbb98c94":"1586004902",
"_ga":"GA1.2.176298213.1586004902",
"_gid":"GA1.2.1361882340.1586004902",
"yaozh_logintime":"1586004958",
"yaozh_user":"903296%09hnly16",
"yaozh_userId":"903296",
"yaozh_jobstatus":"kptta67UcJieW6zKnFSe2JyXnoaaZ5hnnpqHnKZxanJT1qeSoMZYoNdzbZtamtHR25Kahpyqn26fhtHCpquUrJrOnlNu1HCWlHNZkm1qmZW548b258ff609D55e046e713953447961SlZ2ZmVmgqJ%2BYn4OnoKKdU5ysa2SUcIeVbm%2BXaGKXnpiRlZuYWaCy9ad17ef87b413691bb2d0da2261ed543",
"_gat":"1",
"Hm_lpvt_65968db3ac154c3089d7f9a4cbb98c94":"1586004963",
"yaozh_uidhas":"1",
"yaozh_mylogin":"1586004964",
"acw_tc":"2f624a3415860048929125885e77cb5639a3840b0ff09296ccfcb4d5eae124",
}
'''
#  拆分字符串
cook_dict = {}
cookies_list = cookies.split('; ')
for cookie in cookies_list:
    cook_dict[cookie.split('=')[0]] = cookie.split('=')[1]

#  字典推导式
#  cook_dict = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookies.split('; ')}
response = requests.get(member_url, headers=headers, cookies=cook_dict)

data = response.content.decode()

with open('04047cookie.html', 'w', encoding='utf-8') as f:
    f.write(data)
