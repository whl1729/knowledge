# Git hooks 使用笔记

## Tools to manage git hooks

- [pre-commmit][1] is a framework for managing and maintaining multi-language pre-commit hooks.

- [pre-commit supported hooks][2]

- pre-commit common commands

  ```bash
  pre-commit install --hook-type commit-msg
  pre-commit install --install-hooks
  ```

## Some useful git hooks

### Basic check

```yaml
repos:
-   repo: https://hub.fastgit.xyz/pre-commit/pre-commit-hooks
    rev: v3.2.0
    hooks:
    -   id: trailing-whitespace
    -   id: end-of-file-fixer
    -   id: check-yaml
    -   id: check-added-large-files
        args: [--maxkb=123]
```

### Check Commit Message

```yaml
repos:
-   repo: https://hub.fastgit.xyz/commitizen-tools/commitizen
    # Used to lint your commit message
    rev: v2.27.0
    hooks:
    -   id: commitizen
        stages: [commit-msg]
```

### Markdownlint

```yaml
repos:
-   repo: https://hub.fastgit.xyz/markdownlint/markdownlint
    rev: v0.11.0
    hooks:
    -   id: markdownlint
```

  [1]: https://pre-commit.com/
  [2]: https://pre-commit.com/hooks.html
