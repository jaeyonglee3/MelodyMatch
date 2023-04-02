"""
CSC111 Winter 2023 Project:
MelodyMatch: Tailored Music Recommendations Derived From Your Spotify Habits

This Python module contains the code that will run the local server used by the user to
log in with their Spotify account credentials.

Notes
===============================
This file contains code borrowed directly from the Spotipy library documentation, which
can be found at this link:
    - https://spotipy.readthedocs.io/en/2.22.1/#

Contributors: Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.
"""
from bottle import route, request
from spotipy import oauth2

import spotipy
import csv
import bottle

app = bottle.default_app()

# The Spotify OAuth object contains the access token and refresh
# token required to make authenticated requests to the Spotify Web API
sp_oauth = oauth2.SpotifyOAuth(client_id='2aef90bcdc834c17b59ff1358099865a',
                               client_secret='2ab27bed30c441aab581dbac673736f2',
                               redirect_uri='http://localhost:8080',
                               scope='user-library-read, user-top-read',
                               )

# Initialize empty lists to store the attributes of the user's top songs
top_tracks_ids = []
top_tracks_names = []
top_tracks_danceability = []
top_tracks_energy = []
top_tracks_loudness = []
top_tracks_speechiness = []
top_tracks_acousticness = []
top_tracks_instrumentalness = []
top_tracks_valence = []
top_tracks_liveness = []
top_tracks_tempo = []


# The decorator maps the specified function to the root URL path
@route('/')
def get_access_token():
    """
    This function does several things:
        - Obtain an access token by calling the get_access_token method on the Spotify OAuth object.
        - If an access token is successfully retrieved, create a "Spotify" object with said token.
        - Make the API call to obtain the user's top 50 tracks.
        - The return value of this function is what gets sent back to the client that made the request, in
            this case being HTML code displayed in the user's browser.
    """
    global top_tracks_ids, top_tracks_names, top_tracks_danceability, top_tracks_energy, top_tracks_loudness, \
        top_tracks_speechiness, top_tracks_acousticness, top_tracks_instrumentalness, top_tracks_valence, \
        top_tracks_liveness, top_tracks_tempo

    token_info = sp_oauth.get_access_token()
    access_token = ""

    if token_info:
        print("Access token found.")
        access_token = token_info['access_token']
    else:
        code = sp_oauth.parse_response_code(request.url)
        if code:
            print("Found Spotify auth code in Request URL. Trying to get valid access token...")
            token_info = sp_oauth.get_access_token(code)
            access_token = token_info['access_token']

    if access_token:
        sp = spotipy.Spotify(access_token)
        top_tracks = sp.current_user_top_tracks(limit=50, offset=0, time_range='medium_term')
        top_tracks_names = [track['name'] for track in top_tracks['items']]
        top_tracks_ids = [track['id'] for track in top_tracks['items']]
        audio_features = sp.audio_features(top_tracks_ids)  # Load the audio features of every song using its ID

        print(type(top_tracks))

        for i in range(len(top_tracks_ids)):
            top_tracks_danceability.append(audio_features[i]['danceability'])
            top_tracks_energy.append(audio_features[i]['energy'])
            top_tracks_loudness.append(audio_features[i]['loudness'])
            top_tracks_speechiness.append(audio_features[i]['speechiness'])
            top_tracks_acousticness.append(audio_features[i]['acousticness'])
            top_tracks_instrumentalness.append(audio_features[i]['instrumentalness'])
            top_tracks_valence.append(audio_features[i]['valence'])
            top_tracks_liveness.append(audio_features[i]['liveness'])
            top_tracks_tempo.append(audio_features[i]['tempo'])

        # todo delete this
        for i in range(len(top_tracks_names)):
            print(str(i + 1) + '. ' + str(top_tracks_names[i]))

        write_to_csv()

        # stop_server()
        return '''
        <html>
            <head>
                <title>MelodyMatch</title>
            </head>
            <body>
                <h1>Got it! We've collected the data we need</h1>
                <p>You may now close this tab and hit ctrl+c to stop the server!</p>
            </body>
        </html>
        '''

    else:
        # return "<a href='" + sp_oauth.get_authorize_url() + "'>Login to Spotify</a>"
        return '''
                <html>
                    <head>
                        <title>MelodyMatch</title>
                    </head>
                    <body>
                        <h1>Error Obtaining Access Token</h1>
                        <p>We were unable to gain access to your Spotify account.</p>
                    </body>
                </html>
                '''


def run_server() -> None:
    """Run the bottle server."""
    # global server
    # server = run(host='')
    bottle.run(app, host='')


def write_to_csv() -> None:
    """Writes the attributes of the top songs belonging to the user in a new CSV file
    """
    with open('data/user_top_songs.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file, delimiter=',')

        for i in range(len(top_tracks_ids)):
            writer.writerow([top_tracks_ids[i], top_tracks_names[i], top_tracks_danceability[i], top_tracks_energy[i],
                            top_tracks_loudness[i], top_tracks_speechiness[i], top_tracks_acousticness[i],
                            top_tracks_instrumentalness[i], top_tracks_valence[i], top_tracks_liveness[i],
                            top_tracks_tempo[i]])
