### 前言
本次项目使用AirtestIDE和辅助工具adb来测试安卓模拟器中的app 
我选用的安卓模拟器是雷电模拟器，并且我已经在模拟器中预先安装了抖音app
关于AirtestIDE环境的搭建以及Android SDK的安装，可以自行网上查阅，
  
##### 明确功能  
本次项目想要构建脚本来模拟用户抖音刷视频的操作 

##### 步骤实现  
1. 明确测试对象的包名  
+ 采用使用adb指令来获取
+ 可以使用adb中罗列应用或者是抓取日志的方法来获取
+ 如果使用罗列应用的方法，可以在cmd中键入命令：adb shell pm list packages
+ 如果使用抓取日志的方法，可以在cmd中键入命令：adb shell logcat
+ 使用罗列应用的方法会输出一堆包名，无法快速定位，这里我才用了第二种方法
+ 键入adb shell logcat | findstr START && 在模拟器中打开抖音app  
  
2. 定位滑动操作路径  
+ 使用poco的get_screen_size方法去得到当前屏幕的分辨率  
+ get_screen_size方法会返回一个列表[x, y]，x代表的是屏幕的宽度，y代表的是屏幕的长度  
+ 使能airtest中的实时坐滑动路径，得到实时坐标值，带入坐标值到swipe方法，运行代码，  
+ 看是否划到了下一个视频，是的话进入下一步，否的话回到上一步继续规划路径  
+ 将坐标值与当前屏幕分辨率进行比较得出滑动路线的相对路径，这一步的目的是使我的滑动操作能够适配不同屏幕分辨率的手机  
  
3. 为了让我的操作更贴近用户，把滑动操作加入随机特性  
+ 引入了随机函数random
+ 引入了sleep()方法  
  
##### 编写bat脚本  
这部分内容可以自行查阅资料，以下仅供参考
@echo off  
D:  
cd D:\AirtestIDE\app_test_prj  
start airtest run test1.air  
exit  
