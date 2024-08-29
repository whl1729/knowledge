# Python 使用笔记

## import

- 一般而言，Python 程序里同一个模块只会被导入一次。但如果你使用不同的路径（比如同时使用绝对路径和相对路径），就可能会被导入多次。
  - 这是因为 Python 是以导入路径来作为缓存模块的 key，使用不同的路径时，Python 会误以为这个模块尚未被导入

## 编程风格

- [Python 代码注释][4]

```python
"""Gets and prints the spreadsheet's header columns

Args:
    file_loc (str): The file location of the spreadsheet
    print_cols (bool): A flag used to print the columns to the console
        (default is False)

Returns:
    list: a list of strings representing the header columns
"""
```

## 安装

- [编译 Ubuntu 16.04 + Python 3.8 的 docker 镜像][3]

  ```dockerfile
  FROM ubuntu:16.04

  RUN apt-get update
  RUN apt-get install -y libsqlite3-dev build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev wget devscripts lintian dh-systemd
  RUN wget https://www.python.org/ftp/python/3.8.6/Python-3.8.6.tgz
  RUN tar xzf Python-3.8.6.tgz
  RUN ./Python-3.8.6/configure --enable-optimizations --enable-shared
  RUN make altinstall
  RUN echo "/usr/local/lib/" >> /etc/ld.so.conf
  RUN ldconfig
  RUN wget https://bootstrap.pypa.io/get-pip.py
  RUN python3.8 -V
  RUN python3.8 get-pip.py""
  ```

- 在 Ubuntu 20.04 安装 Python 3.11

  ```sh
  sudo apt update
  sudo add-apt-repository ppa:deadsnakes/ppa -y
  sudo apt update

  # 国内网络安装 Python 速度较慢，有 VPN 的话可以使用 proxychains，即
  # sudo proxychains apt install python3.11
  sudo apt install python3.11
  sudo apt install python3.11-dev
  python3.11 --version

  sudo apt install python-is-python3
  ```

- 修改 Ubuntu 环境下默认的 Python 版本

  ```sh
  sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.8 1
  sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.11 2
  sudo update-alternatives --config python
  ```

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

- 将中文写入 Python 文件

  ```python
  with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
  ```

- [utf vs unicode][1]
  - [unicode -> utf-8][2]

> 伍注：简单地说，unicode 制定了每个字符对应哪个数字的映射关系。
> 但在实际使用时，为了能够正确从二进制流中分隔字符（也就是「解码」），需要先进行「编码」，否则将无法区分不同长度的字符。
> utf-8 就是一种编码/解码的方式。

## Python 虚拟环境

- Python 虚拟环境的依赖管理
  - 比如我本地环境安装了 pytest，虚拟环境中没安装 pytest，我运行 pytest 后，将会在本地环境查找模块，这点要特别注意

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
  [3]: https://medium.com/howtorapeurjob/how-to-build-python3-8-in-ubuntu-16-04-bc559ac1477c
  [4]: https://realpython.com/documenting-python-code/
