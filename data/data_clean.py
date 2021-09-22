# -*- coding: UTF-8 -*-
import time
with open('messages_testset.txt', 'r',encoding='ISO-8859-15') as f:
    f = f.read()
    time_point_all = f.split('\n')
    # print(time_point_all)
    time_points = []
    for times in time_point_all:
        tmp = times[0:19].replace('T',' ')
        timeArray = time.strptime(tmp, "%Y-%m-%d %H:%M:%S")
        timestamp = time.mktime(timeArray)
        timestamp = int(timestamp // 300)
        time_points.append(timestamp)
        print(timestamp)
    
    
    
