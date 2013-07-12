from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey
)
from .meta import Base
from .behaviors.createable import Createable


class App(Createable, Base):
    __tablename__ = 'apps'

    # Main Fields
    name = Column(String(100))
    stack = Column(String(20), default='cedar')
    web_url = Column(String(100))
    git_url = Column(String(100))
    dynos = Column(Integer)
    workers = Column(Integer)
    slugsize = Column(Integer)
    reposize = Column(Integer)
    buildpack_provided_description = Column(String(50))
    status = Column(String(50))

    # Foreign Keys
    user_id = Column(Integer, ForeignKey('users.id'))

    def __json__(self, request):
        return {
            'id': self.id,
            'name': self.name,
            'stack': self.stack,
            'web_url': self.web_url,
            'git_url': self.git_url,
            'dynos': self.dynos,
            'workers': self.workers,
            'slugsize': self.slugsize,
            'reposize': self.reposize,
            'buildpack_provided_description': self.buildpack_provided_description,
            'status': self.status,
            'user_id': self.user_id
        }
