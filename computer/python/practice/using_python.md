# Python 使用笔记

## 疑问

- Python 设计问题：在一个类里面使用一个不依赖此类的函数时，应该怎么定义它？
  - classmethod，staticmethod, method or function ?

- `python -m pip install` 与  `pip install` 的区别？
- `.spec` 文件有啥作用？
- 为什么 pip install 新的包后，重新运行 pyinstaller 没有将其打包进去？

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
