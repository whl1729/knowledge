# vscode 使用指南

## 快捷键

- `F4`: next search result
- `Shift` + `F4`: previous search result

## FAQs

- 解决 vscode SSH 连接远端设备时一直卡在 Setting up SSH Host back: Downloading VS Code Server 的问题
  - [手动下载 vscode-server 并解压到远端设备的指定目录中][1]

- [vscode 自动激活 Python 虚拟环境][2]

  ```json
  "settings": {
    "python.terminal.activateEnvInCurrentTerminal": true,
    "python.defaultInterpreterPath": "~/venv/bin/python"
  }
  ```

  [1]: https://stackoverflow.com/a/56781109
  [2]: https://stackoverflow.com/a/66281531
