from core.database.DB import DB
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session

class SqliteDatabase(DB):
    def connect(self, dbPath: str, password: str):
        if self.engine is not None:
            return self.engine
        uri = f"sqlite+pysqlcipher://:{password}@/{dbPath}"
        try:
            print(f"database path: {dbPath}")
            engine = create_engine(uri)
            self.engine = engine
            self.session = Session(engine)
        except Exception:
            print(f"passowrd: {password}")
        return engine