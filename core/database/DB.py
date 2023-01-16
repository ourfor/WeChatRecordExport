from typing import List
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import select
from typing import Sequence, TypeVar

T = TypeVar('T')

class DB():
    engine = None
    session = None
    def createTable(self, Model):
        engine = self.engine
        if engine is None:
            engine = self.connect()
        Model.metadata.create_all(engine)
    
    def connect(self):
        pass

    def open(self):
        if self.session is None:
            engine = self.connect()
            self.session = Session(engine)
        return self.session

    def save(self, model):
        session = self.open()
        session.merge(model)
        session.commit()
    
    def saveAll(self, models):
        session = self.open()
        session.add_all(models)
        session.commit()
    
    def query(self, sql: str) -> List:
        session = self.session
        if session is None:
            return []
        return session.execute(sql).all()
    
    def find(self, modelType: T) -> Sequence[T]:
        session = self.session
        if session is None:
            return []
        table = modelType.__table__
        sql = select(modelType)
        return session.scalars(sql)
    
    def count(self, modelType: T)-> int:
        session = self.session
        if session is None:
            return 0
        count = session.query(modelType).count()
        return count
    
    def commit(self):
        session = self.session
        if session is not None:
            session.commit() 
    
    def close(self):
        session = self.session
        if session is not None:
            session.close()