import urllib.request
import requests


def money_proxy_use():
    #  1.付费代理IP：添加用户名密码进行验证
    # money_proxy = {"http": "username:password@192.168.12.11:8080"}
    # proxy_handler = urllib.request.ProxyHandler(money_proxy)
    # opener = urllib.request.build_opener(proxy_handler)
    # opener.open("http://www.baidu.com")
    #  2.付费代理IP：速度较快
    use_name = "abcname"
    pwd = "123456"
    proxy_money = "123.158.63.130:8080"
    password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    #  add_password(self, realm: str, uri: Union[str, Sequence[str]], user: str, passwd: str)
    password_manager.add_password(None, proxy_money, use_name, pwd)

    handler_auth_proxy = urllib.request.ProxyBasicAuthHandler(password_manager)
    opener_auth = urllib.request.build_opener(handler_auth_proxy)
    response = opener_auth.open("http://www.baidu.com")
    print(response.read())


money_proxy_use()
