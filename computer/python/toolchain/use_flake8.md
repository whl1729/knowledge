# flake8 使用笔记

## config file

The user settings are read from the ~/.config/flake8 file (or the ~/.flake8 file on Windows). Example:

```text
[flake8]
ignore = E226,E302,E41
max-line-length = 160
exclude = tests/*
max-complexity = 10
```

## settings

## 参考资料

- [flake8 官方文档][1]

  [1]: https://flake8.pycqa.org/en/2.5.5/config.html
