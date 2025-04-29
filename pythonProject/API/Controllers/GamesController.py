from flask import Blueprint, jsonify, request

from API.Models.GameLauncher import GameLauncher
from API.UseCases.gamesUseCase import GamesUseCase
from API.UseCases.gameTagsUseCase import GameTagsUseCase
from API.UseCases.gameLauncherUseCase import GameLauncherUseCase
from API.Models.Game import Game
from API.Models.GameTags import GameTags

games_bp: Blueprint = Blueprint('games', __name__)
gamesUseCase: GamesUseCase = GamesUseCase()
gameTagsUseCase: GameTagsUseCase = GameTagsUseCase()
gameLauncherUseCase: GameLauncherUseCase = GameLauncherUseCase()

@games_bp.route('/<int:game_id>', methods=['GET'])
def get_game_by_id(game_id):
    result, game = gamesUseCase.get_game_by_id(game_id)
    if result:
        return jsonify(game.to_dict()), 200
    return jsonify({'error': 'User not found'}), 500

@games_bp.route('/allGames', methods=['GET'])
def get_all_games():
    result, games = gamesUseCase.get_all_games()
    if result:
        gamesJson = []
        for game in games:
            gamesJson.append(game.to_dict())
        return jsonify(gamesJson), 200
    return jsonify({'error': 'Unable to get all games'}), 400

@games_bp.route('/newGame', methods=['POST'])
def new_game():
    data = request.get_json()
    name = data["name"]
    singleplayer = data["singleplayer"]
    multiplayer = data["multiplayer"]
    releaseDate = data["releaseDate"]
    latestUpdate = data["latestUpdate"]
    downloadSize = data["downloadSize"]
    achievements = data["achievements"]
    mkSupport = data["mkSupport"]
    controllerSupport = data["controllerSupport"]
    newGame = Game(name, singleplayer, multiplayer, releaseDate, latestUpdate, downloadSize, achievements, mkSupport, controllerSupport)

    response, dbGame = gamesUseCase.newGame(newGame)
    if response:
        return jsonify(dbGame.to_dict()), 200
    return jsonify({'error': 'Game not found'}), 400

@games_bp.route('/updateGame', methods=['POST'])
def update_game():
    data = request.get_json()
    id = data["id"]
    name = data["name"]
    singleplayer = data["singleplayer"]
    multiplayer = data["multiplayer"]
    releaseDate = data["releaseDate"]
    latestUpdate = data["latestUpdate"]
    downloadSize = data["downloadSize"]
    achievements = data["achievements"]
    mkSupport = data["mkSupport"]
    controllerSupport = data["controllerSupport"]
    toUpdateGame = Game(name, singleplayer, multiplayer, releaseDate, latestUpdate, downloadSize, achievements, mkSupport, controllerSupport)
    toUpdateGame.id = id

    response, dbGame = gamesUseCase.updateGame(toUpdateGame)
    if response:
        return jsonify(dbGame.to_dict()), 200
    return jsonify({'error': 'Game not found'}), 400

@games_bp.route('/<int:game_id>/addTag/<int:tag_id>', methods=['POST'])
def add_tag(game_id, tag_id):
    gameTag = GameTags(game_id, tag_id)
    response, gameTag = gameTagsUseCase.add_tag_to_game(gameTag)
    if response:
        return jsonify(gameTag.to_dict()), 200
    return jsonify({'error': 'Unable to add tag to game'}), 400

@games_bp.route('/<int:game_id>/addLauncher/<int:launcher_id>', methods=['POST'])
def add_launcher(game_id, launcher_id):
    gameLauncher = GameLauncher(game_id, launcher_id)
    response, gameLauncher = gameLauncherUseCase.add_launcher_to_game(gameLauncher)
    if response:
        return jsonify(gameLauncher.to_dict()), 200
    return jsonify({'error': 'Unable to add launcher to game'}), 400




