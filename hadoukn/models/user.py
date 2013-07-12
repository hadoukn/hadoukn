import os

from hashlib import sha1
from sqlalchemy import (
    String,
    Column
)
from sqlalchemy.orm import relationship
from hadoukn.models import Base


class User(Base):
    __tablename__ = 'users'

    username = Column(String(50))
    password = Column(String(80))
    api_key = Column(String(80))

    # Relationships
    apps = relationship('App', backref='user')
    keys = relationship('Key', backref='user')

    def __init__(self, username, password, **kwargs):
        self.username = username
        if password is not None:
            self._set_password(password)
        self._set_api_key()
        self.__dict__.update(kwargs)

    def _generate_salt(self):
        salt = sha1()
        salt.update(os.urandom(60))
        return salt

    def _set_password(self, password):
        hashed_password = password

        if isinstance(password, unicode):
            password_8bit = password.encode('UTF-8')
        else:
            password_8bit = password

        salt = self._generate_salt()
        hash = sha1()
        hash.update(password_8bit + salt.hexdigest())
        hashed_password = salt.hexdigest() + hash.hexdigest()

        if not isinstance(hashed_password, unicode):
            hashed_password = hashed_password.decode('UTF-8')

        self.password = hashed_password

    def _set_api_key(self):
        salt = self._generate_salt()
        hash = sha1()
        hash.update(self.username)

        api_key = salt.hexdigest() + hash.hexdigest()
        self.api_key = api_key

    def validate_password(self, password):
        hashed_pass = sha1()
        hashed_pass.update(password + self.password[:40])
        return self.password[40:] == hashed_pass.hexdigest()

    @classmethod
    def by_username(cls, db, username):
        return db.query(cls).filter_by(username=username).first()

    @classmethod
    def by_api_key(cls, db, api_key):
        return db.query(cls).filter_by(api_key=api_key).first()

    def __json__(self, request):
        return {
            'id': self.id,
            'username': self.username,
            'api_key': self.api_key
        }
