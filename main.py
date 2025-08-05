import speech_recognition as sr
import pyttsx3
import webbrowser

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    if "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    if "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening for wake word...")
            try:
                audio = r.listen(source, timeout=5, phrase_time_limit=3)
                word = r.recognize_google(audio)
                print(f"Heard: {word}")
                if word.lower() == "jarvis":
                    print("Wake word detected. Responding...")
                    speak("Ya")
                    print("Jarvis Activated..")
                    with sr.Microphone() as source:
                        audio = r.listen(source, timeout=5)
                        command = r.recognize_google(audio)
                        processCommand(command)
            except Exception as e:
                print(f"Error: {e}")
