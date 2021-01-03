import brain 
import pyttsx3 
import speech_recognition as sr 
import webbrowser

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
    jarvis_init.voice_engine.setProperty('voice', 'com.apple.speech.synthesis.voice.samantha')

    goodbye_query = ["Bye", "Goodbye", "Farewell", "See you later", "Until the next time"] 
    goodbye_query = [q.lower() for q in goodbye_query]
    while True:
        query = jarvis_init.get_command()
        query = query.lower()
        print("You said: ", query)
        if query in goodbye_query:
            jarvis_init.voice_engine.say(brain.chat(query))
            jarvis_init.voice_engine.runAndWait()
            break
        elif "search for" in query:
            jarvis_init.voice_engine.say(brain.chat("search for"))
            jarvis_init.voice_engine.runAndWait() 
            query = query.replace("search for", "")
            jarvis_init.voice_engine.say(f"Here is some information about {query}")
            jarvis_init.voice_engine.runAndWait()
            webbrowser.open_new(f"https://google.com/search?q={query}")
        else:
            jarvis_init.voice_engine.say(brain.chat(query))
            jarvis_init.voice_engine.runAndWait()