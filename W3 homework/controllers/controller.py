from flask import render_template, request
from app import app
from models.player import Player
from models.game_functions import players, add_new_player


@app.route("/game")
def index():
    return render_template("index.html", title="Home", players=players)


@app.route("/game")
def add_player():
    player_name = request.form["event_date"]
    player_choice = request.form["event_name"]
    new_player = Player(player_name, player_choice)
    add_new_player(new_player)

    return render_template("index.html", title="Home", players=players)
