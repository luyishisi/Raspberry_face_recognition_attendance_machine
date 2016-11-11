import os
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
        dir_img =dir_temp+'/'+img_name
        print (dir_img)
        yuan = (name,dir_img)
        PERSONS.append(yuan)
    print (PERSONS)
    
#    c = facepp.File(''))   
