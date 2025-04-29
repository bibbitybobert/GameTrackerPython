from flask import Blueprint, jsonify, request

from API.Controllers.GamesController import gameLauncherUseCase
from API.UseCases.launchersUseCase import LauncherUseCase

launcher_bp: Blueprint = Blueprint('Launcher', __name__)
launcherUseCase: LauncherUseCase = LauncherUseCase()

@launcher_bp.route('/newLauncher', methods=['POST'])
def newLauncher():
    data = request.get_json()
    name = data['name']

    result, newLauncher = launcherUseCase.newLauncher(name)
    if result:
        return jsonify(newLauncher.to_dict()), 200
    return jsonify({'error': 'Unable to create new Launcher'}), 500

@launcher_bp.route('/getAllLaunchers', methods=['GET'])
def getAllLaunchers():
    result, launchers = launcherUseCase.getAllLaunchers()
    if result:
        returnLaunchers = []
        for launcher in launchers:
            returnLaunchers.append(launcher.to_dict())
        return jsonify(returnLaunchers), 200
    return jsonify({'error': 'Unable to get all Launchers'}), 500

@launcher_bp.route('/getGameLauncher/<int:gameId>', methods=['GET'])
def getGameLauncher(gameId):
    result, launcher = gameLauncherUseCase.get_game_launcher(gameId)
    if result:
        return jsonify(launcher.to_dict()), 200
    return jsonify({'error': 'Unable to get game launcher'}), 500