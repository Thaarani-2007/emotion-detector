# 🎙️ Voice Emotion Detection Web App

A simple and intuitive web app that detects emotions from voice recordings using a custom-trained machine learning model.

---

## 🌟 Overview

This project is part of my ongoing journey to bridge the gap between machine learning theory and real-world applications.  
It allows users to either **record their voice live** or **upload audio files (WAV/MP3)** and returns the predicted **emotion with a confidence score**.

---

## 🧠 What It Does

- Accepts audio input (recorded or uploaded).
- Extracts acoustic features from the audio.
- Predicts the emotion using a trained ML model.
- Returns both the **emotion label** and **confidence score**.

---

## 📂 Dataset Used

- **RAVDESS** (Ryerson Audio-Visual Database of Emotional Speech and Song)
- Contains professionally recorded voice clips labeled with 8 emotional states.
- In this project, 5 core emotions are used:
  - 😊 Happy
  - 😢 Sad
  - 😡 Angry
  - 😌 Calm
  - 😐 Neutral

---

## 📊 Model & Accuracy

- Feature Extraction:
  - MFCCs (60)
  - Chroma
  - Mel Spectrogram
  - Spectral Contrast
  - Zero-Crossing Rate

- ML Model:
  - **XGBoost Classifier**
  - Trained with:
    - 🎛️ Data Augmentation
    - 🧪 Hyperparameter Tuning via GridSearchCV

- **Test Accuracy**: ~85%

---

## 🛠️ Tech Stack

| Layer     | Technologies |
|-----------|--------------|
| Frontend  | React (with file upload & audio recording) |
| Backend   | Flask (REST API), Librosa (audio processing) |
| ML Model  | Python, Scikit-learn, XGBoost |

---

## 🚀 Getting Started (Run Locally)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Thaarani-2007/ser-model.git
cd ser-model
