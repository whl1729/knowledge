# Go 使用笔记

- 让结构体的字段对外部可见，但不会被 JSON 编解码

  ```go
  type MyStruct struct {
    MyField string `json:"-"`
  }
  ```
