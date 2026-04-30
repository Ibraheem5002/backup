import speech_to_text as stt
import text_to_speech as tts
import time_and_date as td
import system_info as si
import online_web_search as ows
import weather
import open_apps as oa
import text_processing as tp
import os

intext = stt.listenToHuman()

while (True):
    if 'exit' in intext:
        tts.speak("Hope I was helpful to you. See you later")
        break
    else:
        os.system("cls")
        tp.process_text(intext)
        tts.speak("How can I be more helpful for you")
        intext = stt.listenToHuman()