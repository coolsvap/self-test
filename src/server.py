import threading

from flask import (Flask, request, jsonify, abort)

from player import Player
from tournament import Tournament


app = Flask(__name__)
logger = app.logger

# TODO: Refactor this and add facility that sets up tournaments on-demand.
tournament = Tournament(max_players=2)


def _start_tournament(tournament):
    """Quick helper to pass in as thread callback"""
    logger.info('Let the tournament begin!')
    tournament.start()


@app.route('/tournament/connect/', methods=['POST'])
def connect():
    player_id = int(request.form['player_id'])
    player_host = request.form['player_host']
    player_port = int(request.form['player_port'])

    # Players shouldn't be able to 'reset' data by re-connecting
    if tournament.has_player(player_id) or tournament.is_at_max_capacity():
        # TODO: Return proper error message
        return abort(400)
    else:
        player = Player(player_id, player_host, player_port)
        tournament.add_player(player)

    logger.info(
        'Player ID: {} connected!\nWaiting for {} more players...'.format(
            player_id, tournament.get_vacancies()
        )
    )

    # When the final player joins, kick off the tourney
    if tournament.is_at_max_capacity():
        t = threading.Thread(target=_start_tournament, args=(tournament,))
        t.start()

    return jsonify(**{
        'status': 'ok'
    })


if __name__ == '__main__':
    app.run(debug=True)
