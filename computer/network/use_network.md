# 网络使用笔记

- 修复 Ubuntu 系统翻墙后仍无法访问 github 的问题
  - `ping github.com` 发现访问的 IP 为 `13.234.176.102`
  - 想起来之前为 github 配置了静态 IP，删除 `/etc/hosts` 的静态 IP 配置后，恢复正常

- Solve SSH error: `kex_exchange_identification: Connection closed by remote host`
  - 在深圳大学城图书馆，使用图书馆的无线网络，`git pull` github 仓库时报以上错误
  - 改用自己手机的热点，则可以正常 `git pull` github 仓库
  - 可能是图书馆网络设置了防火墙

- Python 环境中使用代理进行 HTTP 通信

  ```bash
  # correct
  export all_proxy="https://127.0.0.1:7890/"

  # ERROR: Could not install packages due to an OSError: Missing dependencies for SOCKS support.
  export http_proxy="sock5://127.0.0.1:7890/"
  ```
