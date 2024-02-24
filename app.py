from flask import Flask, request, jsonify
from flask_cors import CORS

from actual_hitokara import lyrics
from actual_hitokara.recommendations import Recommendations
from actual_hitokara import search

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/lyrics", methods=["POST"])
def get_lyrics():
    data = request.get_json()
    print(data)
    artist_name = data["artist_name"]
    song_name = data["song_name"]

    if data["lang"] == "en":
        return jsonify(lyrics.en_fetch_lyrics(artist_name, song_name))
    else:
        return jsonify(lyrics.hn_fetch_lyrics(artist_name, song_name))


@app.route("/recommendations/<genre>", methods=["GET"])
def get_recommendations(genre):
    recommendations = Recommendations()

    if genre == "pop":
        return jsonify(recommendations.pop_hits())
    elif genre == "hip_hop":
        return jsonify(recommendations.hip_hop_hits())
    elif genre == "indie":
        return jsonify(recommendations.indie_hits())
    elif genre == "rock":
        return jsonify(recommendations.rock_hits())
    else:
        return jsonify({"Error": "Invalid genre"})


@app.route("/search", methods=["GET"])
def search_songs():
    data = request.get_json()
    query = data["query"]

    return jsonify(search.search_song(query))


if __name__ == "__main__":
    app.run(debug=True)
