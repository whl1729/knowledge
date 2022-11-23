# pre-commit 使用笔记

[pre-commmit][1] is a framework for managing and maintaining multi-language pre-commit hooks.

## Quick Start

1. Install pre-commit

  ```bash
  pip install pre-commit
  ```

2. Add a pre-commit configuration
  - create a file named .pre-commit-config.yaml
  - you can generate a very basic configuration using pre-commit sample-config

3. Install git hook script for pre-commit stage

  ```bash
  # 以下命令只会安装 .git/hooks/pre-commit 脚本
  # 如果想安装其他阶段的 git hooks 脚本，需要提供 `-t` 或 `--hook-type` 参数
  pre-commit install
  ```

4. Install git hook script for commit-msg stage

  ```bash
  pre-commit install -t commit-msg
  ```

5. 安装 `.pre-commit-config.yaml` 配置的各种 git hooks

  ```bash
  # 如果不提前执行以下命令，用户首次进行 git commit 时，
  # pre-commit 会自动安装配置好的各种 git hooks，会使得这次 commit 显得特别慢。
  pre-commit install --install-hooks
  ```

6. 对所有文件进行检查

  ```bash
  pre-commit run -a
  ```

## Configuration

- Passing auguments to hooks

  ```yaml
  - repo: https://github.com/PyCQA/flake8
    rev: 4.0.1
    hooks:
    - id: flake8
      args: [--max-line-length=131, --max-complexity=10]

  - repo: https://github.com/markdownlint/markdownlint
    rev: v0.11.0
    hooks:
    - id: markdownlint
      args: [-s, .mdlrc.rb]
  ```

## Some useful git hooks

You can find a lot of useful git hooks in [pre-commit supported hooks][2].

### Basic check

```yaml
repos:
  - repo: https://hub.fastgit.xyz/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
```

### Check Commit Message

```yaml
repos:
  - repo: https://hub.fastgit.xyz/commitizen-tools/commitizen
    rev: v2.27.0
    hooks:
      - id: commitizen
        stages: [commit-msg]
```

### Markdownlint

```yaml
repos:
  - repo: https://hub.fastgit.xyz/markdownlint/markdownlint
    rev: v0.11.0
    hooks:
    - id: markdownlint
      args: [-s, .mdlrc.rb]
```

- [Example for mdlrc.rb][3]

  ```ruby
  all
  exclude_rule 'MD001'
  exclude_rule 'MD002'
  rule 'MD013', :line_length => 160
  rule 'MD026', :punctuation => ".,;:"
  rule 'MD029', :style => false
  ```

- [Disable a rule on command line][3]
  - see `mdl -h` for more details.

  ```shell
  mdl -r ~MD001,~MD002 xxx.md
  ```

  [1]: https://pre-commit.com/
  [2]: https://pre-commit.com/hooks.html
  [3]: https://github.com/markdownlint/markdownlint/blob/main/.mdl_style.rb
  [4]: https://github.com/markdownlint/markdownlint/blob/main/docs/configuration.md#specifying-which-rules-mdl-processes
