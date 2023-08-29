from __future__ import print_function 
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

load_dotenv()

sp_client_id = os.getenv("SP_CLIENT_ID")
sp_client_secret = os.getenv("SP_CLIENT_SECRET")
g_client_id = os.getenv("G_CLIENT_ID")
g_client_secret = os.getenv("G_CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=sp_client_id, client_secret=sp_client_secret))

def song_features(id: str):
    # id = 'https://open.spotify.com/track/795p3jKj5stjPf8IFpZkdD?si=MUzR8Y2rQs6h4s4vsbGr5g'

    features = sp.audio_features([id])[0]

    return features