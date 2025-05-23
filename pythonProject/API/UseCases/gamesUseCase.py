from API.DataAccess.GameDataAccess import GameDataAccess
from API.Models.Game import Game

class GamesUseCase:
    def __init__(self):
        self.dataAccess = GameDataAccess()

    def newGame(self, newGame: Game):
        if self.dataAccess.get_game_by_name(newGame.name):
            return False, "Game Already Exists in this context"

        dbGame = self.dataAccess.new_game(newGame)

        if not dbGame:
            return False, "Unable to create new game"
        return True, dbGame

    def updateGame(self, toUpdateGame: Game):
        if not self.dataAccess.get_game_by_id(toUpdateGame.id):
            return False, "No Game with this Id exists"

        dbGame = self.dataAccess.update_game(toUpdateGame)

        if not dbGame:
            return False, "Unable to update game"
        return True, dbGame

    def get_game_by_name(self, game_name):
        game = self.dataAccess.get_game_by_name(game_name)
        if not game:
            return False, "Game Not Found"
        return True, game

    def get_game_by_id(self, game_id):
        game = self.dataAccess.get_game_by_id(game_id)
        if not game:
            return False, "Game Not Found"
        return True, game

    def get_all_games(self):
        games = self.dataAccess.get_all_games()
        if not games:
            return False, "Unable to get all games"
        return True, games