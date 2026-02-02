import cv2
import os
import time
import numpy as np
from PIL import Image
recognizer=cv2.face.LBPHFaceRecognizer_create()
detector=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

def get_image_and_lebals(path):
    images_paths=[os.path.join(path,f) for f in os.listdir(path)]
    face_samples=[]
    ids=[]
    for image_path in images_paths:
        img_PIL=Image.open(image_path).convert('L')
        img_numpy=np.array(img_PIL,'unit8')
        id=int(os.path.split(images_path)[-1].split('.')[1])
        faces=detector.detectMultiScale(img_numpy)
        for (x,y,w,h) in faces:
            face_samples.append(img_numpy[y:y+h, x:x+w]) 
            ids.append(id)
    return face_samples,ids
print("Info: Traning is starting...")
faces,ids=get_image_and_lebals('samples')
recognizer.train(faces,np.array(ids))
recognizer.write("OpenCV/trainer.yml")
print(f"\n info {len(np.unique(ids))} faces trained")
