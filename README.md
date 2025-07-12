# 🎙️ Voice Emotion Detector using Machine Learning

A full-stack web application that predicts the emotional tone of a person based on their voice input using a machine learning model trained on the RAVDESS dataset.

Built with **React.js**, **Flask**, and **XGBoost**, the app lets users upload `.wav` files and returns both the **predicted emotion** and the **confidence score**. 🎧🧠

---

## 🌐 Live Demo

> Coming soon... (e.g., https://emotion-detector.vercel.app)

---

## 🧠 Trained on RAVDESS Dataset

This project uses the **Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS)** to train the emotion classification model.

- 🎤 Audio-only subset of RAVDESS
- 7 emotions: `Happy`, `Sad`, `Angry`, `Neutral`, `Disgust`, `Fear`, `Surprise`
- Audio processing using **Librosa**
- Model trained using **XGBoost**
- Serialized using **joblib**

---

## 📦 Tech Stack

| Layer      | Tech Used                        |
|------------|----------------------------------|
| Frontend   | React.js, HTML5 Audio API, CSS   |
| Backend    | Flask, Flask-CORS, Librosa       |
| Model      | XGBoost, NumPy, Scikit-learn     |
| Deployment | Vercel (Frontend), Render (Backend) |

---

## 🖼️ Features

- 🎧 Upload `.wav` audio files
- 🧠 Predicts emotions based on voice
- 📊 Shows model confidence (probability)
- ▶️ Audio playback for preview
- 🖼️ Beautiful & responsive UI
- 🔐 CORS-secure API requests
- 🌍 Easy deployment-ready setup

---

## 🗂️ Folder Structure

emotion-detector-app/
├── backend/
│ ├── app.py
│ ├── requirements.txt
│ └── model/
│ ├── xgb_ravdess_emotion_model.pkl
│ └── label_encoder.pkl
├── frontend/
│ ├── src/
│ │ ├── api/
│ │ │ └── emotionAPI.js
│ │ └── components/
│ │ └── EmotionForm.jsx
│ ├── public/
│ └── package.json
├── .gitignore
└── README.md

## 💻 Local Setup

### 📦 Backend (Flask + ML)

1. Navigate to the `backend` folder:
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py

### 📦 frontend (React)
```bash
   cd frontend
   npm install
   npm start


