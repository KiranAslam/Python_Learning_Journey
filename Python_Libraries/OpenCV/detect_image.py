import cv2
face_cascade1=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
img=cv2.imread("test.jpg")