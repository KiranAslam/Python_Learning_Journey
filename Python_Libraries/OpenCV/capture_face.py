import cv2
import os
import time

model=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
vid_capture=cv2.VideoCapture(0)
face_id=input("Enter user ID: ")
count=0
while True:
    ret,frame=vid_capture.read()
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    face=model.detectMultiScale(gray_frame,scaleFactor=1.3,minNeighbors=3)
    for (x,y,w,h) in face:
        count+=1
        file_name=f"Python_libraries/OpenCV/samples/user.{face_id}.{count}.jpg"
        cv2.imwrite(file_name, gray_frame[y:y+h, x:x+w])
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        cv2.putText(frame,f"captured:{count}/30",(50,50), cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        time.sleep(0.3)
    cv2.imshow("Capturing....",frame)
    
    if cv2.waitKey(1) & 0xFF==ord('q') or count>=30:
        break
print("photo saved!")
vid_capture.release()
cv2.destroyAllWindows()