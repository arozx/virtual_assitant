# voice_recognition.py
import json
import os
import queue
import sys

import sounddevice as sd
import vosk

q = queue.Queue()


def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


class VoiceRecognition:
    def __init__(self, wake_word, model_path="vosk-model-en-us-0.42-gigaspeech"):
        self.wake_word = wake_word
        self.model_path = model_path
        self.load_model()

    def load_model(self):
        if not os.path.exists(self.model_path):
            print(
                "Please download the model from https://alphacephei.com/vosk/models and unpack as 'model' in the current folder."
            )
            sys.exit(1)
        self.model = vosk.Model(self.model_path)
        self.recognizer = vosk.KaldiRecognizer(self.model, 16000)
        self.samplerate = 16000
        self.device = 1  # Adjust as needed

    def listen(self):
        with sd.RawInputStream(
            samplerate=self.samplerate,
            blocksize=8000,
            device=self.device,
            dtype="int16",
            channels=1,
            callback=callback,
        ):
            print("Listening...")
            while True:
                data = q.get()
                if self.recognizer.AcceptWaveform(data):
                    result = self.recognizer.Result()
                    text = json.loads(result).get("text", "")
                    if text:
                        print(f"Recognized: {text}")
                        return text
                else:
                    print(self.recognizer.PartialResult())

    def detect_wake_word(self, text):
        return self.wake_word.lower() in text.lower()
