from flask import Flask, request, jsonify
from flask_cors import CORS

from actual_hitokara import lyrics
from actual_hitokara.recomendations import Recomendations
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


@app.route("/recomendations/<genre>", methods=["GET"])
def get_recomendations(genre):
    recomendations = Recomendations()

    if genre == "pop":
        return jsonify(recomendations.pop_hits())
    elif genre == "hip_hop":
        return jsonify(recomendations.hip_hop_hits())
    elif genre == "indie":
        return jsonify(recomendations.indie_hits())
    elif genre == "rock":
        return jsonify(recomendations.rock_hits())
    else:
        return jsonify({"Error": "Invalid genre"})


@app.route("/search", methods=["GET"])
def search_songs():
    data = request.get_json()
    query = data["query"]

    return jsonify(search.search_song(query))


if __name__ == "__main__":
    app.run(debug=True)
