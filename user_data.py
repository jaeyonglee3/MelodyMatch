import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="fdbdeeb74de2412eab01a82a453a0eb3",
                                               client_secret="d2ccf8e74aca46c888f470699ced19e4",
                                               redirect_uri="https://github.com/Manal-jpg/csc111-group-project",
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx*1000, track['artists'][0]['name'], " – ", track['name'])
