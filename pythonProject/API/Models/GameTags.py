from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from API.Services.databaseContext import Base
from API.Models.Game import Game
from API.Models.Tag import Tag

class GameTags(Base):
    __tablename__ = 'GameTags'

    gameId = Column(Integer, ForeignKey(Game.id), primary_key=True)
    tagId = Column(Integer, ForeignKey(Tag.id), primary_key=True)

    game = relationship("Game", foreign_keys='GameTags.gameId', lazy='joined')
    tag = relationship("Tag", foreign_keys='GameTags.tagId', lazy='joined')

    def __init__(self, gameId, tagId):
        self.gameId = gameId
        self.tagId = tagId

    def to_dict(self):
        return {
            'game': self.game.to_dict(),
            'tag': self.tag.to_dict(),
        }