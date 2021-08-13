import speech_recognition as sr

r = sr.Recognizer()


with sr.Microphone() as source:
    # read the audio data from the default microphone
    print("Listening")
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    try:
        text = r.recognize_google(audio_data, language = 'en-IN', show_all = True )
        print("I thinks you said '" + r.recognize_google(audio_data) + "'")
    except:
        print("Except")
    # wb.get(chrome_path).open(f_text)
    # convert speech to text
# text = r.recognize_google(audio_data,language="es-ES")
# print(text)
# text = r.recognize_google(audio_data, language="es-ES")
