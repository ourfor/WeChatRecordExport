生成macOS微信数据库Model

```bash
 export password="x'AABBCCDD'"
 export dbPath=/Users/ourfor/Tmp/WeChat/msg_0.db
 cd core/model
 sqlacodegen "sqlite+pysqlcipher://:${password}@/${dbPath}" --outfile=WeChatModel.py
 ```

生成iOS微信数据库Model
```bash
export dbPath=/Users/ourfor/Tmp/WeChatMobile/com.tencent.xin/Documents/665a137ec457899aab4be1a151fa5e1d/DB/message_1.sqlite
sqlacodegen "sqlite:///${dbPath}" --outfile=WeChatModel.py
```