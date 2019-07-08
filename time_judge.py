# -*- coding: utf-8 -*-
import time
"""
白天 晚上 睡觉时间 三个时间段的判断
"""
def time_judge():
    ranges = "060000-180000,180000-220000,220000-240000,000000-060000"
    now = time.strptime(time.strftime("%H%M%S"), "%H%M%S")
    ranges = ranges.split(",")
    time_flag = 0
    for range in ranges:
        r = range.split("-")
        if time.strptime(r[0], "%H%M%S") <= now <= time.strptime(r[1], "%H%M%S"):
            if time_flag == 0:
                print('白天')
                return '74'
            elif time_flag == 1:
                print('晚上')
                return '75'
            elif time_flag == 2 or time_flag == 3:
                print('睡觉时间')
                return '25'
        time_flag += 1


