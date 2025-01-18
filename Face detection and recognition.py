
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
