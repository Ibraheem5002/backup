import pyttsx3 as pyt

def speak(text):
    print(f"Assistant Say: {text}")

    engine = pyt.init()
    engine.setProperty('rate',210)
    engine.setProperty('volume',1)

    engine.say(text)
    engine.runAndWait()

# speak("Hey there, I am David, your personal assistant. How can I help you?")
# speak("This is speak number 2. Hey there")