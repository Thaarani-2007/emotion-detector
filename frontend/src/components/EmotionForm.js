import React, { useState, useRef } from 'react';
import { predictEmotion } from '../api/emotionAPI';
import './EmotionForm.css';

export default function EmotionForm() {
  const [file, setFile] = useState(null);
  const [audioURL, setAudioURL] = useState(null);
  const [result, setResult] = useState('');
  const [confidence, setConfidence] = useState(null);
  const [error, setError] = useState('');
  const fileInputRef = useRef(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setResult('');
    setConfidence(null);
    setError('');

    if (!file) {
      setError("Please upload a WAV file");
      return;
    }

    try {
      const res = await predictEmotion(file);
      if (res.error) {
        setError(res.error);
      } else {
        setResult(res.emotion);
        setConfidence(res.confidence);
      }
    } catch (err) {
      setError("Failed to connect to backend: " + err.message);
    }
  };

  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    setFile(selectedFile);
    if (selectedFile) {
      setAudioURL(URL.createObjectURL(selectedFile));
    }
  };

  return (
    <div className="emotion-container">
      <div className="form-card">
        <h1 className="title">🎙️ Emotion Detector</h1>

        <form onSubmit={handleSubmit} className="form-area">
          <label className="upload-label">Upload a WAV file</label>
          <input
            type="file"
            accept="audio/wav"
            onChange={handleFileChange}
            ref={fileInputRef}
          />

          {audioURL && (
            <div className="audio-section">
              <label>Preview:</label>
              <audio controls src={audioURL} className="audio-preview" />
            </div>
          )}

          <button type="submit" className="submit-button">
            🚀 Predict Emotion
          </button>
        </form>

        {result && (
          <div className="result success">
            <p><strong>Predicted Emotion:</strong> {result}</p>
            <p><strong>Confidence:</strong> {confidence}%</p>
          </div>
        )}
        {error && (
          <div className="result error">
            ⚠️ {error}
          </div>
        )}
      </div>
    </div>
  );
}
