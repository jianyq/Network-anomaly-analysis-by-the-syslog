# -*- coding: UTF-8 -*-
import time
path1 = 'messages_trainset.txt'
path2 = 'messages_testset.txt'
check = {'rsyslogd':0,'CH-CH-XSK1B-3F01-R02C03U12-5GC-SVR-0017-HW2288V5':0,'kernel':0,'uvp_hotpatch_status':0,'MONITOR':0,'cloud_agent':0,'ntpd':0,'systemd':0,'sh':0,'logrotate':0,'gcn_hotpatch_status':0,'yum':0,'libstorage-list':0,'haveged':0,'smartd':0,'kbox':0,'kdumpctl':0,'？？？':0,'vBMC_agentd':0,'sftp-server':0,'[/bin/bash]':0,'dracut':0,'openipmi-helper':0}
def time_point(times):
    tmp = times[0:19].replace('T',' ')
    timeArray = time.strptime(tmp, "%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(timeArray)
    timestamp = int(timestamp // 300)
    # time_points.append(timestamp)
    # print(timestamp)
    timestamp = str(timestamp)
    return timestamp 

def patternsearch(times):
    # print(times[34])
    if times[34] == 's':# rsyslogd
        check['rsyslogd'] += 1
        return '1'
    if times[34] == 'H':# CH-CH-XSK1B-3F01-R02C03U12-5GC-SVR-0017-HW2288V5
        check['CH-CH-XSK1B-3F01-R02C03U12-5GC-SVR-0017-HW2288V5'] += 1
        return '2'
    if times[34] == 'e':# kernel
        check['kernel'] += 1
        return '3'
    if times[34] == 'v':# uvp_hotpatch_status
        check['uvp_hotpatch_status'] += 1
        return '4'
    if times[34] == 'O':# MONITOR
        check['MONITOR'] += 1
        return '5'
    if times[34] == 'l':# cloud_agent
        check['cloud_agent'] += 1
        return '6'
    if times[34] == 't':# ntpd
        check['ntpd'] += 1
        return '7'
    if times[34] == 'y':# systemd
        check['systemd'] += 1
        return '8'
    if times[34] == 'h':# sh
        check['sh'] += 1
        return '9'
    if times[34] == 'o':# logrotate
        check['logrotate'] += 1
        return '0'  
    if times[34] == 'c':# gcn_hotpatch_status
        check['gcn_hotpatch_status'] += 1
        return '!'
    if times[34] == 'u':# yum
        check['yum'] += 1
        return '@'
    if times[34] == 'i':# libstorage-list
        check['libstorage-list'] += 1
        return '#'

    '''

    especially in test

    '''
    if times[34] == 'a':# haveged
        check['haveged'] += 1
        return '$'
    if times[34] == 'm':# smartd
        check['smartd'] += 1
        return '%'
    if times[34] == 'b':# kbox
        check['kbox'] += 1
        return '^'
    if times[34] == 'd':# kdumpctl
        check['kdumpctl'] += 1
        return '&'
    if times[35] == ']':# ???
        check['???'] += 1
        return '*'
    if times[34] == 'B':# vBMC_agentd
        check['vBMC_agentd'] += 1
        return '('
    if times[34] == 'f':# sftp-server
        check['sftp-server'] += 1
        return ')'
    if times[34] == '/':# [/bin/bash]
        check['[/bin/bash]'] += 1
        return '_'
    if times[34] == 'r':# dracut
        check['dracut'] += 1
        return '+'
    if times[34] == 'p':# openipmi-helper
        check['openipmi-helper'] += 1
        return 'q'
    

def errortest(times):
    list1 = ['Product          : EulerOS', 'Soft version     : EulerOS_V200R002C20', 'Frame No         : 1', 'Slot No          : 0', 'Location No      : 0', 'Hardware version : Unknown']
    if times in list1:
        return 1
    return 0

with open(path1, 'r',encoding='ISO-8859-15') as f:
    f = f.read()
    time_point_all = f.split('\n')
    # print(time_point_all)
    time_points = []
    for times in time_point_all:
        if errortest(times):
            print('error')
            continue
        try:
            a = time_point(times)
            b = patternsearch(times)
            # print(a + ' ' + b)
            time_points.append(a + ' ' + b)
        except:
            # print(times[34])
            print(times)
            # exit()
    print(str(check))
    # for items in time_points:
    #     print(items)
	