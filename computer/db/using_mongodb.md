# MongoDB 使用笔记

## 查询数据库

- Mongosh select 部分字段

    ```sh
    db.testResult.find({"product": "D2H", "station": "PCBA测试"}, { product: 1, station: 1, deviceSN: 1, code: 1, startTime: 1})
    ```

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

## FAQs

### Q1: `An object representing an expression must have exactly one field`

使用 MongoDB 定义一个 pipeline 时，抛出以下错误：

```text
(Location15983) An object representing an expression must have exactly one field: { $year: { $dateFromString: { dateString: \"$startTime\", format: \"%Y-%m-%d %H:%M:%S\" } }, station: \"$station\" }"}
```

对应的代码如下：

```go
"_id": bson.M{
            "$year": bson.M{
                "$dateFromString": bson.M{"dateString": "$startTime", "format": "%Y-%m-%d %H:%M:%S"},
            },
            "station": "$station",
        },
```

修改后的代码如下：

```go
"_id": bson.M{
            "year": bson.M{
                groupID: bson.M{
                    "$dateFromString": bson.M{"dateString": "$startTime", "format": "%Y-%m-%d %H:%M:%S"},
                },
            },
            "station": "$station",
        },
```

### Q2: 为什么 MongoDB 使用那么多内存

根据[官方文档][1]，MongoDB 的内存使用策略如下：

> With WiredTiger, MongoDB utilizes both the WiredTiger internal cache and the filesystem cache.
>
> Starting in MongoDB 3.4, the default WiredTiger internal cache size is the larger of either:
>
> 50% of (RAM - 1 GB), or
>
> 256 MB.

  [1]: https://www.mongodb.com/docs/manual/core/wiredtiger/
