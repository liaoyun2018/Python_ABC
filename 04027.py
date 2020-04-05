import urllib.request


#  内网爬取数据
def auth_nei_wang():
    use_name = "admin"
    pwd = "123456"
    nei_url = "http://192.168.63.130"
    #  创建密码管理器
    pwd_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    pwd_manager.add_password(None, nei_url, use_name, pwd)
    #  创建认证处理器
    auth_handler = urllib.request.ProxyBasicAuthHandler(pwd_manager)
    opener = urllib.request.build_opener(auth_handler)
    response = opener.open(nei_url)
    print(response)


auth_nei_wang()
