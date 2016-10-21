# folder_protection_using_facerec
This project is designed to get rid of folder protection using encryption and passwords. The core ides is using face recognition to protect folders in operating system. 

Python Libraries used:
OpenCV
PIL
getpass
sys
OS
shutil, copyfile

Basic Algorithm:
1)	Mount the drives as soon as the computer is started. A bash script is automated to do this task. To start anything at a computer restart in Linux, the corresponding bash command must be saved in ./config/autostart folder which is hidden in /home/user folder.
2)	The mounting is done using mount command in bash scripting. (Check mount.sh file in the report)
3)	There are four main parts of the software viz., security (check security,py file in report), this parts lets the user to add the folder in the protection list, create a new user profile and remove a folder from protection. The second part is face recognizer (check face_recognizer.py file in report), this code runs as soon a protected folder is tried to access, this scripts takes the pictures, compares it with training set and gives a result, if the image matches to the user stored, the folder opens up otherwise the folder is not opened. <.desktop file> (Check demo .desktop file in the report) is used to manipulate the operating system parameters. Mount and <folder.sh> (check demo files given in the report) are used to make sure that process goes as expected.
4)	Security script is independent of others. 
5)	As soon as a folder is added to the path, a desktop launcher is created and placed instead of the folder and the folder is hided with special permissions to access.
6)	A bash file with folders name is also created, this will launch the desired application after the double click.
7)	Face Recognizer is used to train and recognize faces and give results.

Face Recognizer:
1)	As soon as a person clicks on a protected folder, the launcher launches the .desktop file corresponding to the folder the person is trying to access. Example, there is a folder in /media/m169/ named VIT, if a person clicks on the folder VIT, the script named VIT.desktop is launched which launched VIT.sh file.
2)	The script VIT.sh then launches the python script named face_recongnizer.py. 
3)	This python script has three main parts viz., training, clicking photos and recognizing.
4)	A training dataset is stored in a particular location with form “name_number”, where name is the name of the user and the number is some random number provided to generate labels used by OpenCV face recognizer algorithm. 
5)	Flow of data in the code is:
a.	Click a picture, store it at pre-defined location.
b.	Run a training dataset, generate labels for each image.
c.	Run a function which will try to compare images in training dataset and clicked image and based on this comparison will give a verdict if the image is recognized or not, if recognized, what is the confidence and what is the user name that had been identified.
d.	If user name matches, the program returns 1
6)	Then this return value is parsed to the folder launcher and folder is opened, if return value is not 1 in that case the folder is not opened.
7)	Algorithm inside OpenCV codes: Three algorithms are used by OpenCV for face recognition.
a.	EigenFaces
b.	FisherFaces
c.	Local Binary Pattern Histogram
8)	We are using LBPH in our code. The detailed working of all of these algorithms with their codes can be found on the link http://docs.opencv.org/2.4/modules/contrib/doc/facerec/facerec_tutorial.html (OpenCV FaceRec Documentation)

