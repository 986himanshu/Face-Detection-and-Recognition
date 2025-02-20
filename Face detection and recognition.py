
import cv2,os
import numpy as np
from PIL import Image
import pickle
import sqlite3
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);
recognizer=cv2.createLBPHFaceRecognizer();                                                                                                              
recognizer.load('trainner.yml')
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX,0.4,1,0,1)
def getProfile(id):									               
    conn=sqlite3.connect("FaceBase.db")
    cmd="SELECT * FROM People WHERE ID="+str(id)
    cursor=conn.execute(cmd)								          
    profile=None
    for row in cursor:										
        profile=row									         
    conn.close()      
    return profile										
while(True): 
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)          					                                  
    faces=faceDetect.detectMultiScale(gray,1.3,5);					
    for(x,y,w,h) in faces:									
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) 
        id,conf=recognizer.predict(gray[y:y+h,x:x+w])					
        profile=getProfile(id)
        if(profile!=None):	
            cv2.cv.PutText(cv2.cv.fromarray(img),"ID : "+str(profile[0]),(x,y+h+20),font,(0,255,0)); 
            cv2.cv.PutText(cv2.cv.fromarray(img),"Name : "+str(profile[1]),(x,y+h+45),font,(0,255,0));	
    cv2.imshow("Face detection and recognize",img);		
    if(cv2.waitKey(1)==ord('q')):											break;                                                                                                    	                  10
cam.release()
cv2.destroyAllWindows()
