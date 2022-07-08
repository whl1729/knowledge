# Webpack Guides

## Chapter 01: Getting Started

### Basic Setup

- Installation (locally)

  ```sh
  mkdir webpack-demo
  cd webpack-demo
  npm init -y
  npm install webpack webpack-cli --save-dev
  ```

### Creating a Bundle

- `npx webpack`
  - Runs the webpack binary (./node_modules/.bin/webpack) of the webpack package we installed in the beginning.

- Dependency graph and bundle
  - By stating what dependencies a module needs, webpack can use this information to build a dependency graph.
  - It then uses the graph to generate an optimized bundle where scripts will be executed in the correct order.

### Modules

- Behind the scenes, webpack actually "transpiles" the code (Wu: the import and export statements) so that older browsers can also run it.

- Webpack will not alter any code other than import and export statements.
  - If you are using other ES2015 features, make sure to use a transpiler such as Babel via webpack's loader system.

> 伍注：webpack 只负责处理模块导入/导出（import/export）语句，其他语句的转换需要使用其他工具，比如 Babel。

### Using a Configuration

- How to use a configuration
  - `npx webpack --config webpack.config.js`

- When to use the `--config`
  - If a webpack.config.js is present, the webpack command picks it up by default.
  - We use the --config option here only to show that you can pass a configuration of any name.
  - This will be useful for more complex configurations that need to be split into multiple files.

### NPM Scripts

- Adding an npm script in `package.json`:
  - within scripts we can reference locally installed npm packages by name the same way we did with npx.

  ```json
  {
    "scripts": {
      "build": "webpack"
    }
  }
  ```

- Pass parameters to webpack
  - Custom parameters can be passed to webpack by adding two dashes between the npm run build command and your parameters.
  - E.g. `npm run build -- --color`.
