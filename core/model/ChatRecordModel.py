from sqlalchemy import Column, String, Integer, Text, BLOB
from sqlalchemy.orm import declarative_base
from typing import Dict

Base = declarative_base()
class ChatRecordModel(Base):
    __abstract__ = True
    mesLocalID	= Column(Integer, primary_key=True)		
    mesSvrID	= Column(Integer)		
    msgCreateTime	= Column(Integer)		
    msgContent	= Column(Text)		
    msgStatus	= Column(Integer)		
    msgImgStatus	= Column(Integer)		
    messageType	= Column(Integer)		
    mesDes	= Column(Integer)		
    msgSource	= Column(Text)		
    IntRes1	= Column(Integer)		
    IntRes2	= Column(Integer)		
    StrRes1	= Column(Text)		
    StrRes2	= Column(Text)		
    msgVoiceText	= Column(Text)		
    msgSeq	= Column(Integer)		
    CompressContent	= Column(BLOB)		
    ConBlob	= Column(BLOB)
    
    def build(self, dict: Dict):
        for key, value in dict.items():
            if hasattr(self, key):
                setattr(self, key, value)
        return self

def ChatRecordModelForTableName(tableName: str) -> ChatRecordModel:
    className = f"{tableName}Class"
    Model = type(className, (ChatRecordModel,), {
        '__tablename__': tableName
    })
    # class GenericModel(Base, tableName):
    #     __tablename__ = tableName
    #     __metaclass__ = tableName
    #     mesLocalID	= Column(Integer, primary_key=True)		
    #     mesSvrID	= Column(Integer)		
    #     msgCreateTime	= Column(Integer)		
    #     msgContent	= Column(Text)		
    #     msgStatus	= Column(Integer)		
    #     msgImgStatus	= Column(Integer)		
    #     messageType	= Column(Integer)		
    #     mesDes	= Column(Integer)		
    #     msgSource	= Column(Text)		
    #     IntRes1	= Column(Integer)		
    #     IntRes2	= Column(Integer)		
    #     StrRes1	= Column(Text)		
    #     StrRes2	= Column(Text)		
    #     msgVoiceText	= Column(Text)		
    #     msgSeq	= Column(Integer)		
    #     CompressContent	= Column(BLOB)		
    #     ConBlob	= Column(BLOB)
    return Model