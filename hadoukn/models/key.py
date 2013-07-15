from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)
from .meta import Base
from .behaviors.createable import Createable
from hadoukn.util import print_time


class Key(Base, Createable):
    __tablename__ = 'keys'

    # Main Fields
    key_type = Column(String(10))
    key_key = Column(String(1000))
    key_comment = Column(String(100))

    # Foreign Keys
    user_id = Column(Integer, ForeignKey('users.id'))

    @classmethod
    def by_key_key(cls, db, key_key):
        return db.query(cls).filter_by(key_key=key_key).first()

    def __json__(self, request):
        return {
            'id': self.id,
            'created': print_time(self.created),
            'key_type': self.key_type,
            'key_key': self.key_key,
            'key_comment': self.key_comment,
            'user_id': self.user_id
        }
