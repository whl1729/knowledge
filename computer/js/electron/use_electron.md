# electron 使用笔记

## 安装 electron

- [由于镜像设置有误导致 electron 安装失败][1]

- 解决electron下载慢的问题（方法1：使用缓存）
  - 使用浏览器，前往 [国内淘宝镜像源][2] 下载你所需要的版本
  - 将下载的文件拷贝到以下路径：
    - Windows: `C:\Users\<user>\AppData\Local\electron\Cache`
    - Linux: `~/.cache/electron/[sha256_string]/`
  - Linux 系统的 electron 缓存路径的 sha256 值的计算（以 electron v8.5.5 为例）
    - `echo -n https://npmmirror.com/mirrors/electron/v8.5.5 | sha256sum`

- 解决electron下载慢的问题（方法2：设置国内镜像源）

  ```sh
  # 方式1：通过 npm 设置 electron 镜像源。（注意： electron_mirror 必须为小写形式，否则配置无效。）
  npm config set electron_mirror https://npm.taobao.org/mirrors/electron/

  # 方式2：在安装时直接通过环境变量设置 electron 镜像源。
  ELECTRON_MIRROR="https://npm.taobao.org/mirrors/electron/" npm install
  ```

  [1]: fail_to_install_electron_because_of_error_mirror.md
  [2]: https://npm.taobao.org/mirrors/electron/
