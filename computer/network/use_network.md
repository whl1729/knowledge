# 网络使用笔记

- Python 环境中使用代理进行 HTTP 通信

  ```bash
  # correct
  export all_proxy="https://127.0.0.1:7890/"

  # ERROR: Could not install packages due to an OSError: Missing dependencies for SOCKS support.
  export http_proxy="sock5://127.0.0.1:7890/"
  ```
