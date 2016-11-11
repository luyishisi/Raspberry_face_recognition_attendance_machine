import subprocess
import time

file_number = 0
dir = "/home/pi/images/"

while True:
    file_name = dir + format(file_number,"05d")+".jpg"
    file_number = file_number + 1
    subprocess.call(["raspistill","-w","400","-h","400","-e","jpg","-n","-t","1","-o",file_name])
    subprocess.call(["cp","-f",file_name,dir + "live.jpg"])
    time.sleep(2)
    
