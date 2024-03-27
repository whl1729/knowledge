# GORM 使用笔记

- 避免在 `Where` 和 `First` 函数中设置矛盾的过滤条件

  ```go
  // 以下查询语句将会报错，因为查找不到 id 同时为 1 和 2 的记录
	err := db.Where("id = ?", 1).First(&User{ID: 2}).Error
  ```
