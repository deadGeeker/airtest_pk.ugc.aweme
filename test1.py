# -*- encoding=utf8 -*-
__author__ = "csy"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
import random

auto_setup(__file__)

poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
start_app("com.ss.android.ugc.aweme")

xy = poco.get_screen_size()

x = xy[0]
y = xy[1]
# print(xy)
# swipe((715, 1371), (715, 259))

while True:
    r = random.randrange(1, 3)
    swipe((0.66 * x,  0.71 * y), (0.66 * x, 0.135 * y))
    sleep(r)
    print("随机延时了{}秒".format(r))
