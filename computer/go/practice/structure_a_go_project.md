# Go 项目结构设计

## 各家观点整理

### [Christoph Berger][8]

- Go project layout best practices
  - Start small
  - Name your packages by their functionality
    - Avoid grab-bag package names like `util`, `models`, `controllers`, `helpers`, or similar.
  - Follow the (few) conventions
    - Known directory names
      - `internal/`
      - `testdata/`
      - `vendor/`
    - Do not use `src`

- Whether to use `pkg`
  - Pure library projects need no pkg directory.
  - Small projects that contain library packages and CLI tools require no pkg directory.
  - Large applications, might use a pkg directory, but there are consequences.
  - Consider splitting dual application/library projects
    - Packages that can exist in their own right and that are worth exposing to the public can be collected in one or more separate library projects.
    - Packages that serve the application but do not work well as stand-alone packages go into internal.
    - Packages that serve the application, and for which you want to reserve the right to apply breaking changes to their API, should live in the internal directory.

- CLI tools

  ```text
  compress/
  +-- main.go
    go.mod
    go.sum
  ```

  ```text
  compress/
  +-- main.go
    go.mod
    go.sum
    internal/
    +-- deflate/
        +-- deflate.go
  ```

- Pure library projects

  ```text
  compress/
  +-- compress.go
    go.mod
    go.sum
    encode/
    +-- encode.go
    decode/
    +-- decode.go
  ```

- CLI tools with public packages, and libraries with CLI tools

  ```text
  compress/
  +-- compress.go
    go.mod
    go.sum
    cmd/
    +-- compress/
        +-- main.go
  ```

- Interim result: Everything together

  ```text
  compress/
  +-- compress.go
    go.mod
    go.sum
    encode/
    +-- encode.go
    decode/
    +-- decode.go
    internal/
    +-- deflate/
        +-- deflate.go
    cmd/
    +-- compress/
        +-- main.go
  ```

## main.go 应该放在哪里？

- 放在项目根目录下
  - 优点：`go install` 更加方便、初学者容易找到入口
  - 缺点：不能支持多个应用

- 放在 `cmd/myapp/` 目录里
  - 优点：可以支持多个应用
  - 缺点：`go install` 不方便、初学者不容易找到入口

## 要不要有 internal 目录？

- Benjamin Cane
  - when dealing with in-app packages, I don't see a clear line between internal and external packages.
  - In the name of internal-only packages, I've seen many developers skip best practices because "no one else is going to use it...".

- Mark Wolfe
  - Personally I prefer to use this over internal, mainly as I like to keep things open for reuse in most of projects.

## 要不要有 pkg 目录？

## 参考资料

- [The one-and-only, must-have, eternal Go project layout][8]: 综合各家观点，首先推荐
_ [Eli Bendersky's Website: Simple Go project layout with modules][9]
- [Benjamin Cane: How to Structure a Go Command-Line Project][1]
- [Benjamin Cane: How to Structure a Golang Project][2]
- [Mark Wolfe's Blog: How do I Structure my Go Project?][3]
- [Organizing Go code][4]
- [Scott White: Go Project Structure][5]
- [Ben Johnson: Standard Package Layout][6]
- [Golang project structuring — Ben Johnson way][7]

  [1]: https://medium.com/swlh/how-to-structure-a-go-command-line-project-788c318a1d8c
  [2]: https://madflojo.medium.com/how-to-structure-a-golang-project-aad7095d70a
  [3]: https://www.wolfe.id.au/2020/03/10/how-do-i-structure-my-go-project/
  [4]: https://go.dev/talks/2014/organizeio.slide#9
  [5]: https://levelup.gitconnected.com/go-project-structure-5157f458c520
  [6]: https://www.gobeyond.dev/standard-package-layout/
  [7]: https://medium.com/sellerapp/golang-project-structuring-ben-johnson-way-2a11035f94bc
  [8]: https://appliedgo.com/blog/go-project-layout
  [9]: https://eli.thegreenplace.net/2019/simple-go-project-layout-with-modules/
