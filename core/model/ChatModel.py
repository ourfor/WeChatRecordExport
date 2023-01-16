from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata
class ChatModel(Base):
    __tablename__ = 'sqlite_sequence'
    metadata
    name = Column(NullType, primary_key=True)
    seq = Column(NullType)