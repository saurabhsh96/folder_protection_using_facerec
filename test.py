#!/usr/bin/env python

import cv2, os
import numpy as np
from PIL import Image
import sys

cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
recognizer = cv2.createLBPHFaceRecognizer()

cam_port = 0
ramp_frames = 30
cam = cv2.VideoCapture(cam_port)
#y=[]
count=1
def get_images_and_labels(path):
    #global y
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    images = []
    labels = []
    for image_path in image_paths:
        image_pil = Image.open(image_path).convert('L')
        image = np.array(image_pil, 'uint8')
        x=image_path
        x=x.split('/')
        x=x[len(x)-1].split('.')
        #print x
        x=x[0].split('_')
        print x
        #y.append(x)
        nbr = int(x[1])
        faces = faceCascade.detectMultiScale(image)
        for (x, y, w, h) in faces:
            images.append(image[y: y + h, x: x + w])
            labels.append(nbr)
            cv2.imshow("Adding faces to traning set...", image[y: y + h, x: x + w])
            cv2.waitKey(50)
    return images, labels

def facerec():
    a=0
    path = '/home/saurabh/DIP/users/'
    images, labels = get_images_and_labels(path)
    cv2.destroyAllWindows()
    recognizer.train(images, np.array(labels))
    path1 = '/home/saurabh/DIP/clicks'
    image_paths = [os.path.join(path1, f) for f in os.listdir(path1)]
    for image_path in image_paths:
        predict_image_pil = Image.open(image_path).convert('L')
        predict_image = np.array(predict_image_pil, 'uint8')
        faces = faceCascade.detectMultiScale(predict_image)
        for (x, y, w, h) in faces:
            nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w])
            print nbr_predicted, conf
            cv2.imshow("Recognizing Face", predict_image[y: y + h, x: x + w])
            cv2.waitKey(1000)
            if (conf > 30.0):
                cv2.destroyAllWindows()
                a=1
                break
            else:
                a=0
    return a

def capture_photo():
    global cam
    for i in xrange(ramp_frames):
        temp=get_image()
    image = get_image()
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("/home/saurabh/DIP/clicks/click.png", image)
    del(cam)

def get_image():
    global cam
    retval, im=cam.read()
    return im

def main():
    global count
    capture_photo()
    a=facerec()  
    try:
        if(a==1):
            print("The user has been validated, fetching the folder, please wait")
            sys.exit('matched')
        else:
            print("The user is invalid, please try again")
            count = count+1
            if(count>2):
                print("Number of attempts are exhausted, please enter the password.")
                passkey = getpass.getpass()
                if (passkey=="physics"):
                    print("The user is validated, fetching the folder, please wait.")
                    sys.exit('matched')
                else:
                    print("Wrong password. Invalid user, please contact the Batman")
                    sys.exit('unmatched')
            else:
                main()

    except IOError:
        print("Some error occurred! Sorry, please try again! :)")
        sys.exit(0)

if __name__=="__main__":
    main()
