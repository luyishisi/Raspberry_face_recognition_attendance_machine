#coding:utf-8
# $File: hello.py

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

api = API(API_KEY, API_SECRET)
#face = api.detection.detect(img = facepp.File('3.jpg'))
# 人名及其脸部图片
#IMAGE_DIR = 'http://www.urlteam.org/wp-content/uploads/2016/02/3.jpg'
#facepp.File('3.jpg') 
import os
path=r'./picture'
fns=[os.path.join(root,fn) for root,dirs,files in os.walk(path) for fn in files]
for f in fns:
    print(f)
    
print(len(fns))
PERSONS = [
    (u'雅新', facepp.File('picture/yaxin/1.jpg') ),
    (u'雅新', facepp.File('picture/yaxin/2.jpg') ),
    (u'许娜', facepp.File('picture/xuna/1.jpg') ),
    (u'许娜', facepp.File('picture/xuna/2.jpg') ),
    (u'陆毅', facepp.File('picture/luyi/1.jpg') ),
    (u'其道', facepp.File('picture/qidao/1.jpg') ),
    (u'其道', facepp.File('picture/qidao/2.jpg') ),
    (u'其道', facepp.File('picture/qidao/3.jpg') ),
]
TARGET_IMAGE = facepp.File('picture/1/3.jpg')# IMAGE_DIR 
# 步骤1：检测出三张输入图片中的Face，找出图片中Face的位置及属性

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
print_result('create group', rst)
rst = api.group.add_person(group_name = 'test', person_name = FACES.iterkeys())
print_result('add these persons to group', rst)

# Step 4: train the model
# 步骤4：训练模型
rst = api.train.identify(group_name = 'test')
print_result('train', rst)
# 等待训练完成
rst = api.wait_async(rst['session_id'])
print_result('wait async', rst)

# 步骤5：识别新图中的Face
rst = api.recognition.identify(group_name = 'test', img = TARGET_IMAGE)
print_result('recognition result', rst)
print '=' * 60
print 'The person with highest confidence:', \
        rst['face'][0]['candidate'][0]['person_name']

# 最终，删除无用的person和group
api.group.delete(group_name = 'test')
api.person.delete(person_name = FACES.iterkeys())

