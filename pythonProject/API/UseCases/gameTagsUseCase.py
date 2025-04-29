from API.DataAccess.GameDataAccess import GameDataAccess
from API.DataAccess.TagDataAccess import TagDataAccess
from API.DataAccess.GameTagsDataAccess import GameTagsDataAccess

from API.Models import Game, Tag, GameTags

class GameTagsUseCase:
    def __init__(self):
        self.gameDataAccess = GameDataAccess()
        self.tagDataAccess = TagDataAccess()
        self.gameTagsDataAccess = GameTagsDataAccess()

    def add_tag_to_game(self, gameTag):
        if not self.gameDataAccess.game_exists_by_id(gameTag.gameId):
            return False, "Game Does not exist"

        if not self.tagDataAccess.tag_exists_by_id(gameTag.tagId):
            return False, "Tag Does not exist"

        gameTag = self.gameTagsDataAccess.new_game_tag(gameTag)
        if not gameTag:
            return False, "Unable to add new tag to game"

        return True, gameTag

    def get_tags_for_game(self, gameId):
        if not self.gameDataAccess.game_exists_by_id(gameId):
            return False, "Game Does not exist"

        tags = self.gameTagsDataAccess.get_tags_for_game(gameId)
        if not tags:
            return False, "Unable to get tags for game"

        return True, tags