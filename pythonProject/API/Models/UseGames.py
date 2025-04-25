from sqlalchemy import Column, Integer, String

from API.Services.databaseContext import Base

class UserGame(Base):
    __tablename__ = 'UserGame'

    userId = Column(String(255), foreign_key=True)
    gameId = Column(Integer, foreign_key=True)

    def __init__(self, userId, gameId):
        self.userId = userId
        self.gameId = gameId

    def to_dict(self):
        return {
            'userId': self.userId,
            'gameId': self.gameId
        }