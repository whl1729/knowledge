# eslint 使用笔记

## Installation and Usage

- Installation

  ```sh
  npm install eslint --save-dev
  # or
  yarn add eslint --dev
  ```

- Set up a configuration file

  ```sh
  npm init @eslint/config
  # or
  yarn create @eslint/config
  ```

- Run ESLint on any file or directory

  ```sh
  npx eslint yourfile.js
  ```

## Configuration

- Set rules in `.eslintrc.{js,yml,json}`
  - The names "semi" and "quotes" are the names of rules in ESLint.
  - The first value is the error level of the rule and can be one of these values:
    - "off" or 0 - turn the rule off
    - "warn" or 1 - turn the rule on as a warning (doesn't affect exit code)
    - "error" or 2 - turn the rule on as an error (exit code will be 1)

  ```javascript
  {
    "rule": {
      "semi": ["error", "always"],
      "quote": ["error", "double"],
      "no-console": ["off"],
      "eqeqeq": ["error", "always"],
    }
  }
  ```

- Turn on all of the rules marked "✓" on the rules page

  ```javascript
  {
    "extends": "eslint:recommended"
  }
  ```

## 参考资料

1. [Getting Started with ESLint][1]

  [1]: https://eslint.org/docs/user-guide/getting-started
