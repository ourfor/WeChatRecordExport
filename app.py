#!/usr/bin/env python3

import copy
from core.database.DB import DB
from core.database.SqliteDatabase import SqliteDatabase
from core.database.MysqlDatabase import MysqlDatabase
from core.model.ChatModel import ChatModel
from core.model.ChatRecordModel import ChatRecordMobileModelForTableName, ChatRecordModel, ChatRecordModelForTableName

import argparse
import os
from tqdm import tqdm
import configparser
from typing import List, Dict

def config() -> Dict:
    parser = configparser.ConfigParser()
    parser.read("config.ini")
    return parser

def allDatabaseFilePath(path: str, isMobile: bool = False) -> List[str]:
    dbPaths = []
    suffix = ".sqlite" if isMobile else ".db"
    prefix = "message" if isMobile else "msg"
    for filename in os.listdir(path):
        fullPath = os.path.join(path, filename)
        if not os.path.isfile(fullPath):
            continue
        if not filename.endswith(suffix) or not filename.startswith(prefix):
            continue
        dbPaths.append(fullPath)
    return dbPaths

def cmd():
    args = argparse.ArgumentParser(description = 'Personal Information ',epilog = 'Information end ')
    args.add_argument("-d",'--path', type = str, dest = "path",   help = u"Sqlite 数据库文件目录", default = "")
    args.add_argument("-p",'--password', type = str, dest = "password",   help = u"Sqlite 数据库文件秘密", default = "")
    args = args.parse_args()
    return args

def main():
    args = cmd()
    path = args.path
    password = args.password
    print(password)
    if password != "":
        password = f"x'{password}'"
      
    if path == "":
        return
    
    mysqlDB = MysqlDatabase()
    conf = config()
    mysqlDB.connect(
        host=conf["MYSQL"]["host"],
        username=conf["MYSQL"]["username"],
        password=conf["MYSQL"]["password"],
        database=conf["MYSQL"]["database"],
        port=int(conf["MYSQL"]["port"])
    )
    mysqlDB.createTable(ChatModel)
    isMobile = True
    dbPaths = allDatabaseFilePath(path, isMobile)

    for dbPath in dbPaths:
        sqliteDB = SqliteDatabase()
        sqliteDB.connect(dbPath, password)
        models = sqliteDB.find(ChatModel)
        for model in models:
            tableName = model.name
            if tableName.startswith("Chat_Chat"):
                continue
            
            if isMobile:
                ChatRecordMobileModelType = ChatRecordMobileModelForTableName(tableName)
                records = sqliteDB.find(ChatRecordMobileModelType)
                mysqlDB.createTable(ChatRecordMobileModelType)
                size = sqliteDB.count(ChatRecordMobileModelType)
                print(f"⌛ 开始导出 {tableName} 📝 {size}条")
                with tqdm(total=size) as pbar:
                    completed = 0
                    failed = 0
                    for record in records:
                        pbar.set_description(f"⏰ {record.CreateTime}")
                        try:
                            mysqlDB.save(copy.copy(record))
                            completed = completed + 1
                        except Exception:
                            failed = failed + 1
                        finally:
                            pbar.update(1)
                    
                    print(f"👌 总共 {size} 条, 成功 {completed} 失败: {failed}")
            # else:
            #     ChatRecordModelType = ChatRecordModelForTableName(tableName)
            #     records = sqliteDB.find(ChatRecordModelType)
            #     # mysqlDB.createTable(ChatRecordModelType)
            #     for record in records:
            #         print(record.msgCreateTime)   
            #     # mysqlDB.saveAll(records)
        mysqlDB.saveAll(models)
        sqliteDB.close()
    # mysqlDB.close()
    
if __name__ == "__main__":
    main()
    