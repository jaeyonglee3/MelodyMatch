# Gets all the public playlists for the given
# user. Uses Client Credentials flow
#

import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="fdbdeeb74de2412eab01a82a453a0eb3",
                                                           client_secret="d2ccf8e74aca46c888f470699ced19e4"))

user = 'spotify'

if len(sys.argv) > 1:
    user = sys.argv[1]

playlists = sp.user_playlists(user)

while playlists:
    for i, playlist in enumerate(playlists['items']):
        print(
            "%4d %s %s" %
            (i +
             1 +
             playlists['offset'],
             playlist['uri'],
             playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
