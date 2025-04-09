from sqlalchemy import Column, String
import hashlib
import secrets
import base64

from API.Services.databaseContext import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(String(255), primary_key=True, index=True)
    fName = Column(String(30))
    lName = Column(String(100))
    email = Column(String(255), unique=True, nullable=False)
    passwordHash = Column(String(255), nullable=False)

    def __init__(self, fName, lName, email, passwordHash):
        self.id = self._generate_new_uid()
        self.fName = fName
        self.lName = lName
        self.email = email
        self.passwordHash = passwordHash

    def to_dict(self):
        return {
            "id": self.id,
            "fName": self.fName,
            "lName": self.lName,
            "email": self.email,
            "password_hash": self.passwordHash,
        }

    def _generate_new_uid(self):
        token_bytes = secrets.token_bytes(18)
        new_id = base64.urlsafe_b64encode(token_bytes).rstrip(b'=')
        return hashlib.sha256(new_id).digest().hex()