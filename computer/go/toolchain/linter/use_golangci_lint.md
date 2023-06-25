# golangci-lint 使用笔记

- 使用 golangci-lint 前必须配置环境变量 `GOPATH`，否则报以下错误：

  ```bash
  # go v1.17 环境下报错：
  ERRO Running error: context loading failed: failed to load packages:
  failed to load with go/packages: err: exit status 1: stderr: missing $GOPATH

  # go v1.18 环境下报错：
  ERRO Running error: context loading failed: no go files to analyze
  ```
