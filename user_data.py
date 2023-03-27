import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="fdbdeeb74de2412eab01a82a453a0eb3",
                                                           client_secret="d2ccf8e74aca46c888f470699ced19e4"))

results = sp.search(q='weezer', limit=20)
for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])
