# Go 语言工具链

## 项目初始化

- 项目初始化流程
  - 创建项目目录
  - 在项目根目录下初始化 `go.mod` 文件

  ```bash
  mkdir hello
  cd hello

  # 如果你不打算发布模块，那模块的地址可以任意填
  go mod init example/hello

  # 如果你要发布模块，那模块的地址必须能够被 Go 工具访问
  go mod init github.com/hello
  ```

## 包管理

- 查看第三方库
  - 访问[Go 官方开发包网站][1]，搜索你想要的包
  - 包的文档的 index 章节给出了所有函数的原型
  - 包的文档的 functions 章节给出了所有函数的详细描述

- 使用第三方库
  - 找到库的地址，在代码中通过 import 语句将其导入
  - goimports 工具可以为代码自动添加一些漏写的常用的库
  - `go mod tidy` 可以安装缺少的模块、删除多余的模块
    （伍注：类似 js 的 `npm install` 或 python 的 `pip install`）
  - 几种高级 import 语句

  ```go
  // Import declaration          Local name of Sin

  import   "lib/math"         math.Sin
  import m "lib/math"         m.Sin
  import . "lib/math"         Sin

  // To import a package solely for its side-effects (initialization),
  // use the blank identifier as explicit package name:
  import _ "lib/math"
  ```

- 安装第三方库
  - `go get rsc.io/quote`

- 使用本地模块
  - 在代码中 import 本地模块时，填写本地模块的真实路径（亦即本地模块的 go.mod 配置的路径）
  - 执行 `go mod edit -replace example.com/greetings=../greetings`，替换本地模块的路径为文件夹相对路径
  - 执行 `go mod tidy` 同步本地模块的依赖

- 配置国内镜像源

  ```bash
  # 启用 Go Modules 功能（Linux 系统）
  go env -w GO111MODULE=on

  # 配置 GOPROXY 环境变量，以下三选一

  # 1. 七牛 CDN
  go env -w  GOPROXY=https://goproxy.cn,direct

  # 2. 阿里云
  go env -w GOPROXY=https://mirrors.aliyun.com/goproxy/,direct

  # 3. 官方
  go env -w  GOPROXY=https://goproxy.io,direct
  ```

  ```sh
  # 启用 Go Modules 功能（Windows 系统）
  $env:GO111MODULE="on"

  # 配置 GOPROXY 环境变量，以下三选一

  # 1. 七牛 CDN
  $env:GOPROXY="https://goproxy.cn,direct"

  # 2. 阿里云
  $env:GOPROXY="https://mirrors.aliyun.com/goproxy/,direct"

  # 3. 官方
  $env:GOPROXY="https://goproxy.io,direct"
  ```

  [1]: https://pkg.go.dev/
