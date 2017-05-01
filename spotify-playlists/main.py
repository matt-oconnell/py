from flask import Flask, jsonify, render_template, request
import spotify_utils

app = Flask(__name__)


@app.route('/playlists/')
@app.route('/playlists/<username>')
def playlists(username=None):
    if not username:
        return 'Username required! Example: playlists/my_username'
    playlists_list = spotify_utils.get_user_playlists(username)
    return render_template('playlists.html', user=username, playlists=playlists_list)


@app.route('/playlist')
def playlist():
    user_id = request.args.get('user_id')
    playlist_id = request.args.get('playlist_id')
    playlist_data = spotify_utils.get_user_playlist(user_id, playlist_id)
    return render_template('playlist.html',
                           count=len(playlist_data['tracks']),
                           name=playlist_data['name'],
                           tracks=playlist_data['tracks'])


if __name__ == "__main__":
    # app.run()
    app.run(debug=True)
