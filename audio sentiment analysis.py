import speech_recognition as sr 
import pyttsx3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

engine=pyttsx3.init()
r=sr.Recognizer()
with sr.Microphone() as source:
    # read the audio data from the default microphone
    print("Listening")
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    try:
        text = r.recognize_google(audio_data, language = 'en-IN', show_all = True )
        print("I thinks you said: '" + r.recognize_google(audio_data) + "'")
    except:
        print("Except")


Sentence=[str(text)]
analyser=SentimentIntensityAnalyzer()

for i in Sentence:
    v=analyser.polarity_scores(i)
    print(v)