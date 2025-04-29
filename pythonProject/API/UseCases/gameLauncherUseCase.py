from API.DataAccess.GameDataAccess import GameDataAccess
from API.DataAccess.LauncherDataAccess import LauncherDataAccess
from API.DataAccess.GameLauncherDataAccess import GameLauncherDataAccess

from API.Models import Game, Tag, GameTags

class GameLauncherUseCase:
    def __init__(self):
        self.gameDataAccess = GameDataAccess()
        self.launcherDataAccess = LauncherDataAccess()
        self.gameLauncherDataAccess = GameLauncherDataAccess()

    def add_launcher_to_game(self, gameLauncher):
        if not self.gameDataAccess.game_exists_by_id(gameLauncher.gameId):
            return False, "Game Does not exist"

        if not self.launcherDataAccess.launcherExistsById(gameLauncher.launcherId):
            return False, "Tag Does not exist"

        gameLauncher = self.gameLauncherDataAccess.new_game_launcher(gameLauncher)
        if not gameLauncher:
            return False, "Unable to add new tag to game"

        return True, gameLauncher

    def get_game_launcher(self, gameId):
        if not self.gameDataAccess.game_exists_by_id(gameId):
            return False, "Game Does not exist"

        gameLauncher = self.gameLauncherDataAccess.get_launcher_for_game(gameId)
        if not gameLauncher:
            return False, "Unable to get game launcher"
        return True, gameLauncher