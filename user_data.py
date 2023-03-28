from flask import Flask, url_for, session, request, redirect
import spotipy
import time
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)

# secret key used to sign the session cookie
app.secret_key = 'Dmd2nI8H34fds'
app.config['SESSION_COOKIE_NAME'] = 'spotify-login-session'
TOKEN_INFO = "token_info"


@app.route('/')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


@app.route('/redirect')
def redirectPage():
    sp_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')  # use the request object to get an access code
    token_info = sp_oauth.get_access_token(code)  # use the code to retrieve an access token
    session[TOKEN_INFO] = token_info  # save the token info into the session
    return redirect(url_for('get_tracks', _external=True))


@app.route('/getTracks')
def get_tracks():
    # todo video @6:30
    try:
        token_info = get_token()
    except:
        print("user not logged in")
        return redirect(url_for("login", _external=False))  # get redirected to the login page if no token data found

    # Now, create a spotify api client instance.
    # It can be used to authenticate a user with Spotify, and to make requests to the API on behalf of that user.
    sp = spotipy.Spotify(auth=token_info['access_token'])
    return str(sp.current_user_saved_tracks(limit=50, offset=0)['items'][0])


def get_token():
    token_info = session.get(TOKEN_INFO, None)  # get the value from the dictionary
    if not token_info:
        raise Exception("The token does not exist")

    # check if token is expired
    curr_time = int(time.time())
    if token_info['expires_at'] - curr_time < 60:
        sp_oauth = create_spotify_oauth()
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])

    return token_info


def create_spotify_oauth():
    return SpotifyOAuth(
            client_id="2aef90bcdc834c17b59ff1358099865a",
            client_secret="2ab27bed30c441aab581dbac673736f2",
            redirect_uri=url_for('redirectPage', _external=True),
            scope="user-library-read")


if __name__ == '__main__':
    app.run()
