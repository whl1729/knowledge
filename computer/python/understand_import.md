# 理解 Python import 机制

## 普通的 import 语句与 from import 语句在 import 对象上的区别

- 首先，两者都可以 import 模块（也可以 import 包，毕竟 package is also module.）
- 然后，普通的 import 语句只能 import 模块，不能 import 模块中的属性；
  而 from import 语句除了可以 import 模块，还可以 import 模块中的属性。

比如一个项目下有`main.py`和`foo.py`两个文件，并且`foo.py`定义了函数`hi`。
那么在`main.py`函数中，以下 import 语句是合法的：

- `import foo` 和 `from foo import hi` 是合法的
- `import foo.hi`是非法的，报错信息如下：
  `ModuleNotFoundError: No module named 'foo.hi'; 'foo' is not a package`
