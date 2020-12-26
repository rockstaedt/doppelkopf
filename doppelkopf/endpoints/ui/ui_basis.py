from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    url_for,
    redirect
)
from datetime import datetime
import pandas as pd
from sqlalchemy import select

from doppelkopf.extensions import db

from doppelkopf.models import Player, Game, Result

from doppelkopf.resource_models import (
    result_rm,
    player_rm
)

ui_basis = Blueprint('ui_basis', __name__)

# @ui_basis.route('/home', methods = ['GET'])
# # @basis.route('/#spielliste', methods = ['GET'])
# # @basis.route('/#rangliste', methods = ['GET'])
# def home():
#     games = Game.query.order_by(Game.date).all()
#     players = Player.query.order_by(Player.name).all()
#     player_results = {}
#     for game in games:
#         player_results[game.id] = result_rm.get_player_results(
#             game_id = game.id
#         )
#     player_statistics = {}
#     for player in players:
#         # update here again because one player is always missing
#         # in game update / save / delete
#         player_rm.update_game_statistics(player.id)
#         db.session.commit()
#         player_statistics[player.id] = player_rm.get_game_statistic_player(
#             player.id
#         )
#     players_ranked = Player.query.order_by(Player.ranking).all()
#     # return render_template('index.html',
#     #     games = games,
#     #     players = players,
#     #     players_ranked  = players_ranked,
#     #     player_results = player_results,
#     #     player_statistics =  player_statistics
#     # )

@ui_basis.route('/', methods=['GET'])
def start():
    return render_template('start.html')

@ui_basis.route('/home', methods=['GET'])
def home():
    games= Game.query.order_by(Game.date).all()
    games_count = len(games)
    return render_template(
        'home.html',
        games_count = games_count
    )
