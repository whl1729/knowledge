# Electron 使用笔记

- 设置镜像

  ```text
  electron_mirror=https://npmmirror.com/mirrors/electron/
  electron_builder_binaries_mirror=https://npmmirror.com/mirrors/electron_builder_binaries_mirror/
  ```

- `Uncaught ReferenceError: require is not defined` [解决方案][1]

  ```javascript
  win = new BrowserWindow({
      width: 300,
      height: 200,

      // The lines below solved the issue
      webPreferences: {
          nodeIntegration: true,
          contextIsolation: false
      }
  })
  ```

  [1]: https://stackoverflow.com/a/56342771
