# MongoDB 使用笔记

## 备份和迁移数据库

```sh
# Step 1: Dump the source collection
mongodump --port sourcePort --db sourceDB --collection sourceCollection --out /path/to/dump_directory

# Step 2: Restore into the destination collection
mongorestore --port destPort --db destDB --collection destCollection /path/to/dump_directory/sourceDB/sourceCollection.bson

```

## 删除数据库

执行以下命令以删除 temp 数据库：

```sh
use temp
db.dropDatabase()
```
