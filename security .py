""" Python Image security system:

Developer: Saurabh Nerkar

Description: The project consists of two parts one, bash script to control the
operating system part and second, the python part, image processing
and recongization.

Algorithm:
1) Attach the script to the folder
1) As soon as you try to open the folder, the script runs
2) The scripts runs redirects to the python script
3) Python takes a picture, processes it, if match found, the folder is opened.
4) If the photo is not matched, the scipt asks for a password if the password
   matched the folder is opened.
5) Trying to open the folder more than three times will cause the deletion of
   folder
6) Enjoy!! :D

Mounts for information:
echo physics | sudo mount /dev/sda10 /media/m169/
echo physics | sudo mount /dev/sda8 /media/m29/
echo physics | sudo mount /dev/sda7 /media/m18/
echo physics | sudo mount /dev/sda6 /media/m90/
echo physics | sudo mount /dev/sda3 /media/m40/
echo physics | sudo mount /dev/sda2 /media/m84/
"""

import sys
import os
import cv2
from shutil import copyfile
import subprocess
import getpass

camera_port=0
ramp_frames=30
cam=cv2.VideoCapture(camera_port)

def main():
    print("What do you want to do")
    print("1. Add folders to protoct")
    print("2. Remove protection")
    print("3. Add a user")
    print("4. Exit the program")

    a=input()

    if(a==1):
        try:
            path=raw_input("Name of the folder: ")
            print path
            if (os.path.isdir(path)==True):
                print "Directory exists, applying protection, please wait"
                x=path.split('/')
                x[len(x)-1]='.'+x[len(x)-1]
                x='/'.join(x)
                os.rename(path, x)
                fp =open('/home/saurabh/DIP/secure.txt', 'a')
                fp.write(x)
                fp.write('\n')
                fp.close()
                x=path.split('/')
                x[len(x)-1]=x[len(x)-1]+'.desktop'
                x='/'.join(x)
                fp=open(x, 'w')
                y=path.split('/')
                fp.write("#!/usr/bin/env xdg-open\n\n")
                fp.write("[Desktop Entry]\n")
                fp.write("Version=1.0\n")
                fp.write("Type=Application\n")
                fp.write("Terminal=true\n")
                fp.write("Exec=/home/saurabh/DIP/{}.sh\n".format(y[len(y)-1]))
                fp.write("Name={}\n".format(y[len(y)-1]))
                fp.write("Icon=/home/saurabh/DIP/folder.jpg\n")    
                fp.close()
                os.system("chmod +x {}".format(x)) 

                fp = open("/home/saurabh/DIP/{}.sh".format(y[len(y)-1]), 'w')
                fp.write("#!/bin/bash\n\n")
                fp.write("checkvar=$(python /home/saurabh/DIP/face_recognizer/test.py)\n\n")
                fp.write('if [ "$checkvar" == "matched" ]\n')
                fp.write('then\n')
                y[len(y)-1]='.'+y[len(y)-1]
                y='/'.join(y)
                fp.write('nautilus {}\n'.format(y))
                fp.write('else\n')
                fp.write('echo "Unmatch found, please try again!"\n')
                fp.write('fi\n')
                fp.close()
                y=path.split('/')
                
                os.system("chmod +x /home/saurabh/DIP/{}.sh".format(y[len(y)-1]))
                
            else:
                print "The directory does not exists, please try again"
                main()
                
        except:
            pass
            
    if(a==2):
        print("Please insert the path of the folder you want to unprotect.")
        path=raw_input()
        x=path.split('/')
        x[len(x)-1]='.'+x[len(x)-1]
        x='/'.join(x)
        os.rename(x, path)
        x=path.split('/')
        x[len(x)-1]=x[len(x)-1]+'.desktop'
        x='/'.join(x)        
        os.remove("{}".format(x))
        x=path.split('/')
        os.remove("/home/saurabh/DIP/{}.sh".format(x[len(x)-1]))
        print("Protection has been invoked from the specified folder! :)")
        
    if(a==3):
        passkey="physics"
        print("To add an user, please enter the passkey")
        inp=getpass.getpass()
        
        try:
            if(inp == passkey):
                print("Password is correct")
                print("1. Add a photo of the user.")
                print("2. Capture a photo")   
                a=input()

                if(a==1):
                    fp = open('/home/saurabh/DIP/user.txt', 'a')
                    print("Enter the user name and designation number:")
                    name=raw_input()
                    number=raw_input()
                    dest="/home/saurabh/DIP/users/"+"{}".format(name)+"_{}".format(number)+".jpeg"
                    print("Please, enter the path of the image")
                    path=raw_input()
                    copyfile(path, dest)
                    image=cv2.imread(dest)
                    gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    cv2.imwrite(dest, gray_image)
                    print("The image has been acquired.")

                if(a==2):
                    global cam
                    print("Enter the user name and designation number:")
                    name=raw_input()
                    number=raw_input()
                    for i in xrange(ramp_frames):
                        temp=get_image()
                    print("Taking image, pose properly!")
                    image=get_image()
                    image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    cv2.imwrite("/home/saurabh/DIP/users/{}_{}.png".format(name, number), image)
                    del(cam)
                    print("The image has been saved!")

        except IOError:
            print("Incorrect path, please try again")
            main()
            
    if(a==4):
        print ("Exiting the program, thank you!")
        sys.exit(0)

def get_image():
    global cam
    retval, im= cam.read()
    return im

if __name__=="__main__":    
    main()

