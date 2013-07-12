from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey
)
from sqlalchemy.orm import relationship

from .meta import Base


class Collaborator(Base):
    __tablename__ = 'collaborators'

    # Main Fields
    access = Column(String(50), default='edit')

    # Foreign Keys
    app_id = Column(Integer, ForeignKey('apps.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    # Relationships
    app = relationship('App', backref='collaborators')
    user = relationship('User', backref='collaborators')
