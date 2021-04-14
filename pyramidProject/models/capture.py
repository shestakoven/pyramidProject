from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,

)

from .meta import Base


class Capture(Base):
    __tablename__ = 'captures'
    id = Column(Integer, primary_key=True)
    path = Column(Text)
    created_at = Column(Text)
    camera = Column(Text)


Index('index_id', Capture.id, unique=True, mysql_length=255)
