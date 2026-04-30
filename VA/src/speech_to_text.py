import speech_recognition as sr

r = sr.Recognizer()
r.pause_threshold = 2

def listenToHuman():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source,duration=2)
        print("Speak Now...")

        try:
            audio = r.listen(source)
        except sr.WaitTimeoutError:
            print("Session Timed Out: No Audio Detected")

    inText = ""
    try:
        print("Processing Audio...")
        inText = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
    
    return inText