import React, { useRef, useState, useEffect } from 'react';
import Webcam from 'react-webcam';
import axios from 'axios';
import './App.css';

function App() {
  const webcamRef = useRef(null);
  const [user, setUser] = useState({ name: "Scanning...", confidence: 0 });

  const capture = async () => {
    if (webcamRef.current) {
      const imageSrc = webcamRef.current.getScreenshot();
      if (imageSrc) {
        try {
          const response = await axios.post('http://127.0.0.1:5000/recognize', {
            image: imageSrc
          });
          setUser({ name: response.data.name, confidence: response.data.confidence });
        } catch (error) {
          console.error("Backend Error:", error);
        }
      }
    }
  };

  useEffect(() => {
    const interval = setInterval(capture, 1000); 
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="container">
      <h1>Live Face Recognition</h1>
      <div className="camera-box">
        <Webcam
          audio={false}
          ref={webcamRef}
          screenshotFormat="image/jpeg"
          width={480}
        />
      </div>
      <div className="result-card">
        <h2>Identify: <span className="highlight">{user.name}</span></h2>
        <p>Match Score: {user.confidence}%</p>
      </div>
    </div>
  );
}

export default App;