from sqlalchemy import Column, String, Integer, DateTime, Boolean, SMALLINT, BigInteger
from sqlalchemy.orm import declarative_base
from typing import Dict

Base = declarative_base()
class ChatModel(Base):
    __tablename__ = 'sqlite_sequence'
    name = Column(String(255), primary_key=True)
    seq = Column(Integer)
    
    def build(self, dict: Dict):
        for key, value in dict.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self