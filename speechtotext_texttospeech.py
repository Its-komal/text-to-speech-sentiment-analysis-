import speech_recognition as sr 
import pyttsx3
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from langdetect import detect

engine=pyttsx3.init()
r=sr.Recognizer()
def detect_intent_texts(project_id, session_id, texts, language_code="en-US"):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    from google.cloud import dialogflow

    session_client = dialogflow.SessionsClient()

    session = session_client.session_path(project_id, session_id)
    # print("Session path: {}\n".format(session))

    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)

        query_input = dialogflow.QueryInput(text=text_input)

        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )

        # print("=" * 20)
        # print(response.query_result.query_text)
        # print(response.query_result.intent.display_name)
        return(response.query_result.fulfillment_text)


with sr.Microphone() as source:
    # read the audio data from the default microphone
    print("Listening")
    audio_data = r.record(source, duration=5)
    print("Recognizing...")
    try:
        language= detect( r.recognize_google(audio_data))

        # if detect(r.recognize_google(audio_data))== "en":
            
        text = r.recognize_google(audio_data, show_all = True, language='en-In' )
        print("I thinks you said: '" + r.recognize_google(audio_data) + "'")
        text_output=detect_intent_texts("neural-proton-321810","123456789",[text],)
        # elif detect(r.recognize_google(audio_data))== "hi":
        #     text = r.recognize_google(audio_data, show_all = True, language='hi-In' )
        #     text_output=detect_intent_texts("neural-proton-321810","123456789",[text],)
        #     print("I thinks you said: '" + r.recognize_google(audio_data) + "'")

        # else:
        #     print(r.recognize_google(audio_data ,language='hi-In'))

    except:
        pass

# def takeCommandHindi():
         
#     r = sr.Recognizer()
#     with sr.Microphone() as source:
          
#         seconds of non-speaking audio before 
#         a phrase is considered complete
#         print('Listening')
#         r.pause_threshold = 0.7  
#         audio_data = r.record(source, duration=5) 
#         try:
#             print("Recognizing")
#             Query = r.recognize_google(audio_data, language='hi-In')
              
#             for listening the command in indian english
#             print("the query is printed='", Query, "'")
          
#         handling the exception, so that assistant can 
#         ask for telling again the command
#         except Exception as e:
#             print(e)  
#             print("Say that again sir")
#             return "None"
#         return Query
  
  
  
# Driver Code
           
# call the function
# takeCommandHindi()


# Sentence=[str(text)]
# analyser=SentimentIntensityAnalyzer()

# for i in Sentence:
#     v=analyser.polarity_scores(i)
#     print(v)

# Import the required module for text 
# to speech conversion
import gtts  
from playsound import playsound  
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio

# Language in which you want to convert

  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
# print(r.recognize_google(audio_data))
t1 = gtts.gTTS(detect_intent_texts("neural-proton-321810","123456789",[r.recognize_google(audio_data)]))  

  
# Saving the converted audio in a mp3 file named
# welcome 
t1.save("welcome.mp3")
  
# Playing the converted file
os.system("welcome.mp3")