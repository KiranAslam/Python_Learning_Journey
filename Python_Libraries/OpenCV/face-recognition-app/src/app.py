from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
import base64
import os

app = Flask(__name__)
CORS(app) 
MODEL_PATH = '../../trainer.yml' 
CASCADE_PATH = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
recognizer = cv2.face.LBPHFaceRecognizer_create()
if os.path.exists(MODEL_PATH):
    recognizer.read(MODEL_PATH)
    print("Model Loaded Successfully!")
else:
    print("Error: trainer.yml not found!")
face_cascade = cv2.CascadeClassifier(CASCADE_PATH)
names = ['None', 'Kiran', 'User2']
@app.route('/recognize', methods=['POST'])
def recognize():
    data = request.json['image']
    img_data = base64.b64decode(data.split(',')[1])
    nparr = np.frombuffer(img_data, np.uint8)
    frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    response = {"name": "No Face Detected", "confidence": 0}
    for (x, y, w, h) in faces:
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])
        if confidence < 100:
            response = {
                "name": names[id] if id < len(names) else "Unknown",
                "confidence": round(100 - confidence)
            }
        else:
            response = {"name": "Unknown", "confidence": round(100 - confidence)}
            
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5000, debug=True)