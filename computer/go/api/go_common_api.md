# Go 常用 API

## 字符串

参考 [go standard library: strings][1]

```go
// strings
func Contains(s, substr string) bool
func Index(s, substr string) int
func Join(elems []string, sep string) string
func Repeat(s string, count int) string
func Replace(s, old, new string, n int) string
func ReplaceAll(s, old, new string) string
func ToLower(s string) string
func ToUpper(s string) string
func TrimPrefix(s, prefix string) string
func TrimSpace(s string) string
func TrimSuffix(s, suffix string) string
```

## HTTP

- [POST multipart/form-data][2]

  [1]: https://pkg.go.dev/strings
  [2]: https://stackoverflow.com/a/20397167
