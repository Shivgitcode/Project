import json
import spotipy
import webbrowser

username = 'Eren'
clientID = '42147918e34b4eaa8482b2328aaea180'
clientSecret = '57ff5d28229749f3a0bae8c05afdddd4'
redirect_uri = 'https://www.google.com/'

# modify SpotifyOAuth initialization to add app-remote-control scope
oauth_object = spotipy.SpotifyOAuth(
    client_id=clientID,
    client_secret=clientSecret,
    redirect_uri=redirect_uri,
    scope='app-remote-control'
)

token_dict = oauth_object.get_access_token()
token = token_dict['access_token']
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()

# To print the JSON response from
# browser in a readable format.
# optional can be removed
print(json.dumps(user_name, sort_keys=True, indent=4))

while True:
    print("Welcome to the project, " + user_name['display_name'])
    print("0 - Exit the console")
    print("1 - Search for a Song")
    user_input = int(input("Enter Your Choice: "))
    if user_input == 1:
        search_song = input("Enter the song name: ")
        results = spotifyObject.search(search_song, 1, 0, "track")
        songs_dict = results['tracks']
        song_items = songs_dict['items']
        song_uri = song_items[0]['uri']
        # get the ID of the device to play on
        device_id = spotifyObject.devices()['devices'][0]['id']
        spotifyObject.play(device_id=device_id, uris=[song_uri])
        print('Song is now playing on your device.')
    elif user_input == 0:
        print("Good Bye, Have a great day!")
        break
    else:
        print("Please enter valid user-input.")
