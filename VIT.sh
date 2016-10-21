#!/bin/bash

checkvar=$(python /home/saurabh/DIP/face_recognizer/test.py)

if [ "$checkvar" == "matched" ]
then
nautilus /media/m169/.VIT
else
echo "Unmatch found, please try again!"
fi
