#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# $File: admin.py

API_KEY = '187aa2ee8fc784972b7302f3b31becab'
API_SECRET = 'F1czaFXaRJ5VzRcdVNZppUwJpDg4zjUY'

# 导入系统库并定义辅助函数
import time
from pprint import pformat
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
from facepp import API
import facepp
import os

api = API(API_KEY, API_SECRET)
#face = api.detection.detect(img = facepp.File('3.jpg'))

# 步骤０：人名及其脸部图片,此部分，读取目录下ｐｉｃｔｕｒｅ文件夹，中通过获取每文件夹的路径和名字，完成ＰＥＲＳＯＮＳ字典的构建。

dir = os.getcwd()+'/picture'
a = os.listdir(dir)
print(a)
PERSONS = []
for name in a:
    print (name)
    dir_temp = dir +'/'+name
    b = os.listdir(dir_temp)
    print(b)
    for img_name in b:
        if img_name[-1] != 'g':
            continue         
        dir_img =dir_temp+'/'+img_name
        print (dir_img)
        f = open(dir_temp+'/name.txt')
        a = f.read()
        f.close()
        dir_temp
        yuan = (a,facepp.File(dir_img))
        PERSONS.append(yuan)
print (PERSONS)

# IMAGE_DIR　此部分则是选择出需要进行分析的图片。。管理员模式下不用设置实用。（可能有文件打开错误的ｂｕｇ，如果本身没有end.jpg的话。）
TARGET_IMAGE = facepp.File('end.jpg')

# 步骤1：检测出输入图片中的Face，找出图片中Face的位置及属性

FACES = {name: api.detection.detect(img = url)
        for name, url in PERSONS}

for name, face in FACES.iteritems():
    print_result(name, face)


# 步骤2：引用face_id，创建新的person
for name, face in FACES.iteritems():
    rst = api.person.create(
            person_name = name, face_id = face['face'][0]['face_id'])
    print_result('create person {}'.format(name), rst)


# 步骤3：.创建Group，将之前创建的Person加入这个Group

rst = api.group.create(group_name = 'test')
print_result('创建一个群组－－ｔｅｓｔ', rst)
rst = api.group.add_person(group_name = 'test', person_name = FACES.iterkeys())
print_result('添加人到群组中', rst)


# 步骤4：训练模型
rst = api.train.identify(group_name = 'test')
print_result('开始训练请等待', rst)

# 等待训练完成
rst = api.wait_async(rst['session_id'])
print_result('等待异步训练完成', rst)

'''
# 步骤5：识别新图中的Face
rst = api.recognition.identify(group_name = 'test', img = TARGET_IMAGE)
print_result('recognition result', rst)
print '=' * 60
print 'The person with highest confidence:', \
        rst['face'][0]['candidate'][0]['person_name']
'''
# 最终，删除无用的person和group

#api.group.delete(group_name = 'test')
#api.person.delete(person_name = FACES.iterkeys())



