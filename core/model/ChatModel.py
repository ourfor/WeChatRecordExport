from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata
class ChatModel(Base):
    __tablename__ = 'sqlite_sequence'
    metadata
    name = Column(String(255), primary_key=True)
    seq = Column(Integer)