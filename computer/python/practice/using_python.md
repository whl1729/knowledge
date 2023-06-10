# Python 使用笔记

## Python 控制台

- 返回字符串和打印字符串
  - 返回字符串会有引号，打印字符串没有引号

  ```python
  >>> def foo(): return "foo"
  >>> def bar(): print("bar")
  >>> foo()
  'foo'
  >>> bar()
  bar
  ```

## 疑问

- Python 设计问题：在一个类里面使用一个不依赖此类的函数时，应该怎么定义它？
  - classmethod，staticmethod, method or function ?

- `python -m pip install` 与  `pip install` 的区别？
- `.spec` 文件有啥作用？
- 为什么 pip install 新的包后，重新运行 pyinstaller 没有将其打包进去？

## Python 编码

- [utf vs unicode][1]
  - [unicode -> utf-8][2]

> 伍注：简单地说，unicode 制定了每个字符对应哪个数字的映射关系。
> 但在实际使用时，为了能够正确从二进制流中分隔字符（也就是「解码」），需要先进行「编码」，否则将无法区分不同长度的字符。
> utf-8 就是一种编码/解码的方式。

## Python 版本管理器

- Tell Ubuntu that python is python3

  ```sh
  apt-get install python-is-python3
  ```

- 使用 virtualenv 管理 Python 版本

  ```sh
  # 安装 virtualenv
  pip install virtualenv

  # 创建一个虚拟环境
  virtualenv --python=<your-python-path> venv

  # 激活（或者说进入）虚拟环境
  ./venv/Scripts/activate

  # 退出虚拟环境
  deactivate
  ```

  [1]: https://stackoverflow.com/a/643810
  [2]: https://stackoverflow.com/a/27939161
