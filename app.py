from flask import Flask, render_template, request, jsonify
from googletrans import Translator
from gtts import gTTS
import os, time

app = Flask(__name__)
translator = Translator()

if not os.path.exists("static"):
    os.makedirs("static")

# Section 1: Telugu → English
@app.route("/telugu_to_english", methods=["POST"])
def telugu_to_english():
    telugu_text = request.json.get("text", "")
    if not telugu_text:
        return jsonify({"error": "No text received"})
    try:
        english_text = translator.translate(telugu_text, src="te", dest="en").text
        filename = f"static/english_{int(time.time()*1000)}.mp3"
        tts = gTTS(english_text, lang="en")
        tts.save(filename)
        return jsonify({"text": english_text, "audio": filename})
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
        filename = f"static/telugu_{int(time.time()*1000)}.mp3"
        tts = gTTS(telugu_text, lang="te")
        tts.save(filename)
        return jsonify({"text": telugu_text, "audio": filename})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
