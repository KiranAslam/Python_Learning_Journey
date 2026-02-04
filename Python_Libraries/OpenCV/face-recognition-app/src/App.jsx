import React, { useRef, useState, useCallback } from 'react';
import Webcam from 'react-webcam';
import axios from 'axios';

function App() {
  const webcamRef = useRef(null);
  const [result, setResult] = useState("Face Not Detected");
  const [confidence, setConfidence] = useState(0);

  const capture = useCallback(async () => {
    const imageSrc = webcamRef.current.getScreenshot();
    
    if (imageSrc) {
      try {
        const response = await axios.post('http://127.0.0.1:5000/recognize', {
          image: imageSrc
        });
        setResult(response.data.name);
        setConfidence(response.data.confidence);
      } catch (error) {
        console.error("Backend se connect nahi ho raha!", error);
      }
    }
  }, [webcamRef]);
  React.useEffect(() => {
    const interval = setInterval(() => {
      capture();
    }, 1000);
    return () => clearInterval(interval);
  }, [capture]);

  return (
    <div style={{ textAlign: 'center', padding: '20px' }}>
      <h1>Face Recognition System</h1>
      <Webcam
        audio={false}
        ref={webcamRef}
        screenshotFormat="image/jpeg"
        width={400}
        style={{ borderRadius: '10px' }}
      />
      <div style={{ marginTop: '20px' }}>
        <h3>User: <span style={{ color: 'green' }}>{result}</span></h3>
        <p>Confidence: {confidence}%</p>
      </div>
    </div>
  );
}

export default App;