# 使用 husky 管理 js 代码库的 git hooks

## 安装 [husky][1]

详见：[husky Documentation][2]

```bash
npx husky-init && npm install
```

## 一些常用的 git hooks

- commitlint
- eslint
- prettier

### [commitlint][3]

- 安装工具

  ```bash
  # Install commitlint cli and conventional config
  npm install --save-dev @commitlint/{config-conventional,cli}
  # For Windows:
  npm install --save-dev @commitlint/config-conventional @commitlint/cli

  # Configure commitlint to use conventional config
  echo "module.exports = {extends: ['@commitlint/config-conventional']}" > commitlint.config.js
  ```

- [添加钩子][5]

  ```bash
  cat <<EEE > .husky/commit-msg
  #!/bin/sh
  . "\$(dirname "\$0")/_/husky.sh"

  npx --no -- commitlint --edit "\${1}"
  EEE
  ```

### eslint

详见： [Commit Better Code with Husky, Prettier, ESLint, and Lint-Staged][4]

1. 安装 prettier

  ```bash
  npm install --save-dev --save-exact prettier eslint-config-prettier
  ```

2. 初始化 eslint config（期间会提示安装 eslint，选 yes 即可）

  ```bash
  npm init @eslint/config
  ```

3. 配置 `.eslintrc.json`

  ```json
  {
    "env": {
        "browser": true,
        "es2021": true
    },
    "extends": ["eslint:recommended", "plugin:react/recommended"],
    "parserOptions": {
        "ecmaFeatures": {
            "jsx": true
        },
        "ecmaVersion": "latest",
        "sourceType": "module"
    },
    "plugins": ["react"],
    "rules": {
        "indent": ["warn", "tab"],
        "quotes": ["error", "single"],
        "semi": ["error", "always"]
    }
  }
  ```

4. 配置 `.eslintignore`

  ```text
  src/*.test.js
  ```

5. 配置 `.prettierrc.json`

  ```json
  {
    "tabWidth": 2,
    "useTabs": true,
    "printWidth": 80,
    "semi": true,
    "trailingComma": "es5",
    "jsxSingleQuote": true,
    "singleQuote": true
  }
  ```

6. 在 `.eslintrc.json` 的 `extends` 配置中增加 `"prettier"`

  ```json
  ...,
  "extends": [
    ...,
    "prettier"
  ],
  ...,
  ```

7. 安装 `lint-staged`

  ```bash
  npm i --save-dev lint-staged
  ```

8. 修改 [`.husky/pre-commit`][6]

  ```sh
  #!/bin/sh
  . "$(dirname "$0")/_/husky.sh"

  npx lint-staged
  ```

9. 在 `package.json` 中添加 lint-staged 配置

  ```json
  ...,
  "lint-staged":{
    "**/*.{js,jsx,ts,tsx}":[
      "npx prettier --write",
      "npx eslint --fix"
    ]
  }
  ```

  [1]: https://github.com/typicode/husky
  [2]: https://typicode.github.io/husky/#/
  [3]: https://github.com/conventional-changelog/commitlint
  [4]: https://www.coffeeclass.io/articles/commit-better-code-with-husky-prettier-eslint-lint-staged
  [5]: commit-msg
  [6]: pre-commit
