from sqlalchemy import (
    Column,
    Index,
    Integer,
    String,
)

from .meta import Base


class Capture(Base):
    __tablename__ = 'captures'
    id = Column(Integer, primary_key=True)
    path = Column('path', String)
    created_at = Column('created at', String)
    camera = Column('camera', String)


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column('username', String, unique=True)
    password = Column('password', String)


Index('index_id', Capture.id, unique=True, mysql_length=255)
