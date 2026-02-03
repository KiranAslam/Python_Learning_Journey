import cv2

recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read('OpenCV/trainer.yml')
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

names=['None','Kiran','User2']
video=cv2.VideoCapture(0)
while True:
    ret,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=3)
    for (x,y,w,h) in faces:
        id,confidence=recognizer.predict(gray[y:y+h,x:x+w])
        if confidence<100:
            name=names[id]
            confidence_text=f"{round(100-confidence)}%"
        else:
            name="unknown"
            confidence_text = f"  {round(100 - confidence)}%"
        cv2.putText(frame,str(name),(x+5,y-5),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,255,0),2)
        cv2.putText(frame,str(confidence_text),(x+5,y+h-5),cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,1,(0,225,0),2)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,225,0),2)
    cv2.imshow("Face Recognization",frame)
    if cv2.waitKey(1) & 0XFF==ord('q'):
        break
video.release()
cv2.destroyAllWindows()