# VocaLink
VocaLink is a real-time bilingual voice translator that converts Telugu speech to English and English speech to Telugu instantly. Speak naturally, see live text transcription, and listen to translated audio — all in a clean, user-friendly interface.

# **VocaLink: Telugu ↔ English Speech Translator**

**Tagline:** *Speak. Translate. Listen. Effortless Telugu & English Voice Translation.*

---

## **1. Concept / Idea**

VocaLink is designed to **bridge language gaps** for Telugu and English speakers by providing **real-time speech translation**. It allows users to:

* Speak in **Telugu** and get **English text and audio** instantly.
* Speak in **English** and get **Telugu text and audio** instantly.
* Provide **interactive, responsive voice-to-voice translation** for users of all ages.

**Use Cases:**

* Students and professionals needing bilingual communication.
* Travelers or people interacting with Telugu/English speakers.
* Language learning and accessibility applications.

---

## **2. Features**

1. **Real-Time Speech Recognition**

   * Recognizes speech from the microphone and converts it to text live.

2. **Bilingual Translation**

   * Supports Telugu → English and English → Telugu translations seamlessly.

3. **Audio Playback**

   * Translated text can be played back as audio using gTTS (Google Text-to-Speech).

4. **Auto-Stop Listening**

   * Stops automatically when the user pauses speaking.

5. **Professional & User-Friendly UI**

   * Modern, card-based design with live status updates and loader animations.

6. **Multi-Sentence Input Support**

   * Can handle multiple sentences in sequence without breaking.

7. **Responsive & Interactive**

   * Works on desktop and mobile with real-time feedback.

---

## **3. Technology Stack**

| Component          | Technology                             |
| ------------------ | -------------------------------------- |
| Backend            | Python, Flask                          |
| Frontend           | HTML, CSS, JavaScript                  |
| Speech Recognition | Web Speech API (Browser)               |
| Translation        | Google Translate API via `googletrans` |
| Text-to-Speech     | gTTS (Google Text-to-Speech)           |
| Audio Hosting      | Flask static folder                    |
| Deployment         | Local/Heroku/GCP/AWS                   |

---

## **4. Workflow**

**Section 1: Telugu → English**

1. User clicks **Start** button and speaks in Telugu.
2. Web Speech API recognizes the speech and displays live Telugu text.
3. When the user stops speaking, Flask backend translates text to English using Google Translate API.
4. gTTS converts English text to speech and returns an audio file.
5. Audio is played automatically, and English text is displayed.

**Section 2: English → Telugu**

1. User clicks **Start** button and speaks in English.
2. Web Speech API recognizes the speech and displays live English text.
3. When the user stops speaking, Flask backend translates text to Telugu.
4. gTTS converts Telugu text to speech and returns an audio file.
5. Audio is played automatically, and Telugu text is displayed.

**Both sections** feature:

* **Auto-stop listening on silence**
* **Live transcription**
* **Loader animation during processing**
* **Dynamic audio generation for multiple inputs**


Do you want me to do that next?

