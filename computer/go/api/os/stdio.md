# Go 标准输入/输出

## 基本 API

```go
// Output
func Printf(format string, a ...any) (n int, err error)
func Println(a ...any) (n int, err error)

// Input
func Scanf(format string, a ...any) (n int, err error)
func Sscanf(str string, format string, a ...any) (n int, err error)
func Fscanf(r io.Reader, format string, a ...any) (n int, err error)

// Others
func Sprintf(format string, a ...any) string
func Errorf(format string, a ...any) error
```

## [格式化输出字符串][1]

### General

```text
%v    the value in a default format
    when printing structs, the plus flag (%+v) adds field names
%#v    a Go-syntax representation of the value
%T    a Go-syntax representation of the type of the value
%%    a literal percent sign; consumes no value
```

The default format for `%v` is:

```text
bool:                    %t
int, int8 etc.:          %d
uint, uint8 etc.:        %d, %#x if printed with %#v
float32, complex64, etc: %g
string:                  %s
chan:                    %p
pointer:                 %p
```

For compound objects, the elements are printed using these rules, recursively, laid out like this:

```text
struct:             {field0 field1 ...}
array, slice:       [elem0 elem1 ...]
maps:               map[key1:value1 key2:value2 ...]
pointer to above:   &{}, &[], &map[]
```

> 伍注：
> 1. 对于 string 变量，`%v` 直接打印内容，`%#v` 则还会打印双引号。
> 2. 记忆方法：v 为 value 的首字母，T 为 Type 的首字母。

### Boolean

```text
%t    the word true or false
```

> 伍注：记忆方法：t 为 true 的首字母。

### Integer

```text
%b    base 2
%c    the character represented by the corresponding Unicode code point
%d    base 10
%o    base 8
%O    base 8 with 0o prefix
%q    a single-quoted character literal safely escaped with Go syntax.
%x    base 16, with lower-case letters for a-f
%X    base 16, with upper-case letters for A-F
%U    Unicode format: U+1234; same as "U+%04X"
```

> 记忆方法：
> 1. b 对应 binary，d 对应 decimal，o 对应 octal，x 对应 hexadecimal
> 2. q 打印的是一个单引号括起来的字符，对应的整数一般小于 256，否则大概率为乱码

### Floating-point and complex constituents

```text
%e    scientific notation, e.g. -1.234456e+78
%E    scientific notation, e.g. -1.234456E+78
%f    decimal point but no exponent, e.g. 123.456
%F    synonym for %f
%g    %e for large exponents, %f otherwise. Precision is discussed below.
%G    %E for large exponents, %F otherwise
```

Width is specified by an optional decimal number immediately preceding the verb.

```text
%f     default width, default precision
%9f    width 9, default precision
%.2f   default width, precision 2
%9.2f  width 9, precision 2
%9.f   width 9, precision 0
```

Either or both of the flags may be replaced with the character '*',
causing their values to be obtained from the next operand (preceding the one to format),
which must be of type int.

> 记忆方法：e 对应 exponent，f 对应 floatint-point，g 对应 global（全面的，大数目和小数目都考虑到）

### String

```text
%s    the uninterpreted bytes of the string or slice
%q    a double-quoted string safely escaped with Go syntax
```

### Slice of bytes

```text
%x    base 16, lower-case, two characters per byte
%X    base 16, upper-case, two characters per byte
%p    address of 0th element in base 16 notation, with leading 0x
```

### Pointer

```text
%p    base 16 notation, with leading 0x
```

### Format errors

If an invalid argument is given for a verb, such as providing a string to `%d`,
the generated string will contain a description of the problem.

## 格式化输入字符串

- 3 kinds of Scanning function
  - Scan, Scanf and Scanln read from os.Stdin
  - Fscan, Fscanf and Fscanln read from a specified io.Reader
  - Sscan, Sscanf and Sscanln read from an argument string

- Scanf, Fscanf, and Sscanf parse the arguments according to a format string, analogous to that of Printf.

- Format String
  - A character other than %, space, or newline in the format consumes exactly that input character, which must be present.
  - A newline with zero or more spaces before it in the format string
    consumes zero or more spaces in the input followed by a single newline or the end of the input.
  - A space following a newline in the format string consumes zero or more spaces in the input.
  - Otherwise, any run of one or more spaces in the format string consumes as many spaces as possible in the input.
    Unless the run of spaces in the format string appears adjacent to a newline,
    the run must consume at least one space from the input or find the end of the input.

> 伍注：普通字符消耗自身，换行符或空格消耗尽可能多的空格。只能记到这里。

- The verbs behave analogously to those of Printf.

- Input processed by verbs is implicitly space-delimited

- Width
  - Width is interpreted in the input text but there is no syntax for scanning with a precision (no %5.2f, just %5f).
  - If width is provided, it applies after leading spaces are trimmed and specifies the maximum number of runes to read to satisfy the verb.

  [1]: https://pkg.go.dev/fmt
