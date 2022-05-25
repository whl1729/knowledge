# 《Go 语言项目开发实战》分析笔记

## 第17章 API 文档：如何生成 Swagger API 文档？

### Q1：这一章的内容属于哪一类别？

计算机/软件工程

### Q2：这一章的内容是什么？

### Q3：这一章的大纲是什么？

- Swagger 介绍
- Swagger 和 OpenAPI 的区别
- 用 go-swagger 来生成 Swagger API 文档
  - 安装 Swagger 工具
  - swagger 命令行工具介绍
- 如何使用 swagger 命令生成 Swagger 文档？
  - 解析注释生成 Swagger 文档
  - go-swagger 其他常用功能介绍
- IAM Swagger 文档
- 总结

### Q4：作者想要解决什么问题？

### Q5：这一章的关键词是什么？

### Q6：这一章的关键句是什么？

#### Swagger 介绍

- Swagger 是一套围绕 OpenAPI 规范构建的开源工具，可以设计、构建、编写和使用 REST API。

- Swagger 包含很多工具，其中主要的 Swagger 工具包括：
  - [Swagger 编辑器][1]：基于浏览器的编辑器，可以在其中编写 OpenAPI 规范，并实时预览 API 文档。
  - Swagger UI：将 OpenAPI 规范呈现为交互式 API 文档，并可以在浏览器中尝试 API 调用。
  - Swagger Codegen：根据 OpenAPI 规范，生成服务器存根和客户端代码库，目前已涵盖了 40 多种语言。

#### Swagger 和 OpenAPI 的区别

- OpenAPI 是一个 API 规范，Swagger 则是实现规范的工具。

- OpenAPI 规范规定了一个 API 必须包含的基本信息，包括：
  - 对 API 的描述，介绍 API 可以实现的功能。
  - 每个 API 上可用的路径（/users）和操作（GET /users，POST /users）。
  - 每个 API 的输入 / 返回的参数。
  - 验证方法。
  - 联系信息、许可证、使用条款和其他信息。

- 要编写 Swagger 文档，首先要会使用 [Swagger 文档编写语法][2]。

#### 用 go-swagger 来生成 Swagger API 文档

- 在 Go 项目开发中，我们可以通过下面两种方法来生成 Swagger API 文档：
  - 如果你熟悉 Swagger 语法的话，可以直接编写 JSON/YAML 格式的 Swagger 文档。
    建议选择 YAML 格式，因为它比 JSON 格式更简洁直观。
  - 通过工具生成 Swagger 文档，目前可以通过 [swag][3] 和 [go-swagger][4] 两个工具来生成。

- go-swagger vs swag
  - go-swagger 比 swag 功能更强大：go-swagger 提供了更灵活、更多的功能来描述我们的 API。
  - 使我们的代码更易读
    - 如果使用 swag，我们每一个 API 都需要有一个冗长的注释，有时候代码注释比代码还要长，
    - 如果使用 go-swagger，我们可以将代码和注释分开编写，
      一方面可以使我们的代码保持简洁，清晰易读，
      另一方面我们可以在另外一个包中，统一管理这些 Swagger API 文档定义。
  - 更好的社区支持
    - go-swagger 目前有非常多的 Github star 数，出现 Bug 的概率很小，并且处在一个频繁更新的活跃状态。

- go-swagger 的特性
  - 根据代码注释生成 Swagger API 文档
  - 根据 Swagger 定义文件生成服务端代码
  - 根据 Swagger 定义文件生成客户端代码
  - 校验 Swagger 定义文件是否正确
  - 启动一个 HTTP 服务器，使我们可以通过浏览器访问 API 文档。
  - 根据 Swagger 文档定义的参数生成 Go model 结构体定义。

- 安装 Swagger 工具
  - 直接到 github 仓库下载二进制文件即可

#### 如何使用 swagger 命令生成 Swagger 文档？

- [go-swagger 文档][5]

- 解析注释生成 Swagger 文档
  - `swagger generate` 命令会找到 main 函数，
  - 然后遍历所有源码文件，解析源码中与 Swagger 相关的注释，
  - 然后自动生成 swagger.json/swagger.yaml 文件。

- go-swagger 其他常用功能介绍

#### IAM Swagger 文档

#### 总结

### Q7：作者是怎么论述的？

### Q8：作者解决了什么问题？

### Q9：我有哪些疑问？

### Q10：这一章说得有道理吗？为什么？

### Q11: 这一章讨论的知识的本质是什么？

### Q12: 这一章讨论的知识的第一原则是什么？

### Q13：这一章讨论的知识的结构是怎样的？

### Q14：这一章讨论的知识为什么是这样的？为什么发展成这样？为什么需要它？

### Q15：有哪些相似的知识？它们之间的联系是什么？

### Q16：其他领域/学科有没有相关的知识？日常生活中有没有类似的现象？

### Q17: 这一章对我有哪些用处/帮助/启示？

### Q18: 我如何应用这一章的知识去解决问题？

  [1]: https://editor.swagger.io
  [2]: https://swagger.io/docs/specification/about/
  [3]: https://github.com/swaggo/swag
  [4]: https://github.com/go-swagger/go-swagger
  [5]: https://goswagger.io/
