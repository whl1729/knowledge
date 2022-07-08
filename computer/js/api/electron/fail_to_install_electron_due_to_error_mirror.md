# 由于镜像设置有误导致 electron 安装失败

## 问题描述

- 在 Ubuntu 20.04 和 node v14.17.3 环境下，执行 `npm i -D electron` 失败，报错如下所示。

  ```sh
  along:~$ npm i -D electron

  > electron@19.0.7 postinstall /home/along/src/learn-electron/my-electron-app/node_modules/electron
  > node install.js

  Error: Generated checksum for "electron-v19.0.7-linux-x64.zip" did not match expected checksum.
      at Hash.<anonymous> (/home/along/src/learn-electron/my-electron-app/node_modules/sumchecker/index.js:133:20)
      at Hash.emit (events.js:375:28)
      at emitReadable_ (internal/streams/readable.js:550:12)
      at onEofChunk (internal/streams/readable.js:528:5)
      at readableAddChunk (internal/streams/readable.js:245:5)
      at Hash.Readable.push (internal/streams/readable.js:204:10)
      at Hash.Transform.push (internal/streams/transform.js:166:32)
      at done (internal/streams/transform.js:234:17)
      at internal/streams/transform.js:148:7
      at Hash._flush (internal/crypto/hash.js:71:3)
  npm WARN my-electron-app@1.0.0 No repository field.

  npm ERR! code ELIFECYCLE
  npm ERR! errno 1
  npm ERR! electron@19.0.7 postinstall: `node install.js`
  npm ERR! Exit status 1
  npm ERR!
  npm ERR! Failed at the electron@19.0.7 postinstall script.
  npm ERR! This is probably not a problem with npm. There is likely additional logging output above.

  npm ERR! A complete log of this run can be found in:
  npm ERR!     /home/along/.npm/_logs/2022-07-05T03_30_36_254Z-debug.log
  ```

- 同样环境下，执行`npm i -D electron@10.0.0`，同样失败，但报错信息不太一样。

  ```sh
  along:~/src/learn-electron/my-electron-app$ npm i -D electron@10.0.0

  > electron@10.0.0 postinstall /home/along/src/learn-electron/my-electron-app/node_modules/electron
  > node install.js

  Error: Could not parse checksum file at line 1: <!DOCTYPE html>
      at ChecksumValidator.parseChecksumFile (/home/along/src/learn-electron/my-electron-app/node_modules/sumchecker/index.js:83:15)
      at ChecksumValidator.validate (/home/along/src/learn-electron/my-electron-app/node_modules/sumchecker/index.js:106:10)
      at async /home/along/src/learn-electron/my-electron-app/node_modules/@electron/get/dist/cjs/index.js:110:21
      at async useAndRemoveDirectory (/home/along/src/learn-electron/my-electron-app/node_modules/@electron/get/dist/cjs/utils.js:10:18)
      at async /home/along/src/learn-electron/my-electron-app/node_modules/@electron/get/dist/cjs/index.js:75:13
      at async useAndRemoveDirectory (/home/along/src/learn-electron/my-electron-app/node_modules/@electron/get/dist/cjs/utils.js:10:18)
      at async downloadArtifact (/home/along/src/learn-electron/my-electron-app/node_modules/@electron/get/dist/cjs/index.js:65:12)
  npm WARN my-electron-app@1.0.0 No description
  npm WARN my-electron-app@1.0.0 No repository field.

  npm ERR! code ELIFECYCLE
  npm ERR! errno 1
  npm ERR! electron@10.0.0 postinstall: `node install.js`
  npm ERR! Exit status 1
  npm ERR!
  npm ERR! Failed at the electron@10.0.0 postinstall script.
  npm ERR! This is probably not a problem with npm. There is likely additional logging output above.

  npm ERR! A complete log of this run can be found in:
  npm ERR!     /home/along/.npm/_logs/2022-07-05T09_54_25_748Z-debug.log
  ```

- 同样环境下，执行`npm i -D electron@8.0.0`，最终显示成功，但其实也有跟安装 10.0.0 时一样的错误（导致 electron 没有完整安装），只不过被忽略掉了。

  ```sh
  along:~/src/learn-electron/my-electron-app$ npm i -D electron@8.0.0

  > electron@8.0.0 postinstall /home/along/src/learn-electron/my-electron-app/node_modules/electron
  > node install.js

  (node:210739) UnhandledPromiseRejectionWarning: Error: Could not parse checksum file at line 1: <!DOCTYPE html>
      at ChecksumValidator.parseChecksumFile (/home/along/src/learn-electron/my-electron-app/node_modules/sumchecker/index.js:83:15)
      at ChecksumValidator.validate (/home/along/src/learn-electron/my-electron-app/node_modules/sumchecker/index.js:106:10)
      at async /home/along/src/learn-electron/my-electron-app/node_modules/@electron/get/dist/cjs/index.js:110:21
      at async useAndRemoveDirectory (/home/along/src/learn-electron/my-electron-app/node_modules/@electron/get/dist/cjs/utils.js:10:18)
      at async /home/along/src/learn-electron/my-electron-app/node_modules/@electron/get/dist/cjs/index.js:75:13
      at async useAndRemoveDirectory (/home/along/src/learn-electron/my-electron-app/node_modules/@electron/get/dist/cjs/utils.js:10:18)
      at async downloadArtifact (/home/along/src/learn-electron/my-electron-app/node_modules/@electron/get/dist/cjs/index.js:65:12)
  (Use `node --trace-warnings ...` to show where the warning was created)
  (node:210739) UnhandledPromiseRejectionWarning: Unhandled promise rejection.
  This error originated either by throwing inside of an async function without a catch block, or by rejecting a promise which was not handled with .catch().
  To terminate the node process on unhandled promise rejection, use the CLI flag `--unhandled-rejections=strict`
  (see https://nodejs.org/api/cli.html#cli_unhandled_rejections_mode). (rejection id: 1)
  (node:210739) [DEP0018] DeprecationWarning: Unhandled promise rejections are deprecated.
  In the future, promise rejections that are not handled will terminate the Node.js process with a non-zero exit code.
  npm WARN my-electron-app@1.0.0 No description
  npm WARN my-electron-app@1.0.0 No repository field.

  + electron@8.0.0
  added 91 packages from 93 contributors in 5.49s

  9 packages are looking for funding
    run `npm fund` for details
  ```

## 定位过程

- 谷歌搜索报错信息，有人说需要删除以前缓存的校验和文件。

- 查看 `~/.cache/electron` 及其子目录，发现确实存在 `SHASUMS256.txt` 文件。

  ```sh
  along:~$ ls ~/.cache/electron/f6139e9727b66e3d3b8e9e2ac8a775e9381bda182d92ed1137ad233ae1c4003c/SHASUMS256.txt
  ```

- 删除上述文件，重新运行 `npm i -D electron`，但依然报同样的错误。

- 百般尝试后，发现执行如下命令来安装可以成功：

  ```js
  ELECTRON_MIRROR="https://npm.taobao.org/mirrors/electron/" npm i -D electron@10.0.0
  ```

- 接下来就很快发现是 electron 镜像路径没配置正确导致的问题，我原先配置的 electron 镜像路径如下所示：
  - 之前访问`https://npm.taobao.org/`，会重定向到`https://npmmirror.com/`，并且后者提示「原淘宝 npm 域名即将停止解析」。
  - 于是我就修改 electron 镜像路径：本来 npmmirror 主页给出的 electron 镜像路径为 `https://npmmirror.com/mirrors/electron/`，
    但我没使用这个路径，使用的是点击此路径后在网址栏显示的路径（如下所示）。

  ```js
  electron_mirror = "https://registry.npmmirror.com/binary.html?path=electron/"
  ```

- 这样配置路径会导致什么问题呢？查看`node_modules/electron/install.js`及相关文件，发现：
  - 安装 electron 镜像时，会下载一个校验和文件，该文件放在对应版本的 electron 目录下，
    下载地址按以下方式拼接得到的： `${electron_mirror}/${electron_version}/SHASUMS256.txt`
  - 按照我配置的 electron_mirror，会导致无法下载到正确的 SHASUMS256.txt，实际上下载的是 electron 镜像主页（一个 html 文件）
  - 因此，校验 SHASUMS256.txt 时会发现其格式不正确，从而报错。

## 经验教训

- 配置镜像地址时应该使用官方提供的网址，不要自行制作。

- 定位 node.js 问题有个好处：源码就放在 node_modules 目录下，可以随便加调试打印。也不用备份，反正重新安装又能生成原始文件。

- 之前一直以为是 electron 与 node 版本不匹配导致的问题，还因此埋怨 electron 太不好用。
  可见，如果对问题浅尝辄止，不能寻根问底，往往会带来误解，得出错误的结论。
