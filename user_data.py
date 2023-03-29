"""
CSC111 Winter 2023 Project:
MelodyMatch: Tailored Music Recommendations Derived From Your Spotify Habits

This Python module contains the code that will run the local server used by the user to
log in with their Spotify account credentials.

Notes
===============================
This file contains code borrowed directly from the Spotipy library documentation, which
can be found at the following link.
    - https://spotipy.readthedocs.io/en/2.22.1/#

Contributors: Manaljav Munkhbayar, Kevin Hu, Stanley Pang, Jaeyong Lee.
"""

from bottle import route, run, request, WSGIRefServer, Bottle
from spotipy import oauth2
import spotipy
import os

# The Spotify OAuth object contains the access token and refresh
# token required to make authenticated requests to the Spotify Web API
sp_oauth = oauth2.SpotifyOAuth(client_id='2aef90bcdc834c17b59ff1358099865a',
                               client_secret='2ab27bed30c441aab581dbac673736f2',
                               redirect_uri='http://localhost:8080',
                               scope='user-library-read',
                               )

track_names = []

# The decorator maps the specified function to the root URL path
@route('/')
def get_access_token():
    token_info = sp_oauth.get_access_token()
    access_token = ""

    global track_names

    if token_info:
        print("Found access token!")
        access_token = token_info['access_token']
    else:
        code = sp_oauth.parse_response_code(request.url)
        if code:
            print("Found Spotify auth code in Request URL! Trying to get valid access token...")
            token_info = sp_oauth.get_access_token(code)
            access_token = token_info['access_token']

    if access_token:
        print("Access token available! Trying to get user information...")
        sp = spotipy.Spotify(access_token)  # create a Spotify object authenticated with our acess token
        saved_tracks = sp.current_user_saved_tracks(limit=50)
        track_names = [track['track']['name'] for track in saved_tracks['items']]
        print(track_names)
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
        return "<a href='" + sp_oauth.get_authorize_url() + "'>Login to Spotify</a>"


run(host='')  # this starts the server
