import speech_to_text as stt
import text_to_speech as tts
import time_and_date as td
import system_info as si
import online_web_search as ows
import weather
import open_apps as oa

def process_text(intext):
    intext = intext.lower()

    if "open" in intext:
        apps = ['notepad','paint','calculator','word','excel','chrome','edge','vlc']
        appFound = False

        for app in apps:
            if app in intext:
                tts.speak(f"Opening {app} for you.")
                appFound = True

                if (app == 'paint'):
                    oa.open_app("mspaint")

                elif (app == 'calculator'):
                    oa.open_app("calc")
                
                elif (app == 'word'):
                    oa.open_app("winword")
                
                elif (open == 'edge'):
                    oa.open_app("msedge")
                
                else:
                    oa.open_app(app)
        
        if appFound == False:
            tts.speak("Sorry, no such app found with that name. You can try doing a manual search")
    
    elif "search" in intext:
        if "google" in intext:
            tts.speak("Sure, what do you want to search on google")
            query = stt.listenToHuman()
            ows.web_search(query)
            tts.speak(f"Here are the google search results on {query}")
        
        elif "youtube" in intext:
            tts.speak("Sure, what do you want to search on youtube")
            query = stt.listenToHuman()
            ows.yt_search(query)
            tts.speak(f"Here are the youtube search results on {query}")

        else:
            tts.speak("Sorry, I dont have that search engine available, you can try google or youtube")