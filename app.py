from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import speech_recognition as sr
from pydub import AudioSegment
from reportlab.pdfgen import canvas
import io

app = Flask(__name__)
api = Api(app)

tasks = []

class Task(Resource):
    def get(self):
        """Return all tasks"""
        return jsonify(tasks)

    def post(self):
        """Create a new task"""
        data = request.get_json()
        tasks.append(data)
        return jsonify(data), 201

class AudioToText(Resource):
    def post(self):
        """Convert audio to text"""
        if 'audio' not in request.files:
            return {"error": "No audio file provided"}, 400

        audio_file = request.files['audio']
        sound = AudioSegment.from_file(audio_file)
        sound.export("temp.wav", format="wav")

        recognizer = sr.Recognizer()
        with sr.AudioFile("temp.wav") as source:
            audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio)
            return jsonify({"text": text}), 200
        except sr.UnknownValueError:
            return {"error": "Unable to recognize speech"}, 400
        except sr.RequestError as e:
            return {"error": "Error with speech recognition service"}, 400

if __name__ == '__main__':
    app.run(debug=True)
