from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, DateTime, Float

from API.Services.databaseContext import Base

class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    singleplayer = Column(Boolean)
    multiplayer = Column(Boolean)
    releaseDate = Column(DateTime)
    latestUpdate = Column(DateTime)
    downloadSize = Column(Float)
    achievements = Column(Integer)
    mk = Column(Boolean)
    controller = Column(Boolean)

    def __init__(self,
               name,
               singleplayer,
               multiplayer,
               releaseDate,
               latestUpdate,
               downloadSize,
               achievements,
               mk,
               controller):
        self.id = None
        self.name = str(name)
        self.singleplayer = bool(singleplayer)
        self.multiplayer = bool(multiplayer)
        self.releaseDate = datetime.fromisoformat(releaseDate)
        self.latestUpdate = datetime.fromisoformat(latestUpdate)
        self.downloadSize = float(downloadSize)
        self.achievements = int(achievements)
        self.mk = bool(mk)
        self.controller = bool(controller)

    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "singleplayer" : self.singleplayer,
            "multiplayer" : self.multiplayer,
            "releaseDate" : self.releaseDate,
            "latestUpdate" : self.latestUpdate,
            "downloadSize" : self.downloadSize,
            "achievements" : self.achievements,
            "mk" : self.mk,
            "controller" : self.controller
        }
