# 理解 Python import 机制

## `import <>`只支持绝对路径的 import，相对路径的 import 必须使用`from <> import`

- 根据[PEP-0328 关于 "Absoulte Imports" 的描述][1]，为消除二义性，Python 推荐使用绝对路径的 import，并约定其语句格式为`import <>`。

> To resolve the ambiguity in `import foo`,
> it is proposed that foo will always be a module or package reachable from sys.path. This is called an absolute import.

- 根据[PEP-0328 关于 "Relative Imports" 的描述][2]，考虑到相对路径的 import 在调整包的结构等方面的便利性，
  Python 也支持相对路径的 import，并约定其语句格式为`from <> import`。

> The most important of which is being able to rearrange the structure of large packages without having to edit sub-packages.
> In addition, a module inside a package can't easily import itself without relative imports.

## `import <>`语句不能 import 模块内的属性，而`from <> import`语句可以

先来看看[Python Reference 定义的 "The import statement"][3]:

```
import_stmt     ::=  "import" module ["as" identifier] ("," module ["as" identifier])*
                     | "from" relative_module "import" identifier ["as" identifier]
                     ("," identifier ["as" identifier])*
                     | "from" relative_module "import" "(" identifier ["as" identifier]
                     ("," identifier ["as" identifier])* [","] ")"
                     | "from" relative_module "import" "*"
module          ::=  (identifier ".")* identifier
relative_module ::=  "."* module | "."+
```

普通的 import 语句与 from import 语句在 import 对象上的异同点如下：

- 相同点：两者都可以 import 模块（也可以 import 包，毕竟 package is also module.）
- 不同点：普通的 import 语句只能 import 模块，不能 import 模块中的属性；
  而 from import 语句除了可以 import 模块，还可以 import 模块中的属性。

比如一个项目下有`main.py`和`foo.py`两个文件，并且`foo.py`定义了函数`hi`。
那么在`main.py`函数中，

- `import foo` 和 `from foo import hi` 是合法的
- `import foo.hi`是非法的，报错信息如下：
  `ModuleNotFoundError: No module named 'foo.hi'; 'foo' is not a package`

  [1]: https://www.python.org/dev/peps/pep-0328/#rationale-for-absolute-imports
  [2]: https://www.python.org/dev/peps/pep-0328/#rationale-for-relative-imports
  [3]: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement

