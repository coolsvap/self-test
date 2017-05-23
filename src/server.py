from flask import Flask, jsonify, request
import requests
import json
from player import Player

player_file = open('/data/player.json', 'r')
player_data = json.load(player_file)
player = Player(player_data)
app = Flask('ping_pong_player:' + str(player.id))
logger = app.logger
	
@app.route('/choose-number/', methods=['POST'])
def choose_number():
    player.choose_number()
    return jsonify(**{
        'chosen_number': player.get_chosen_number()
    })


@app.route('/make-defense-matrix/', methods=['POST'])
def make_defense_matrix():
    player.make_defense_matrix()
    return jsonify(**{
        'defense_matrix': player.get_defense_matrix()
    })


def _shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the werkzeug server')
    func()


@app.route('/shutdown/', methods=['POST'])
def shutdown():
    _shutdown_server()
    msg = 'Player {} is shutting down...'.format(player.id)
    logger.info(msg)
    return msg

@app.route('/connect/', methods=['POST'])
def connect_to_referee():
    referee_host = 'localhost'
    referee_port = 5000
    url = 'http://{host}:{port}/tournament/connect/'.format(
        host=referee_host, port=referee_port
    )
    requests.post(url, data={
        'player_id': player.id,
        'player_host': player.host,
        'player_port': player.port
    })

    # TODO: This logger doesn't work since 'app' isn't runnning yet.
    logger.info('Player ID: {} is connected to server!'.format(player.id))
    logger.info('what')
    return jsonify(**{
        'player': player.__dict__
    })

@app.route('/player/', methods=['GET'])
def get_players():
    return jsonify(**{
        'player': player.__dict__
    })


if __name__ == '__main__':
    app.run(debug=True)
