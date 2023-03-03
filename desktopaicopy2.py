import datetime
import os
import subprocess
import webbrowser

import pyttsx3  # pip install pyttsx3
import pywhatkit
import speech_recognition as sr  # pip install speechRecognition
import spotipy
import wikipedia  # pip install wikipedia
import wolframalpha
from pyjokes import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

# Shweta's api keys
# clientID = '42147918e34b4eaa8482b2328aaea180'
# clientSecret = '57ff5d28229749f3a0bae8c05afdddd4'

# My Api Keys
clientID = "cb5e9743b4b04366b8387fe58f53f713"
clientSecret = "28ce3775643143c18830e4858d123eb9"
redirect_uri = 'https://www.google.com/'
oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()

chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"


def shutdown():
    subprocess.call(["shutdown", "/s"])


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")

    elif 12 <= hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Please tell me how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name_ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'play song on spotify' in query:
            speak("which song do you want to play")
            search_song = takeCommand()
            results = spotifyObject.search(
                search_song, 1, 0, "track")
            songs_dict = results['tracks']
            song_items = songs_dict['items']
            song = song_items[0]['external_urls']['spotify']
            webbrowser.open(song)
            print('Song has opened in your browser.')
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'zoro' in query:
            webbrowser.open("zoro.to")
        elif 'instagram' in query:
            webbrowser.open("www.instagram.com")
        elif 'git' in query:
            webbrowser.open("github.com")
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
        elif 'who is ' in query or 'what is' in query:
            # Shweta's Id
            # client = wolframalpha.Client("9AY2KR-PW27XVJXE6")

            # My Wolframaplha id
            client = wolframalpha.Client(app_id="6QK9JX-XLAT737JUH")
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
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif 'open code' in query:
            codePath = "C:\\Users\\yashk\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'search on google' in query:
            speak('what do you want to search')
            find = takeCommand()
            url = f"https://www.google.com/search?q={find}"

            webbrowser.open(url)
        if 'about shivansh' in query:
            speak(
                "shivansh is currently working on me . he is a 1st year student at chitkara university in computer science and engineering branch and he likes to play football")
        elif 'about shweta' in query:
            speak(
                "shweta is currently working with shivansh on me . she is also a 1st year student at chitkara university in computer science and engineering and she likes to eat brownie with vanilla ice cream ")
        elif 'open chat gpt' in query:
            webbrowser.register(
                'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(
                'chat.openai.com')
        elif 'open spotify' in query:
            webbrowser.register(
                'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(
                'open.spotify.com')
        elif 'play song on youtube' in query:
            speak("which song do you want to play")
            songorartist = takeCommand()
            pywhatkit.playonyt(songorartist)
        elif 'who made you' in query or "who is your owner" in query:
            speak('I was made by shweta and shivansh on 25 February,2023')
        elif 'I love you' in query:
            speak(
                'well ! I am an virtual assistant so it is not possible')
        elif 'do you like me' in query:
            speak(
                'well ! offcourse because you made . It was you who brought me into this world')
        elif 'about yourself' in query:
            speak(
                'Hello ! I am Eren . I was made at chitkara university by two chitkara first year student , shweta and shivansh . I am here to assist you with your daily tasks and chores!')

        elif 'open gmail' in query:
            webbrowser.register(
                'chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(
                'mail.google.com')
        elif 'thank' in query:
            speak("thanku for using me , have a great day sir !")
            break
        elif 'shutdown' in query:
            shutdown()
