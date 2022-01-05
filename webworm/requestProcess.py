# encoding:utf-8
"""
主要针对以下两种请求
1、request包请求
2、selenium请求
"""
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context
import platform
import os
from bs4 import BeautifulSoup
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
from tqdm import tqdm
from selenium.webdriver import Chrome, ChromeOptions
from ives.webworm.proxies import *
from ives.webworm.header import *


# 请求的响应
def responseWithRequests(url, headers=getRandomHeader(), proxies=getRandomProxies(), params=None):
    try:
        response = requests.get(url.strip(),
                                headers=headers,
                                allow_redirects=True,
                                proxies=proxies,
                                params=params,
                                timeout=10)
        response.raise_for_status()
        return response
    except Exception as exc:
        logging.error(f'bugInfo: {exc}')
        return None


# 获得网页的文本
def getText(url, encoding="utf-8"):
    response = responseWithRequests(url)
    if response:
        response.encoding = encoding
        return response.text
    else:
        return None


# 获得bs4
def getBs4(html, features="html.parser"):
    bs4 = BeautifulSoup(html, features)
    return bs4


# 快速的bs4
def fastBs4(url, encoding="utf-8", features="html.parser"):
    text = getText(url, encoding)
    if text:
        return getBs4(text, features)
    else:
        return None


# 下载文件
def download(url, fileName, headers=getRandomHeader(), proxies=getRandomProxies(), params=None):
    response = responseWithRequests(url, headers=headers, proxies=proxies, params=params)
    fileSize = int(response.headers['Content-Length'])
    if os.path.exists(fileName):
        first_byte = os.path.getsize(fileName)
    else:
        first_byte = 0
    if first_byte >= fileSize:
        logging.info(f"[{fileName}]下载已完成")
        return False
    # 下载失败，第二次下载还可以续上
    headers["Range"] = f"bytes={first_byte}-{fileSize}"
    # 进度条
    pbar = tqdm(
        total=fileSize, initial=first_byte,
        unit='B', unit_scale=True, desc=fileName)
    response = requests.get(url, stream=True, headers=headers, proxies=proxies, params=params)
    with(open(fileName, 'ab')) as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                pbar.update(1024)
    pbar.close()
    logging.info(f"[{fileName}]下载成功")
    return True


def responseWithSelenium(headless=False,
                         chromeDriverPath=r'C:\Users\Administrator\PycharmProjects\QianFuXin\utils\webworm\chromedriver.exe'):
    options = ChromeOptions()
    # # 添加代理
    # proxy = getRandomProxies()
    # if proxies:
    #     # 根据url，自动使用代理
    #     if "https:" in url[:6]:
    #         proxy = proxy["https"][8:]
    #         logging.error(f"使用https代理{proxy}")
    #     else:
    #         proxy = proxy["http"][7:]
    #         logging.error(f"使用http代理{proxy}")
    #     options.add_argument(f'--proxy-server={proxy}')
    # 添加随机头
    options.add_argument(
        f'user-agent="{getRandomHeader()}"')
    # 针对windows和linux的差异性，做出代码更改
    if platform.system() == "Linux":
        # linux默认路径，自动寻址，不需要设置
        chromeDriverPath = "/usr/bin/chromedriver"
        # linux的独有设置
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        options.add_argument("window-size=1024,768")
        options.add_argument("--no-sandbox")
    # windows配置
    else:
        options.headless = headless
    browser = Chrome(chromeDriverPath, options=options)
    return browser
