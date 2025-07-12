# 🎙️ Voice Emotion Detector using Machine Learning

A full-stack web application that predicts the emotional tone of a person based on their voice input using a machine learning model trained on the RAVDESS dataset.

Built with **React.js**, **Flask**, and **XGBoost**, the app lets users **upload `.wav`, `.mp3`, or `.webm` files** or **record their voice live** and returns both the **predicted emotion** and the **confidence score**. 🎧🧠

---

## 🌐 Live Demo

> Coming soon... (e.g., [https://emotion-detector.vercel.app](https://emotion-detector.vercel.app))

---

## 🧠 Trained on RAVDESS Dataset

This project uses the **Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS)** to train the emotion classification model.

* 🎤 Audio-only subset of RAVDESS
* 7 emotions: `Happy`, `Sad`, `Angry`, `Neutral`, `Disgust`, `Fear`, `Calm`
* Audio features extracted using **Librosa**
* Model trained using **XGBoost**
* Serialized with **joblib**

---

## 🖼️ Features

* 📁 Upload `.wav`, `.mp3`, or `.webm` audio
* 🎤 Record live audio using microphone
* 🔀 Audio format conversion handled via `ffmpeg`
* 🧠 Predict emotion + show confidence %
* ▶️ Preview audio before submission
* ⚙️ Error/debug handling in frontend & backend
* 🔐 Secure CORS-enabled API
* 🌈 Responsive and minimal UI

---

## 📦 Tech Stack

| Layer      | Tech Used                               |
| ---------- | --------------------------------------- |
| Frontend   | React.js, HTML5 Audio API, Tailwind CSS |
| Backend    | Flask, Flask-CORS, Librosa, Pydub       |
| ML Model   | XGBoost, NumPy, Scikit-learn            |
| Deployment | Vercel (Frontend), Render (Backend)     |

---

## 📂 Folder Structure

```
emotion-detector-app/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── model/
│       ├── xgb_ravdess_emotion_model.pkl
│       └── label_encoder.pkl
│
├── frontend/
│   ├── public/
│   ├── package.json
│   └── src/
│       ├── api/
│       │   └── emotionAPI.js
│       ├── components/
│       │   └── EmotionForm.jsx
│       └── App.js
│
├── .gitignore
└── README.md
```

---

## 💻 Local Setup

### 📦 Backend (Flask + ML)

1. Navigate to backend folder:

   ```bash
   cd backend
   python -m venv venv
   venv\Scripts\activate  # For Windows
   pip install -r requirements.txt
   ```

2. ✅ Install FFmpeg:

   * Download from: [https://www.gyan.dev/ffmpeg/builds](https://www.gyan.dev/ffmpeg/builds)
   * Extract to: `C:\ffmpeg`
   * Add `C:\ffmpeg\bin` to your **System Environment PATH**
   * Or set manually in `app.py`:

     ```python
     from pydub import AudioSegment
     AudioSegment.converter = r"C:\\ffmpeg\\bin\\ffmpeg.exe"
     ```

3. Start backend server:

   ```bash
   python app.py
   ```

   Server runs at: `http://127.0.0.1:5000`

---

### 📦 Frontend (React)

1. Navigate to frontend folder:

   ```bash
   cd frontend
   npm install
   ```

2. Start React app:

   ```bash
   npm start
   ```

   Runs at: `http://localhost:3000`

---

## 📡️ API Endpoint

### `POST /predict`

**Request**: `multipart/form-data`

```json
{
  "file": audio_file (.wav / .mp3 / .webm)
}
```

**Response**:

```json
{
  "emotion": "happy",
  "confidence": 94.23
}
```

---

## 🧠 Model Info

* Dataset: RAVDESS Emotional Speech
* Algorithm: XGBoost
* Extracted Features:

  * MFCCs
  * Chroma STFT
  * Mel Spectrogram
  * Spectral Contrast
  * Zero Crossing Rate

---

## 🔧 Troubleshooting

* 🔴 `Internal Server Error`:

  * Check if the model files exist in `/model`
  * Confirm `ffmpeg` is installed and accessible

* 🎤 `Microphone permission denied`:

  * Ensure browser has access to mic
  * Not supported in all browsers (Safari issues with `.webm`)

* 🟨 `Failed to convert audio to WAV`:

  * Double check that FFmpeg is installed and accessible by `pydub`

---

## ✨ Future Improvements

* 🎯 Multilingual audio input
* 📈 Emotion trend visualization
* 🤮 More diverse training dataset
* 🌐 Deploy with HTTPS and production build
