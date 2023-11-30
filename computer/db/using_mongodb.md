# MongoDB 使用笔记

## Aggregation

- 通过 `$let` 来访问同一个 pipeline stage 中定义的变量

  ```go
  pipeline := []bson.M{
      {
          "$group": bson.M{
              "_id": "$product",
              "totalSalePrice": bson.M{"$sum": "$salePrice"},
              "totalSaleCount": bson.M{"$sum": "$saleCount"},
          },
      },
      {
          "$project": bson.M{
              "_id":             0,
              "product":         "$_id",
              "totalSalePrice":  1,
              "totalSaleCount":  1,
              "averagePrice": bson.M{
                  "$let": bson.M{
                      "vars": bson.M{
                          "totalSalePrice": "$totalSalePrice",
                          "totalSaleCount": "$totalSaleCount",
                      },
                      "in": bson.M{
                          "$divide": []interface{}{"$$totalSalePrice", "$$totalSaleCount"},
                      },
                  },
              },
          },
      },
  }
  ```

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
