# Go 语言错误处理

## 标准库提供的错误处理包

- 功能
  - 保存和打印错误信息
  - 判断错误类型
  - 同一类型的错误之间的赋值
  - 错误信息封装和解包。（封装时需要使用 `fmt.Errorf`，稍嫌麻烦）

- 不足
  - 没能保存发生错误时的上下文
  - 错误信息的封装不够方便
  - 不支持对错误码的封装

- [Standary library: errors][1]

- Interface

  ```go
  func As(err error, target any) bool
  func Is(err, target error) bool
  func New(text string) error
  func Unwrap(err error) error
  ```

## `github.com/pkg/erros`

- 相比标准库增加的功能
  - 支持错误信息多层封装
  - 支持获取多层封装的错误信息中最内层的信息
  - 支持获取调用栈

- Interface

  ```go
  func As(err error, target interface{}) bool
  func Cause(err error) error
  func Errorf(format string, args ...interface{}) error
  func Is(err, target error) bool
  func New(message string) error
  func Unwrap(err error) error
  func WithMessage(err error, message string) error
  func WithMessagef(err error, format string, args ...interface{}) error
  func WithStack(err error) error
  func Wrap(err error, message string) error
  func Wrapf(err error, format string, args ...interface{}) error
  type Frame
  func (f Frame) Format(s fmt.State, verb rune)
  func (f Frame) MarshalText() ([]byte, error)
  type StackTrace
  func (st StackTrace) Format(s fmt.State, verb rune)
  ```

  [1]: https://pkg.go.dev/errors
