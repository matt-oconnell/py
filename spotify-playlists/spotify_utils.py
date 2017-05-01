import os
import pickle
import spotipy
import keys
from spotipy.oauth2 import SpotifyClientCredentials

DATA_DIR = 'data'

client_credentials_manager = SpotifyClientCredentials(
    keys.SPOTIPY_CLIENT_ID,
    keys.SPOTIPY_CLIENT_SECRET
)

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_data_filename(filename):
    return os.path.join(os.path.dirname(__file__), '{}/{}'.format(DATA_DIR, filename))


def get_pickle_or_store(filename, callback):
    file_path = get_data_filename(filename)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as input_file:
            data = pickle.load(input_file)
    else:
        data = callback()
        with open(file_path, 'wb') as f:
            pickle.dump(data, f)
    return data


def append_tracks(tracks, arr):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        arr.append(track)


def get_user_playlists(username):
    ret_val = []
    filename = username + '-playlists.pickle'
    playlists = get_pickle_or_store(filename, lambda: sp.user_playlists(username))

    while playlists:
        for i, playlist in enumerate(playlists['items']):
            ret_val.append(playlist)
        if playlists['next']:
            playlists = sp.next(playlists)
        else:
            playlists = None
    return ret_val


def get_user_playlist(user_id, playlist_id):
    filename = user_id + '-' + playlist_id + '.pickle'
    playlist = get_pickle_or_store(filename, lambda: sp.user_playlist(user_id, playlist_id, fields="tracks,next,name"))

    tracks = playlist['tracks']
    ret_tracks = []
    append_tracks(playlist['tracks'], ret_tracks)
    while tracks['next']:
        tracks = sp.next(tracks)
        append_tracks(tracks, ret_tracks)
    return {'tracks': ret_tracks, 'name':  playlist['name']}
