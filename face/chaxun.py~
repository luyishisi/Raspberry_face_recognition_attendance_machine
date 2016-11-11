#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: chaxun.py

API_KEY = '187aa2ee8fc784972b7302f3b31becab'
API_SECRET = 'F1czaFXaRJ5VzRcdVNZppUwJpDg4zjUY'

# 导入系统库并定义辅助函数
import time
from pprint import pformat
from facepp import API
import facepp
import os
#此部分是为了中文的处理
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def print_result(hint, result):
    def encode(obj):
        if type(obj) is unicode:
            return obj.encode('utf-8')
        if type(obj) is dict:
            return {encode(k): encode(v) for (k, v) in obj.iteritems()}
        if type(obj) is list:
            return [encode(i) for i in obj]
        return obj
    print hint
    result = encode(result)
    print '\n'.join(['  ' + i for i in pformat(result, width = 75).split('\n')])

# 首先，导入SDK中的API类,还有本地文件读取所需要的ｆａｃｅｐｐ类


api = API(API_KEY, API_SECRET)
#face = api.detection.detect(img = facepp.File('3.jpg'))

# IMAGE_DIR　此部分则是选择出需要进行分析的图片。。管理员模式下不用设置实用。（可能有文件打开错误的ｂｕｇ，如果本身没有end.jpg的话。）
TARGET_IMAGE = facepp.File('end.jpg')
print ("已经读取图片，正在进行人脸识别，根据网络环境速度不定。")
#识别end.jpg图中的Face
rst = api.recognition.identify(group_name = 'test', img = TARGET_IMAGE)
#print_result('识别结果:', rst)

print '=' * 60
print '识别结果最匹配的对象为:', \
        rst['face'][0]['candidate'][0]['person_name']
a = rst['face'][0]['candidate'][0]['person_name']

print ("正在写入kaoqin.txt中,当前时间为："+" "+ time.asctime())
print '=' * 60
fp = open("kaoqin.txt",'a')
fp.write("姓名:"+" "+rst['face'][0]['candidate'][0]['person_name']+"签到时间:"+" "+time.asctime()+"\n")
fp.close()


# 最终，删除无用的person和group
#api.group.delete(group_name = 'test')
#api.person.delete(person_name = FACES.iterkeys())



