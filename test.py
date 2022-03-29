# encoding:utf-8
import glob
# 取出目录下所有XLSX格式的文件
# ?代表一个字符 *代表多个字符 [a-z]等格式都是适用的
files = glob.glob(r"C:\Users\Administrator\PycharmProjects\QianFuXin\ives\*.xlsx")
# 取出目录下所有路径（文件和文件夹）
files = glob.glob(r"C:\Users\Administrator\PycharmProjects\QianFuXin\ives\**",recursive=True)
print(files)


import tempfile
a=tempfile.gettempdir()
print(a)