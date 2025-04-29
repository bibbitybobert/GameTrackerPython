from datetime import datetime
from sqlalchemy import Column, String, Boolean, Integer, DateTime, Float

from API.Services.databaseContext import Base

class Game(Base):
    __tablename__ = 'game'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255), unique=True, nullable=False)
    singleplayer = Column(Integer)
    multiplayer = Column(Integer)
    releaseDate = Column(DateTime)
    latestUpdate = Column(DateTime)
    downloadSize = Column(Float)
    achievements = Column(Integer)
    mk = Column(Integer)
    controller = Column(Integer)

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
        self.releaseDate = datetime.fromisoformat(releaseDate)
        self.latestUpdate = datetime.fromisoformat(latestUpdate)
        self.downloadSize = float(downloadSize)
        self.achievements = int(achievements)

        if singleplayer == 'true':
            self.singleplayer = 1
        else:
            self.singleplayer = 0

        if multiplayer == 'true':
            self.multiplayer = 1
        else:
            self.multiplayer = 0

        if mk == 'true':
            self.mk = 1
        else:
            self.mk = 0

        if controller == 'true':
            self.controller = 1
        else:
            self.controller = 0

    def to_dict(self):
        if(self.singleplayer == b'\x01'):
            self.singleplayer = 1
        else:
            self.singleplayer = 0

        if (self.multiplayer == b'\x01'):
            self.multiplayer = 1
        else:
            self.multiplayer = 0

        if (self.mk == b'\x01'):
            self.mk = 1
        else:
            self.mk = 0

        if (self.controller == b'\x01'):
            self.controller = 1
        else:
            self.controller = 0

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
