import cv2
profile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_profileface.xml")
vid_cap=cv2.VideoCapture(0)
while True:
    ret,frame=vid_cap.read()
    if not ret:
        break
    gray_frame=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    profiles=profile_cascade.detectMultiScale(gray_frame,scaleFactor=1.3,minNeighbors=5)
    for (x, y, w, h) in profiles:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    cv2.imshow("Face Detection" , frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid_cap.release()
cv2.destroyAllWindows()

