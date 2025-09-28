from flask import Flask, render_template, request, jsonify
from googletrans import Translator
from gtts import gTTS
from io import BytesIO
import base64

app = Flask(__name__)
translator = Translator()

# Section 1: Telugu → English
@app.route("/telugu_to_english", methods=["POST"])
def telugu_to_english():
    telugu_text = request.json.get("text", "")
    if not telugu_text:
        return jsonify({"error": "No text received"})
    try:
        english_text = translator.translate(telugu_text, src="te", dest="en").text
        # Generate audio in-memory
        mp3_fp = BytesIO()
        tts = gTTS(english_text, lang="en")
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        audio_base64 = base64.b64encode(mp3_fp.read()).decode('utf-8')
        return jsonify({"text": english_text, "audio": audio_base64})
    except Exception as e:
        return jsonify({"error": str(e)})

# Section 2: English → Telugu
@app.route("/english_to_telugu", methods=["POST"])
def english_to_telugu():
    english_text = request.json.get("text", "")
    if not english_text:
        return jsonify({"error": "No text received"})
    try:
        telugu_text = translator.translate(english_text, src="en", dest="te").text
        # Generate audio in-memory
        mp3_fp = BytesIO()
        tts = gTTS(telugu_text, lang="te")
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        audio_base64 = base64.b64encode(mp3_fp.read()).decode('utf-8')
        return jsonify({"text": telugu_text, "audio": audio_base64})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
