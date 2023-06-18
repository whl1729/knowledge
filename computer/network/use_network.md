# 网络使用笔记

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
