"""
os模块
	os模块主要是对文件、目录的操作
	• 常用方法：
		os.mkdir()：创建目录
		os.removedirs()：删除文件
		os.getcwd()：获取当前目录
        os.path.exists(dir or file)：判断文件或者目录是否存在
"""
import os
import time

# print(os.listdir("./"))
# print(os.getcwd())

# if not os.path.exists("a"):
#     os.mkdir("a")
#
# if not os.path.exists("a/test.txt"):
#
#     f=open("a/test.txt","w")
#     f.write("hello,os using")
#     f.close()
# print(os.listdir("./"))

"""
time模块
"""
print(time.asctime())
print(time.time())
print(time.localtime())
print(time.strftime("%Y-%m-%d %H:%M:%S"))
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# 获取两天前的时间
now = time.time()
two_day_before =  now - 60*60*24*2
time_tuple = time.localtime(two_day_before)
print(time.strftime("%Y-%m-%d %H:%M:%S", time_tuple))