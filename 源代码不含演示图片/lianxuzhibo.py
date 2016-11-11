import subprocess
import time

#file_number = 0

while True:
    #file_name = dir + format(file_number,"05d")+".jpg"
    a = time.time()
    #file_number = file_number + 1
    subprocess.call(["raspistill","-w","600","-h","600","-e","jpg","-n","-t","1","-o",'live.jpg'])
    print ("wait----")
    subprocess.call(["python","opencv.py"])
    b = time.time()
    print (b-a)
    
