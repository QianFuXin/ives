# encoding:utf-8

import random

from xpinyin import Pinyin


def randomPassword(seed):
    seed = 100000000 + int(seed)
    # 字母类型
    englishChar = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'l', 'k', 'j', 'h', 'g', 'f', 'd', 's', 'a', 'z',
                   'x',
                   'c', 'v',
                   'b', 'n', 'm']
    # 数字类型
    numberChar = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    # 符号类型
    symbolChar = ['!', '@', '#', '$']
    passwordCharSet = englishChar.copy() + numberChar.copy() + symbolChar.copy()
    random.seed(seed)
    # 把密码打乱
    random.shuffle(passwordCharSet)

    return "".join(passwordCharSet[:16])


# 获取汉字的首字母
def firstCharacter_pinYin(info):
    pinYinObject = Pinyin()
    transformed = pinYinObject.get_pinyin(info)
    password = ""
    for i in transformed.split("-"):
        password += i[0]
    return password


# 获取汉字的拼音
def pinYin(info):
    p = Pinyin()
    transformed = p.get_pinyin(info).replace("-", "")
    return transformed


print(randomPassword(25))


