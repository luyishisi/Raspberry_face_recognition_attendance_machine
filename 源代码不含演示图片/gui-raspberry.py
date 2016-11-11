#coding:utf-8
import cv2,os
import subprocess
import time
from pygame.locals import *
import pygame
from sys import exit
button1 = 0
button2 = 0

pygame.init() #初始化pygame
#screen=pygame.display.set_mode([640,480])  #窗口大小：640*480
SCREEN_SIZE = (800,480)
screen = pygame.display.set_mode(SCREEN_SIZE, HWSURFACE | FULLSCREEN | DOUBLEBUF, 32)

screen.fill([255,255,255])#用白色填充窗口
myimage=pygame.image.load('bg.jpg') #把变量myimage赋给导入的图片
screen.blit(myimage,[0,0]) #在100,100的地方画出这个图片（100和100为左部和上部）

#上字体
myimage=pygame.image.load('33.png') #把变量myimage赋给导入的图片
screen.blit(myimage,[400,80]) #在400,100的地方画出这个图片（100和100为左部和上部）
#下字体
myimage=pygame.image.load('44.png') #把变量myimage赋给导入的图片
screen.blit(myimage,[400,350]) #在400,100的地方画出这个图片（100和100为左部和上部）
#按钮１-关
myimage=pygame.image.load('1.png') #把变量myimage赋给导入的图片
screen.blit(myimage,[400,130]) #在400,100的地方画出这个图片（100和100为左部和上部）
#按钮２-开
myimage=pygame.image.load('2.png') #把变量myimage赋给导入的图片
screen.blit(myimage,[400,250]) #在400,100的地方画出这个图片（100和100为左部和上部）
while True:
    begin = time.time()   
    subprocess.call(["raspistill","-w","400","-h","300","-e","jpg","-n","-t","1","-o",'live.jpg'])
    for event in pygame.event.get():#获得事件
        if event.type == QUIT:#退出事件
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.unicode == 'q':
                exit()
        elif event.type ==  pygame.MOUSEBUTTONDOWN:#鼠标点击事件
            pressed_array = pygame.mouse.get_pos()
                    
            if 700<=pressed_array[0]<=800 and 0<=pressed_array[1]<=50:#右上角的退出事件
                exit()                   
            if 400<=pressed_array[0]<=550 and 50<=pressed_array[1]<=200:#这里的值要手动修改变化
                if button1 % 2 == 0:
                    myimage=pygame.image.load('2.png') #把变量myimage赋给导入的图片
                    screen.blit(myimage,[400,130]) #在400,100的地方画出这个图片（100和100为左部和上部）
                    print button1 
                    button1 += 1
                    os.system("cp live.jpg end.jpg")
                else:
                    myimage=pygame.image.load('1.png') #把变量myimage赋给导入的图片
                    screen.blit(myimage,[400,130]) #在400,100的地方画出这个图片（100和100为左部和上部）
                    print button1 
                    button1 += 1
                    
            if 400<=pressed_array[0]<=550 and 250<=pressed_array[1]<=400:#这里的值要手动修改变化
                if button2 % 2 == 0:
                    myimage=pygame.image.load('1.png') #把变量myimage赋给导入的图片
                    screen.blit(myimage,[400,250]) #在400,100的地方画出这个图片（100和100为左部和上部）
                    print button2 
                    button2 += 1

                    #开始查询人脸信息
                    subprocess.call(["python","chaxun.py"])

                   
                else:
                    myimage=pygame.image.load('2.png') #把变量myimage赋给导入的图片
                    screen.blit(myimage,[400,250]) #在400,100的地方画出这个图片（100和100为左部和上部）
                    print button2 
                    button2 += 1


    myimage=pygame.image.load('live.jpg')   # 反复画出当前照片
    screen.blit(myimage,[0,75])           

    #time.sleep(0.05)#休息一下，防止太忙碌

    pygame.display.flip() #刷新画面

    end = time.time()

    print(end-begin)
