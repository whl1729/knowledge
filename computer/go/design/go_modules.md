# Go 模块

## import local package

假设你的 Go 项目的目录结构如下：

```text
mymodule/
   |-- greetings/greetings.go
   |-- hello/hello.go
```

这里，greetings 目录定义了 `package greetings`，而 hello 目录定义了 `package main`,
如何在 `hello/hello.go` 文件中 import greetings 模块呢？

答案：import 路径为 「模块名 + 模块根目录到对应包的相对路径」。比如上述例子应该这样写：

```golang
import "mymodule/greetings"
```
