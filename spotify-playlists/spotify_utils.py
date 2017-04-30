import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

import keys

os.environ['SPOTIPY_CLIENT_ID'] = keys.SPOTIPY_CLIENT_ID
os.environ['SPOTIPY_CLIENT_SECRET'] = keys.SPOTIPY_CLIENT_SECRET

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_user_playlists(username):
    retval = []
    playlists = sp.user_playlists(username)
    while playlists:
        for i, playlist in enumerate(playlists['items']):
            retval.append(playlist)
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None
    return retval

def append_tracks(tracks, arr):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        arr.append(track)


def get_user_playlist(user_id, playlist_id):
    playlist = sp.user_playlist(user_id, playlist_id, fields="tracks,next,name")
    ret_name = playlist['name']
    tracks = playlist['tracks']
    ret_tracks = []
    append_tracks(playlist['tracks'], ret_tracks)
    while tracks['next']:
        tracks = sp.next(tracks)
        append_tracks(tracks, ret_tracks)
    return { 'tracks': ret_tracks, 'name': ret_name }


