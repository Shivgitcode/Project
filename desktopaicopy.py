import subprocess
from bs4 import BeautifulStoneSoup
import requests
from pvrecorder import PvRecorder
import time
import pvporcupine
import pyttsx3
import wikipedia
import speech_recognition as sr
import pyaudio
import datetime
import webbrowser
import os
import pywhatkit
import spotipy
import json
import pyjokes
import wolframalpha
import keyboard


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
newvoices = 140
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', newvoices)

username = 'Eren'
clientID = '30fcc1a43d444bc9ab32d0f94fc10b19'
clientSecret = 'f96ed65a76fa440ab0c467815820f571'
redirect_uri = 'https://www.google.com/'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()

print(json.dumps(user_name, sort_keys=True, indent=4))


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning everyone!")
        speak("Hello sir I am Eren ! how may I help you")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon everyone!")
        speak("Hello sir I am Eren ! how may I help you")
    else:
        speak("Good evening everyone!")
        speak("Hello sir I am Eren ! how may I help you")
        speak("how was your day")


def takecommand():
    # it takes microphone input from the user and returns string output
    r = sr.Recognizer()  # this is a class which helps us to recognize audio from the user
    with sr.Microphone() as source:
        speak("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        r.adjust_for_ambient_noise(source, duration=5)
        r.dynamic_energy_threshold = True
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        print(e)
        speak("say that again please ..... ")
        print("say that again please .....")
        return "None"
    return query


def shutdown():
    subprocess.call(["shutdown", "/s"])


while True:
    try:
        if keyboard.is_pressed('1'):
            if __name__ == "__main__":
                wishMe()
                chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

                while True:
                    query = takecommand().lower()

                    # logic for taking commands
                    if 'wikipedia' in query:
                        speak("searching wikipedia")
                        query = query.replace("wikipedia", "")
                        results = wikipedia.summary(query, sentences=2)
                        speak("According to wikipedia")
                        print(results)
                        speak(results)
                    elif 'about shivansh' in query:
                        speak("shivansh is currently working on me . he is a 1st year student at chitkara university in computer science and engineering branch and he likes to play football")
                    elif 'about shweta' in query:
                        speak("shweta is currently working with shivansh on me . she is also a 1st year student at chitkara university in computer science and engineering and she likes to eat brownie with vanilla ice cream ")
                    elif 'open youtube' in query:
                        webbrowser.register(
                            'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        webbrowser.get('chrome').open_new_tab('youtube.com')

                    elif 'open google' in query:
                        webbrowser.register(
                            'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        webbrowser.get('chrome').open_new_tab('google.com')
                    elif 'open chat' in query:
                        webbrowser.register(
                            'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        webbrowser.get('chrome').open_new_tab(
                            'chat.openai.com')
                    elif 'open spotify' in query:
                        webbrowser.register(
                            'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        webbrowser.get('chrome').open_new_tab(
                            'open.spotify.com')
                    elif 'open gmail' in query:
                        webbrowser.register(
                            'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        webbrowser.get('chrome').open_new_tab(
                            'mail.google.com')
                    elif 'the time' in query:
                        strTime = datetime.datetime.now().strftime("%H:%M:%S")
                        speak(f"sir , the time is {strTime}")
                    elif "open code" in query:
                        codepath = "C:\\Users\\shivn\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                        os.startfile(codepath)
                    elif 'thank' in query:
                        speak("thanku for using me , have a great day sir !")
                        break
                    elif 'play song on youtube' in query:
                        speak("which song do you want to play")
                        songorartist = takecommand()
                        pywhatkit.playonyt(songorartist)
                    elif 'play song on spotify' in query:
                        speak("which song do you want to play")
                        search_song = takecommand()
                        results = spotifyObject.search(
                            search_song, 1, 0, "track")
                        songs_dict = results['tracks']
                        song_items = songs_dict['items']
                        song = song_items[0]['external_urls']['spotify']
                        webbrowser.open(song)
                        print('Song has opened in your browser.')
                    elif 'zoro' in query:
                        webbrowser.register(
                            'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        webbrowser.get('chrome').open_new_tab('zoro.to')
                    elif 'instagram' in query:
                        webbrowser.open("www.instagram.com")

                    elif 'git' in query:
                        webbrowser.register(
                            'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        webbrowser.get('chrome').open_new_tab('github.com')

                    elif 'netflix' in query:
                        webbrowser.open('www.netflix.com')

                    elif 'whatsapp' in query:
                        webbrowser.register(
                            'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
                        webbrowser.get('chrome').open_new_tab(
                            'web.whatsapp.com')
                    elif 'joke' in query or 'jokes' in query:
                        myjokes = pyjokes.get_joke(
                            language='en', category='all')
                        speak(myjokes)
                    elif 'calculate' in query:
                        app_id = "9AY2KR-PW27XVJXE6"
                        client = wolframalpha.Client(app_id)
                        indx = query.lower().split().index('calculate')
                        query = query.split()[indx + 1:]
                        res = client.query(' '.join(query))
                        answer = next(res.results).text
                        print("The answer is " + answer)
                        speak("The answer is " + answer)
                    elif 'who is ' in query or 'what is' in query:
                        client = wolframalpha.Client("9AY2KR-PW27XVJXE6")
                        res = client.query(query)

                        try:
                            print(next(res.results).text)
                            speak(next(res.results).text)
                        except StopIteration:
                            print("No results")
                    elif 'open chrome' in query:
                        codepath2 = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                        os.startfile(codepath2)
                    elif 'open telegram' in query:
                        codepath3 = "C:\\Users\\shivn\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
                        os.startfile(codepath3)
                    elif 'open discord' in query:
                        codepath4 = "C:\\Users\\shivn\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe"
                        os.startfile(codepath4)
                    elif 'search on google' in query:
                        speak('what do you want to search')
                        find = takecommand()
                        url = f"https://www.google.com/search?q={find}"

                        webbrowser.open(url)
                    elif 'shutdown' in query:
                        shutdown()
                    elif 'who made you' in query or "who is your owner" in query:
                        speak('I was made by shweta and shivansh on 25 February,2023')
                    elif 'love you' in query:
                        speak(
                            'well ! I am an virtual assistant so it is not possible')
                    elif 'do you like me' in query:
                        speak(
                            'well ! offcourse because you made me . It was you who brought me into this world')
                    elif 'about yourself' in query:
                        speak('Hello ! I am Eren . I was made at chitkara university by two chitkara first year student , shweta and shivansh . I am here to assist you with your daily tasks and chores!')

        else:
            pass
    except:
        pass
