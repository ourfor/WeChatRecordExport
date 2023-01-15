from core.database.DB import DB
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import Session

class MysqlDatabase(DB):
   def connect(self, host: str, username: str, password: str, database: str = "wechatdb", port: int = 3306):
        if self.engine is not None:
            return self.engine
        engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")
        self.engine = engine
        self.session = Session(engine)
        return engine