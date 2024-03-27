# vscode 使用指南

## 快捷键

- `Ctrl + \`: comment and uncomment code
- `F4`: next search result
- `Shift` + `F4`: previous search result

## FAQs

- [解决 vscode SSH 连接远端设备时一直卡在 Setting up SSH Host back: Downloading VS Code Server 的问题][1]
  - On server, get the commit id

  ```bash
  $ ls ~/.vscode-server/bin
  553cfb2c2205db5f15f3ee8395bbd5cf066d357d
  ```

  - Download tarball replacing $COMMIT_ID with the the commit number from the previous step.

  ```text
  https://update.code.visualstudio.com/commit:$COMMIT_ID/server-linux-x64/stable
  ```

  - Move tarball to `~/.vscode-server/bin/$COMMIT_ID/vscode-server-linux-x64.tar.gz`
  - Extract tarball in this directory

  ```bash
  cd ~/.vscode-server/bin/$COMMIT_ID
  tar -xvzf vscode-server-linux-x64.tar.gz --strip-components 1
  ```

- [vscode 自动激活 Python 虚拟环境][2]

  ```json
  "settings": {
    "python.terminal.activateEnvInCurrentTerminal": true,
    "python.defaultInterpreterPath": "~/venv/bin/python"
  }
  ```

  [1]: https://stackoverflow.com/a/56781109
  [2]: https://stackoverflow.com/a/66281531
