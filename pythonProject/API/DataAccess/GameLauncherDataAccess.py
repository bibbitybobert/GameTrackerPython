from API.Services.databaseContext import *

from API.Models.Game import Game
from API.Models.Launcher import Launcher
from API.Models.GameLauncher import GameLauncher

class GameLauncherDataAccess:
    def new_game_launcher(self, newGameLauncher):
        session = Session()
        try:
            session.add(newGameLauncher)
            session.commit()
            return session.query(GameLauncher).filter(GameLauncher.gameId == newGameLauncher.gameId
                                                  and GameLauncher.launcherId == newGameLauncher.launcherId).first()
        except Exception as e:
            print(e)
            return False
        finally:
            session.close()

    def get_launcher_for_game(self, gameId):
        session = Session()
        try:
            return session.query(GameLauncher).filter(GameLauncher.gameId == gameId).first()
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()

    def get_games_for_launcher(self, launcherId):
        session = Session()
        try:
            games = []
            LauncherGames = session.query(GameLauncher).filter(GameLauncher.launcherId == launcherId).all()
            for gamelauncher in LauncherGames:
                games.append(session.query(Game).filter(Game.id == gamelauncher.gameId).first())

            return games
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()