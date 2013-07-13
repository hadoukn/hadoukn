from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey
)
from sqlalchemy.orm import relationship
from .meta import Base
from .behaviors.createable import Createable


class App(Createable, Base):
    __tablename__ = 'apps'

    # Main Fields
    name = Column(String(100))

    # Foreign Keys
    founder_id = Column(Integer, ForeignKey('users.id'))

    # Relationships
    releases = relationship('Release', backref='app')

    def __json__(self, request):
        return {
            'id': self.id,
            'name': self.name,
            'found_id': self.founder_id
        }
