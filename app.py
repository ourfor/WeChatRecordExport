#!/usr/bin/env python3

from core.database.DB import DB
from core.database.SqliteDatabase import SqliteDatabase
from core.database.MysqlDatabase import MysqlDatabase
from core.model.ChatModel import ChatModel
from core.model.ChatRecordModel import ChatRecordModel, ChatRecordModelForTableName

import argparse
import os

def cmd():
    args = argparse.ArgumentParser(description = 'Personal Information ',epilog = 'Information end ')
    args.add_argument("-d",'--path', type = str, dest = "path",   help = u"Sqlite 数据库文件目录", default = 10)
    args.add_argument("-p",'--password', type = str, dest = "password",   help = u"Sqlite 数据库文件秘密", default = 10)
    args = args.parse_args()
    return args

def main():
    args = cmd()
    path = args.path
    password = args.password
    password = f"x'{password}'"
      
    if path is None:
        return
    
    # mysqlDB = MysqlDatabase()
    # mysqlDB.connect(
    #     host="db.com",
    #     username="test",
    #     password="Sql2022DB"
    # )
    # mysqlDB.createTable(ChatModel)
    for filename in os.listdir(path):
        fullPath = os.path.join(path, filename)
        if not os.path.isfile(fullPath):
            continue
        if not filename.endswith(".db") or not filename.startswith("msg"):
            continue
        sqliteDB = SqliteDatabase()
        sqliteDB.connect(fullPath, password)
        models = sqliteDB.find(ChatModel)
        # mysqlDB.saveAll(models)
        for model in models:
            tableName = model.name
            if tableName.startswith("Chat_Chat"):
                continue
            ChatRecordModelType = ChatRecordModelForTableName(tableName)
            records = sqliteDB.find(ChatRecordModelType)
            # mysqlDB.createTable(ChatRecordModelType)
            for record in records:
                print(record.msgCreateTime)   
            # mysqlDB.saveAll(records)
        sqliteDB.close()

    # mysqlDB.close()
    
if __name__ == "__main__":
    main()
    