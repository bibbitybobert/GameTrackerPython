from sqlalchemy import Column, String,  Integer

from API.Services.databaseContext import Base

class Launcher(Base):
    __tablename__ = 'Launcher'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(255))

    def __init__(self,
                 name: String):
        self.id = None
        self.name = name

    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name
        }



