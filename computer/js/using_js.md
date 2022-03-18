# JavaScript 使用笔记

## 环境安装

### 解决 npm 全局安装没有权限的问题

使用`npm install -g`全局安装 package 时，可能报以下错误：

```
Error: EACCES: permission denied, access '/usr/local/lib'
```

可以参考 [npm 官方文档「Manually change npm's default directory」][4] 来解决：

- 为 npm 创建全局安装目录：`mkdir ~/.npm-global`
- 配置 npm 使用该目录：`npm config set prefix ~/.npm-global`
- 在 `~/.profile` （或`~/.bashrc`）中添加该路径到环境变量 PATH：`export PATH=~/.npm-global/bin:$PATH`
- 使上一步的配置立即生效：`source ~/.profile`

### 安装 node 和 npm

- 根据[nodejs 安装页面的说明][1]，推荐使用 [nvm][2] 来安装 node 和 npm。
- 安装 nvm：下载[nvm 安装脚本][3] 并运行。
- 使用 nvm 安装 node：

  ```sh
  export NVM_NODEJS_ORG_MIRROR=http://npm.taobao.org/mirrors/node
  nvm install node
  ```

  [1]: https://docs.npmjs.com/downloading-and-installing-node-js-and-npm
  [2]: https://github.com/nvm-sh/nvm
  [3]: https://github.com/nvm-sh/nvm/blob/v0.39.1/install.sh
  [4]: https://docs.npmjs.com/resolving-eacces-permissions-errors-when-installing-packages-globally
