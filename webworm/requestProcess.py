# encoding:utf-8
"""
主要针对以下两种请求
1、request包请求
2、selenium请求
"""
import logging
logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
import platform
import os
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
from bs4 import BeautifulSoup
from tqdm import tqdm
from selenium.webdriver import Chrome, ChromeOptions
from ives.webworm.header import *
import requests


# 用requests包的请求网页
def requestPageWithRequests(url, headers=getRandomHeader()):
    try:
        response = requests.get(url.strip(),
                                headers=headers,
                                allow_redirects=True,
                                timeout=10)
        response.raise_for_status()
        return response
    except Exception as exc:
        logging.error(f'异常信息: {exc}')
        return None


# 获得网页的文本
def getText(url, encoding="utf-8"):
    response = requestPageWithRequests(url)
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
def downloadFile(url, fileName, headers=getRandomHeader()):
    response = requestPageWithRequests(url, headers=headers)
    fileSize = int(response.headers['Content-Length'])
    if os.path.exists(fileName):
        first_byte = os.path.getsize(fileName)
    else:
        first_byte = 0
    if first_byte >= fileSize:
        logging.info(f"[{fileName}]下载已完成")
        return False
    headers["Range"] = f"bytes={first_byte}-{fileSize}"
    # 进度条
    pbar = tqdm(
        total=fileSize, initial=first_byte,
        unit='B', unit_scale=True, desc=fileName)
    # 下载
    response = requests.get(url, stream=True, headers=headers)
    with(open(fileName, 'ab')) as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                pbar.update(1024)
    pbar.close()
    logging.info(f"[{fileName}]下载成功")
    return True


def requestPageWithSelenium(headless=False, chromeDriverPath=r'D:\谷歌浏览器驱动\chromedriver.exe'):
    options = ChromeOptions()
    if platform.system() == "Linux":
        chromeDriverPath = "/usr/bin/chromedriver"
        options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument("--no-sandbox")
    else:
        options.headless = headless
    browser = Chrome(chromeDriverPath, options=options)
    return browser
