from flask import Flask, jsonify
import twitter_utils

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(twitter_utils.getParkingTweets())

@app.route('/test')
def test():
    return jsonify(twitter_utils.getParkingTweets())

if __name__ == "__main__":
    app.run()
