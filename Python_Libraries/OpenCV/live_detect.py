import cv2

model1=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
model2=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_profileface.xml")
video_capture=cv2.VideoCapture(0)
while True:
    ret,face_frame=video_capture.read()
    if not ret:
        break
    gray_frame=cv2.cvtColor(face_frame,cv2.COLOR_RGB2GRAY)
    face=model1.detectMultiScale(gray_frame,scaleFactor=1.3,minNeighbors=3)
    face2=model2.detectMultiScale(gray_frame,scaleFactor=1.3,minNeighbors=4)
    for (x,y,w,h) in face:
        cv2.rectangle(face_frame,(x,y),(x+w,y+h),(0,255,0),3)
    for (x,y,w,h)in face2:
        cv2.rectangle(face_frame,(x,y),(x+w,y+h),(255,0,0),3)
    cv2.imshow("Detection",face_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()
