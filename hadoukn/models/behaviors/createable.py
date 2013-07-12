from sqlalchemy import (
    Column,
    DateTime
)
from sqlalchemy.ext.declarative import declared_attr


class Createable(object):
    @declared_attr
    def created(cls):
        return Column(DateTime)
