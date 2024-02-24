Notepad++ v8.5.4 bug-fixes and new features:

 1. Fix macro recording regression on Unicode character.
 2. Fix regression of defective detection for file read-only attribute removal via Explorer.
 3. Fix opening multi-files on multi-instance mode regression.
 4. Update: Scintilla 5.3.5 Lexilla 5.2.5
 5. Fix Notepad++ hanging issue running macro to EOF.
 6. Fix EOL symbol color/appearence being reset issue while changing encoding.
 7. Enable code folding in Assembly source files.
 8. Fix document language not remembered through sessions issue.
 9. Add SHA-1 hash features.
10. Add "open new blank document in addition on startup" ability.
11. Fix lexer plugin is sorted unconventionally in language menu issue.
12. Add message NPPM_DARKMODESUBCLASSANDTHEME to allow plugin to use generic dark mode.
13. Add the ability to close multiple files without saving in Document list.
14. Several GUI Enhancements.
15. Fix tabContextMenu_example.xml not being deleted while uninstallation.
16. Fix error message on uninstallation.


Get more info on
https://notepad-plus-plus.org/downloads/v8.5.4/


Included plugins:

1.  NppExport v0.4
2.  Converter v4.5
3.  Mime Tool v2.9


Updater (Installer only):

* WinGup (for Notepad++) v5.2.5
import cv2,os
import numpy as np
from PIL import Image
import pickle
import sqlite3
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);
recognizer=cv2.createLBPHFaceRecognizer();                                                                                                              1
recognizer.load('trainner.yml')
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX,0.4,1,0,1)
def getProfile(id):									               12
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(id)
    cursor=conn.execute(cmd)								          13
    profile=None
    for row in cursor:										14
        profile=row									         15
    conn.close()      
    return profile										16
while(True): 
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)          					                2                  
    faces=faceDetect.detectMultiScale(gray,1.3,5);					
    for(x,y,w,h) in faces:									3
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) 
        id,conf=recognizer.predict(gray[y:y+h,x:x+w])					4
        profile=getProfile(id)                                                                                                		                   5
        if(profile!=None):							            		6
            cv2.cv.PutText(cv2.cv.fromarray(img),"ID : "+str(profile[0]),(x,y+h+20),font,(0,255,0)); 
            cv2.cv.PutText(cv2.cv.fromarray(img),"Name : "+str(profile[1]),(x,y+h+45),font,(0,255,0));	
    cv2.imshow("Face detection and recognize",img);				                   8
    if(cv2.waitKey(1)==ord('q')):							9				break;                                                                                                    	                  10
cam.release()
cv2.destroyAllWindows()
