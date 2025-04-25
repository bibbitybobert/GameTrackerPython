from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from API.Services.databaseContext import Base
from API.Models.Game import Game
from API.Models.Launcher import Launcher

class GameLauncher(Base):
    __tablename__ = 'GameLauncher'

    gameId = Column(Integer, ForeignKey(Game.id), primary_key=True)
    launcherId = Column(Integer, ForeignKey(Launcher.id), primary_key=True)

    game = relationship('Game', foreign_keys='GameLauncher.gameId', lazy='joined')
    launcher = relationship('Launcher', foreign_keys='GameLauncher.launcherId', lazy='joined')

    def __init__(self, gameId, launcherId):
        self.gameId = gameId
        self.launcherId = launcherId

    def to_dict(self):
        return {
            'game': self.game.to_dict(),
            'launcher': self.launcher.to_dict()
        }