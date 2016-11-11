#coding=utf-8
import cv2
import cv2.cv as cv
import time 
import subprocess
img = cv2.imread("live.jpg")

 
def detect(img, cascade):
    '''detectMultiScale函数中smallImg表示的是要检测的输入图像为smallImg，
faces表示检测到的人脸目标序列，1.3表示每次图像尺寸减小的比例为1.3，
 4表示每一个目标至少要被检测到3次才算是真的目标(因为周围的像素和不同的窗口大小都可以检测到人脸),
 CV_HAAR_SCALE_IMAGE表示不是缩放分类器来检测，而是缩放图像，Size(20, 20)为目标的最小最大尺寸'''
    rects = cascade.detectMultiScale(img, scaleFactor=1.3,
                                    minNeighbors=5, minSize=(30, 30), flags = cv.CV_HAAR_SCALE_IMAGE)
    if len(rects) == 0:
        return []
    print rects
    rects[:,2:] += rects[:,:2]
    print rects
    return rects
 
#在img上绘制矩形
def draw_rects(img, rects, color):
    for x1, y1, x2, y2 in rects:
        cv2.rectangle(img, (x1, y1), (x2, y2), color, 2)
 
#转换为灰度图
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#直方图均衡处理
gray = cv2.equalizeHist(gray)
 
#脸部特征分类地址，里面还有其他
cascade_fn = '/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml'
 
#读取分类器,CascadeClassifier下面有一个detectMultiScale方法来得到矩形
cascade = cv2.CascadeClassifier(cascade_fn)
  
#通过分类器得到rects
rects = detect(gray, cascade)
print(rects)

#subprocess.call(["cp","-f","live.jpg","end.jpg"])   
#subprocess.call(["python","chaxun.py"])  

if(rects  != []):
    print "检测到人脸，请看摄像头！！ "
    time.sleep(1)
    print "倒计时：1"
    time.sleep(1)
   
    #subprocess.call(["raspistill","-w","400","-h","400","-e","jpg","-n","-t","1","-o","end.jpg"])
    subprocess.call(["cp","-f","live.jpg","end.jpg"])   
    img = cv2.imread("end.jpg")
    print "正在进行ｏｐｅｎｃｖ分析处理！！ "
    #转换为灰度图
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #直方图均衡处理
    gray = cv2.equalizeHist(gray)
    #通过分类器得到rects
    rects = detect(gray, cascade)
    
#    vis = img.copy()
    #vis为img副本

    #画矩形
#    draw_rects(vis, rects, (0, 255, 0))
 
#    cv2.imshow('facedetect', vis) 

#    cv2.waitKey(1)#这里如果是０则不会自动执行到下面。
    
    #经过３秒后关闭画面

#    cv2.destroyAllWindows()

    if(rects  != []):
        print ("正在进行人脸识别检测，根据网络情况时间不同，请稍等片刻")
        subprocess.call(["python","chaxun.py"])  
        print ("end!!!３秒后自动关闭窗口")
    else:
        print("没有检测到人脸，返回监控状态")
   




