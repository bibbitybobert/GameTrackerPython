from sqlalchemy import Column, String, DateTime
from sqlalchemy.sql import func, text
import hashlib
import secrets
import base64

from API.Services.databaseContext import Base

class Session(Base):
    __tablename__ = 'session'

    id = Column(String(255), primary_key=True, index=True)
    userId = Column(String(255), nullable=False)
    expiresAt = Column(DateTime, nullable=False)

    def __init__(self, user_id):
        self.id = self._generate_new_id()
        self.userId = user_id
        self.expiresAt = func.now() + text("INTERVAL 1 DAY")

    def to_dict(self):
        return {
            "id": self.id,
            "userId": self.userId,
            "expiresAt": self.expiresAt,
        }

    def _generate_new_id(self):
        token_bytes = secrets.token_bytes(18)
        new_id = base64.urlsafe_b64encode(token_bytes).rstrip(b'=')
        return hashlib.sha256(new_id).digest().hex()

    def renew_time(self):
        self.expiresAt = self.expiresAt + text("INTERVAL 1 DAY")
        return self.expiresAt