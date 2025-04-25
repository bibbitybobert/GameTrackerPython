from API.Services.databaseContext import *
from API.Models.Game import Game

class GameDataAccess:
    def new_game(self, newGame: Game):
        session = Session()
        try:
            session.add(newGame)
            session.commit()
            return session.query(Game).filter_by(name=newGame.name).first()
        except Exception as e:
            print(e)
            return False
        finally:
            session.close()

    def game_exists_by_id(self, gameId):
        session = Session()
        try:
            game = session.query(Game).filter_by(id=gameId).first()
            if game:
                return True
            return False
        except Exception as e:
            print(e)
            return False
        finally:
            session.close()

    def get_game_by_id(self, gameId):
        session = Session()
        try:
            return session.query(Game).filter_by(id=gameId).first()
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()

    def get_game_by_name(self, gameName):
        session = Session()
        try:
            return session.query(Game).filter_by(name=gameName).first()
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()

    def get_all_games(self):
        session = Session()
        try:
            return session.query(Game).all()
        except Exception as e:
            print(e)
            return False
        finally:
            session.close()