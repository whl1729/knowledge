# Go 使用笔记

- JSON 数据反序列化为 `interface{}` 时，会将整型数字保存为 float64 形式
  - [json Unmarshal 官方文档][1]
  - [JSON decoded value is treated as float64 instead of int][2]

  ```markdown
  To unmarshal JSON into an interface value, Unmarshal stores one of these in the interface value:

  - bool, for JSON booleans
  - float64, for JSON numbers
  - string, for JSON strings
  - []interface{}, for JSON arrays
  - map[string]interface{}, for JSON objects
  - nil for JSON null
  ```

- 数字的默认类型为 int，在类型判断时需要注意。

  ```go
  mt.Println(reflect.TypeOf(7))
  // Output: int
  ```

- 让结构体的字段对外部可见，但不会被 JSON 编解码

  ```go
  type MyStruct struct {
    MyField string `json:"-"`
  }
  ```

  [1]: https://pkg.go.dev/encoding/json#Unmarshal
  [2]: https://stackoverflow.com/questions/55436628/json-decoded-value-is-treated-as-float64-instead-of-int
