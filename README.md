### 开机更换壁纸

#### 简介

![](https://bing.panghai.top/php/today.php)

​		必应搜索每日都会有一张精美的图片，我们可以每次开机设置最新壁纸到电脑背景

#### 前提

​		1、需拥有python环境

​		2、需要在有网络环境下运行

​    	3、最好先单独执行set_today_background.py，执行错误则需要pip安装以上导入的包

#### 使用说明

##### 开机自动下载壁纸并设置电脑背景

1、克隆项目

```yml
git clone git@github.com:flow2000/set-today-background.git
```

2、编辑set_today_background.py的root_path路径，编辑start.bat中path路径（python安装路径）和python文件路径

3、将set_today_background.py放入图片文件中，start.bat放入C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp，开机重启验证即可

​		至此已实现客户端开机自动下载壁纸并设置电脑背景的需求（有网的情况下）。该方法有一个缺陷：当开机后没有联网运行set_today_background.py会导致下载壁纸失败。可以在start.bat中python xxx.py前加入

```bat
timeout 60
```

60是秒数，可自行设置时长，限定时间内自行连上网即可