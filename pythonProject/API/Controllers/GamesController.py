from flask import Blueprint, jsonify
from API.UseCases.gamesUseCase import GamesUseCase

games_bp: Blueprint = Blueprint('games', __name__)
gamesUseCase: GamesUseCase = GamesUseCase()

@games_bp.route('/<string:game_name>', methods=['GET'])
def get_game(game_name):
    game = gamesUseCase.get_game_by_name(game_name)
    if game:
        return jsonify(game)
    return jsonify({'error': 'User not found'}), 500

