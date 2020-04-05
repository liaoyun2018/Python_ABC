#  IP代理：免费的代理时效性差，错误率高；付费的贵，也有失效不能用
#  IP分类：透明（对方知道我们真实IP）；匿名（不知道真实IP，但知道使用了代理）；高密
import urllib.request


def handler_openner():
    #  系统的urlopen没有添加代理的功能，所以需要自定义，使用handler处理器，种类很多
    #  安全 套接层，ssl第三方的CA数字证书,HTTP使用80端口，HTTPS使用443端口
    url = "https://blog.csdn.net/qq_31598771/article/details/83180500"
    #  创建自己的处理器
    handler = urllib.request.HTTPHandler()
    #  创建自己的opener,请求数据
    opener = urllib.request.build_opener(handler)
    response = opener.open(url)
    data = response.read()
    print(response)
    print(data)


'''    
global _opener
    if cafile or capath or cadefault:
        import warnings
        warnings.warn("cafile, capath and cadefault are deprecated, use a "
                      "custom context instead.", DeprecationWarning, 2)
        if context is not None:
            raise ValueError(
                "You can't pass both context and any of cafile, capath, and "
                "cadefault"
            )
        if not _have_ssl:
            raise ValueError('SSL support not available')
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH,
                                             cafile=cafile,
                                             capath=capath)
        https_handler = HTTPSHandler(context=context)
        opener = build_opener(https_handler)
    elif context:
        https_handler = HTTPSHandler(context=context)
        opener = build_opener(https_handler)
    elif _opener is None:
        _opener = opener = build_opener()
    else:
        opener = _opener
    return opener.open(url, data, timeout)

'''

handler_openner()
