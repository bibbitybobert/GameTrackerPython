from API.Services.databaseContext import *

from API.Models.Game import Game
from API.Models.Tag import Tag
from API.Models.GameTags import GameTags

class GameTagsDataAccess:
    def new_game_tag(self, newGameTag):
        session = Session()
        try:
            session.add(newGameTag)
            session.commit()
            return session.query(GameTags).filter(GameTags.gameId == newGameTag.gameId
                                                  and GameTags.tagId == newGameTag.tagId).first()
        except Exception as e:
            print(e)
            return False
        finally:
            session.close()

    def get_tags_for_game(self, gameId):
        session = Session()
        try:
            tags = []
            gameTags = session.query(GameTags).filter(GameTags.gameId == gameId).all()
            for gametag in gameTags:
                tags.append(session.query(Tag).filter(Tag.id == gametag.tagId).first())

            return tags
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()

    def get_games_for_tag(self, tagId):
        session = Session()
        try:
            games = []
            gameTags = session.query(GameTags).filter(GameTags.tagId == tagId).all()
            for gametag in gameTags:
                games.append(session.query(Game).filter(Game.id == gametag.gameId).first())

            return games
        except Exception as e:
            print(e)
            return None
        finally:
            session.close()
