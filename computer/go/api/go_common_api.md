# Go 常用 API

## 字符串

```go
// strings
func Contains(s, substr string) bool
func Index(s, substr string) int
func Join(elems []string, sep string) string
func ToLower(s string) string
func ToUpper(s string) string
func TrimPrefix(s, prefix string) string
func TrimSpace(s string) string
func TrimSuffix(s, suffix string) string
```

## HTTP

- [POST multipart/form-data][1]

  [1]: https://stackoverflow.com/a/20397167
