from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
import librosa
import os
import tempfile
import traceback

app = Flask(__name__)
CORS(app)

# Load model and label encoder
try:
    model = joblib.load("model/xgb_ravdess_emotion_model.pkl")
    label_encoder = joblib.load("model/label_encoder.pkl")
    print("✅ Model and label encoder loaded successfully")
except Exception as e:
    print("❌ Failed to load model or encoder:", str(e))
    traceback.print_exc()
    model = None
    label_encoder = None

# Feature extraction from WAV files
def extract_features(file_path):
    audio, sample_rate = librosa.load(file_path, res_type='kaiser_fast')  # WAV-only
    mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=60)
    chroma = librosa.feature.chroma_stft(y=audio, sr=sample_rate)
    mel = librosa.feature.melspectrogram(y=audio, sr=sample_rate)
    log_mel = librosa.power_to_db(mel)
    contrast = librosa.feature.spectral_contrast(y=audio, sr=sample_rate)
    zcr = librosa.feature.zero_crossing_rate(y=audio)

    features = np.hstack([
        np.mean(mfccs.T, axis=0),
        np.mean(chroma.T, axis=0),
        np.mean(log_mel.T, axis=0),
        np.mean(contrast.T, axis=0),
        np.mean(zcr.T, axis=0)
    ])

    return features.reshape(1, -1)

@app.route("/predict", methods=["POST"])
def predict():
    try:
        if model is None or label_encoder is None:
            raise ValueError("Model or encoder not loaded.")

        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]
        if file.filename == "":
            return jsonify({"error": "File name is empty"}), 400

        # Save temp file
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp:
            file.save(temp.name)
            temp_path = temp.name

        # Extract features
        features = extract_features(temp_path)

        # Predict emotion and confidence
        proba = model.predict_proba(features)[0]
        predicted_class_index = np.argmax(proba)
        predicted_emotion = label_encoder.inverse_transform([predicted_class_index])[0]
        confidence = float(round(proba[predicted_class_index] * 100, 2))  # ✅ Fixed

        os.remove(temp_path)

        return jsonify({
            "emotion": predicted_emotion,
            "confidence": confidence
        })

    except Exception as e:
        print("❌ Prediction error:", str(e))
        traceback.print_exc()
        return jsonify({
            "error": "Internal server error",
            "details": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
