# encoding:utf-8
import requests


def getRandomProxies():
    """
    当启动代理时，系统会匹配url和代理的之间是否匹配
    （如果url是http，代理是https，那么系统不采用代理，使用本机访问，这种也叫裸机模式）
    所以要指定http和https两种类型的代理
    """
    http = requests.get("http://1.12.181.18:5010/get/?type=http").json().get("proxy")
    https = requests.get("http://1.12.181.18:5010/get/?type=https").json().get("proxy")
    proxies = {"http": f"http://{http}", "https": f"https://{https}"}
    return proxies
