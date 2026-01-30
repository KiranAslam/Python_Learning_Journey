import cv2
face_cascade1=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
img=cv2.imread("Python_Libraries/OpenCV/test.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
face=face_cascade1.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=4)
for (x,y,w,h) in face:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow("Face Detection",img)
cv2.waitKey(0)
cv2.destroyAllWindows()