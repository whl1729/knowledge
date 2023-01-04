# npm 使用笔记

## 查看 node.js 版本 与 ECMAScript 版本的对应关系

- 参考网站：[node.green][6]
  - The website node.green provides an excellent overview over supported ECMAScript features in various versions of Node.js,
    based on kangax's compat-table.
  - 往下拉即可看到不同 ECMAScript 版本被 node.js 的支持情况

## 安装 npm

### npm 设置淘宝镜像

```sh
npm config set registry https://registry.npm.taobao.org
```

### 解决 npm 全局安装没有权限的问题

使用`npm install -g`全局安装 package 时，可能报以下错误：

```sh
Error: EACCES: permission denied, access '/usr/local/lib'
```

可以参考 [npm 官方文档「Manually change npm's default directory」][4] 来解决：

- 为 npm 创建全局安装目录：`mkdir ~/.npm-global`
- 配置 npm 使用该目录：`npm config set prefix ~/.npm-global`
- 在 `~/.profile` （或`~/.bashrc`）中添加该路径到环境变量 PATH：`export PATH=~/.npm-global/bin:$PATH`
- 使上一步的配置立即生效：`source ~/.profile`

### 使用 nvm 安装 node 和 npm

- 根据[nodejs 安装页面的说明][1]，推荐使用 [nvm][2] 来安装 node 和 npm。
- 安装 nvm：下载[nvm 安装脚本][3] 并运行。
- 使用 nvm 安装 node：

  ```sh
  export NVM_NODEJS_ORG_MIRROR=http://npm.taobao.org/mirrors/node/
  nvm install node
  ```

- 如果 nvm 安装 node 很慢，可以手动下载 node 安装包，将其解压到 `~/.nvm/versions/node/` 目录的指定版本目录下，
  再执行 `nvm use` 即可。

## npm 语义化版本号 （SemVer）

- [Semantic Versioning using npm][5]

- 理解 `^` 和 `~` 这两个符号的含义
  - `^`: It will only do updates that do not change the leftmost non-zero number
    i.e there can be changes in minor version or patch version but not in major version.
    If you write ^13.1.0, when running npm update, it can update to 13.2.0, 13.3.0 even 13.3.1, 13.3.2 and so on, but not to 14.0.0 or above.
  - `~`: if you write ~0.13.0 when running npm update it can update to patch releases: 0.13.1 is ok, but 0.14.0 is not.

  [1]: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
  [2]: https://github.com/nvm-sh/nvm
  [3]: https://github.com/nvm-sh/nvm/blob/v0.39.1/install.sh
  [4]: https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally
  [5]: https://nodejs.dev/learn/semantic-versioning-using-npm
  [6]: https://node.green/
