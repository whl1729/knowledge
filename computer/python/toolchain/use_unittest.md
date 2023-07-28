# unittest 使用笔记

- 测试用例目录设计
  - test 目录及子目录下都需要有 `__init__.py` 文件，否则会报 `ImportError: Failed to import test module: busmust` 之类的错误。

  ```text
  myproject
    |-- test
          |-- __init__.py
          |-- foo
               |-- __init__.py
               |-- test_bar.py
  ```
