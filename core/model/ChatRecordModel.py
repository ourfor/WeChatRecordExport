# coding: utf-8
from sqlalchemy import Column, Index, Integer, BigInteger, LargeBinary, Text, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class ChatChatRecordModel(Base):
    __abstract__ = True
    mesAutoID = Column(Integer, primary_key=True)
    mesSvrID = Column(Integer, index=True)
    msgCreateTime = Column(Integer)
    msgSeq = Column(Integer)
    deletionType = Column(Integer)
    _packed_MessageDeletion = Column(LargeBinary)

class ChatRecordModel(Base):
    __abstract__ = True
    mesLocalID = Column(Integer, primary_key=True)
    mesSvrID = Column(Integer, index=True)
    msgCreateTime = Column(Integer, index=True)
    msgContent = Column(Text)
    msgStatus = Column(Integer)
    msgImgStatus = Column(Integer)
    messageType = Column(Integer)
    mesDes = Column(Integer)
    msgSource = Column(Text)
    IntRes1 = Column(Integer)
    IntRes2 = Column(Integer)
    StrRes1 = Column(Text)
    StrRes2 = Column(Text)
    msgVoiceText = Column(Text)
    msgSeq = Column(Integer)
    CompressContent = Column(LargeBinary)
    ConBlob = Column(LargeBinary)

def ChatRecordModelForTableName(tableName: str) -> ChatRecordModel:
    className = f"{tableName}Class"
    Model = type(className, (ChatRecordModel,), {
        "__tablename__": tableName,
        # "__table_args__": (
        #     Index(f"{tableName}_msgStatus_mesDes", 'msgStatus', 'mesDes'),
        # )
    })
    return Model

def ChatChatRecordModelForTableName(tableName: str) -> ChatChatRecordModel:
    className = f"{tableName}Class"
    Model = type(className, (ChatRecordModel,), {
        "__tablename__": tableName
    })
    return Model


# mobile
class ChatExtMobileModel(Base):
    __abstract__ = True
    ConIntRes1 = Column(Integer, server_default=text("0"))
    ConIntRes2 = Column(Integer, server_default=text("0"))
    ConIntRes3 = Column(Integer, server_default=text("0"))
    ConStrRes1 = Column(Text)
    ConStrRes2 = Column(Text)
    ConStrRes3 = Column(Text)
    MesLocalID = Column(Integer, primary_key=True)
    msgFlag = Column(Integer, server_default=text("0"))
    MsgIdentify = Column(Text, index=True)
    MsgSource = Column(Text)

class ChatRecordMobileModel(Base):
    __abstract__ = True
    CreateTime = Column(Integer, index=True, server_default=text("0"))
    Des = Column(Integer)
    ImgStatus = Column(Integer, server_default=text("0"))
    MesLocalID = Column(Integer, primary_key=True)
    Message = Column(Text)
    MesSvrID = Column(BigInteger, index=True, server_default=text("0"))
    Status = Column(Integer, index=True, server_default=text("0"))
    TableVer = Column(Integer, server_default=text("1"))
    Type = Column(Integer)

class ChatHelloMobileModel(Base):
    __abstract__ = True
    ConIntRes1 = Column(Integer, server_default=text("0"))
    ConIntRes2 = Column(Integer, server_default=text("0"))
    ConIntRes3 = Column(Integer, server_default=text("0"))
    ConStrRes1 = Column(Text)
    ConStrRes2 = Column(Text)
    ConStrRes3 = Column(Text)
    CreateTime = Column(Integer, index=True, server_default=text("0"))
    Des = Column(Integer)
    ImgStatus = Column(Integer, server_default=text("0"))
    MesLocalID = Column(Integer, primary_key=True)
    Message = Column(Text)
    MesSvrID = Column(Integer, server_default=text("0"))
    OpCode = Column(Integer, server_default=text("0"))
    Status = Column(Integer, index=True, server_default=text("0"))
    TableVer = Column(Integer, server_default=text("1"))
    Type = Column(Integer)
    UsrName = Column(Text, index=True)

def ChatRecordMobileModelForTableName(tableName: str) -> ChatRecordMobileModel:
    className = f"{tableName}Class"
    Model = type(className, (ChatRecordMobileModel,), {
        "__tablename__": tableName,
        # "__table_args__": (
        #     Index(f"{tableName}_index6", 'Status', 'Des', 'Type', 'ImgStatus'),
        # )
    })
    return Model

def ChatExtMobileModelForTableName(tableName: str) -> ChatExtMobileModel:
    className = f"{tableName}Class"
    Model = type(className, (ChatExtMobileModel,), {
        "__tablename__": tableName
    })
    return Model

def ChatHelloMobileModelForTableName(tableName: str) -> ChatHelloMobileModel:
    className = f"{tableName}Class"
    Model = type(className, (ChatHelloMobileModel,), {
        "__tablename__": tableName
    })
    return Model