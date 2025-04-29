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


    def update_game(self, toUpdateGame: Game):
        session = Session()
        try:
            dbGame = session.query(Game).filter_by(id=toUpdateGame.id).first()
            if dbGame:
                dbGame.name = toUpdateGame.name
                dbGame.singleplayer = toUpdateGame.singleplayer
                dbGame.multiplayer = toUpdateGame.multiplayer
                dbGame.releaseDate = toUpdateGame.releaseDate
                dbGame.latestUpdate = toUpdateGame.latestUpdate
                dbGame.downloadSize = toUpdateGame.downloadSize
                dbGame.achievements = toUpdateGame.achievements
                dbGame.mk = toUpdateGame.mk
                dbGame.controller = toUpdateGame.controller
                session.commit()
            return session.query(Game).filter_by(id=toUpdateGame.id).first()
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