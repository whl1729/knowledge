# MongoDB 使用笔记

## 查询数据库

- Mongosh 筛选数组长度

    ```sh
    db.testResult.find({tasks: {$size: 2}})
    ```

- Mongosh 只显示数组中特定位置的元素的特定字段

    ```sh
    db.testResult.find({}, {"tasks": {$arrayElemAt: ["$tasks.data", 5]}})
    ```

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

调整方法：可以修改 MongoDB 的配置文件或修改 mongod 命令选项。

- [修改 mongod 命令选项][2]
  - `--wiredTigerCacheSizeGB <float>`
  - Values can range from 0.25 GB to 10000 GB
  - Defines the maximum size of the internal cache that WiredTiger uses for all data. The memory consumed by an index build (see maxIndexBuildMemoryUsageMegabytes) is separate from the WiredTiger cache memory.

- [修改 MongoDB 配置文件][3]
  - 修改 `/etc/mongod.conf` 的 `storage.wiredTiger.engineConfig.cacheSizeG` 参数，取值范围为 0.25 ~ 10000.

  [1]: https://www.mongodb.com/docs/manual/core/wiredtiger/
  [2]: https://www.mongodb.com/docs/manual/reference/program/mongod/#std-option-mongod.--wiredTigerCacheSizeGB
  [3]: https://www.mongodb.com/docs/manual/reference/configuration-options/#mongodb-setting-storage.wiredTiger.engineConfig.cacheSizeGB
