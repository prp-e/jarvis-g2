import brain 
import pyttsx3 
import speech_recognition as sr 

class Jarvis:

    def __init__(self, voice_recognizer, voice_engine):
        self.voice_recognizer = voice_recognizer
        self.voice_engine = voice_engine
    
    def get_command(self):
        with sr.Microphone() as source:
            print("Listening...")
            self.voice_recognizer.pause_threshold = 1
            audio = self.voice_recognizer.listen(source)

            try:
                print("Recognizing...")
                query = self.voice_recognizer.recognize_google(audio)
            except Exception as e:
                print(e)

            return query


if __name__ == "__main__":
    jarvis_init = Jarvis(sr.Recognizer(), pyttsx3.init())
    while True:
        query = jarvis_init.get_command()
        print(query)
        jarvis_init.voice_engine.say(brain.chat(query))
        jarvis_init.voice_engine.runAndWait()