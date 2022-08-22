import ctypes
import datetime
import time
import os
import json
import logging
import requests
import urllib.request

"""

Date: 2022-8-10
Author: 庞海
Description: 下载今日壁纸并保存到指定路径

使用方法: 
    1、只需修改本程序保存绝对路径root_path和start.bat的python安装路径和本程序存放路径 
    2、将start.bat放到C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp
    3、每次开机就会自动运行start.bat从而运行python程序更换壁纸
注意：
    1、本程序需要在有网络环境下运行
    2、最好先单独执行set_today_background.py 执行错误则需要pip安装以上导入的包

"""
# 参照下面格式填写本程序保存绝对路径
root_path="D:/壁纸/"
# 当前年份 例如：2022
year = time.strftime('%Y', time.localtime())
# 图片保存路径
save_path=root_path+"/storage/bing/"+year+"/"
# 日志配置
logging.basicConfig(format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.INFO,
                    filename=root_path+'/access.log',
                    filemode='a')

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}

# 创建壁纸保存文件夹
if not os.path.exists(save_path):
    os.makedirs(save_path)
    logging.info(save_path+"+创建成功")

# 下载今日壁纸
url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"
r = requests.get(url, headers=headers)
text = r.text
data = json.loads(text)
img_url = "https://cn.bing.com/"+data["images"][0]["url"]
str1 = img_url.split("th?id=")[1]
str2 = str1.split("1920x1080.jpg")[0]
filepath = save_path+str2+"UHD.jpg"

# 如果已经下载了则跳过下载
if not os.path.exists(filepath):
    logging.info("保存路径："+filepath)
    urllib.request.urlretrieve(img_url, filename=filepath)
else:
    logging.info("已存在："+filepath)

# 设置今日壁纸
ctypes.windll.user32.SystemParametersInfoW(20, 0, filepath, 3)