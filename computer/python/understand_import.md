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

## 模块搜索机制

[Python Tutorial "6. Modules"][5]描述了 "The Module Search Path":

When a module named spam is imported, the interpreter first searches for a built-in module with that name.
If not found, it then searches for a file named spam.py in a list of directories given by the variable sys.path.
sys.path is initialized from these locations:

- The directory containing the input script (or the current directory when no file is specified).
- PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
- The installation-dependent default (by convention including a site-packages directory, handled by the site module).

[Python Reference "7.11 The import statement"][3]描述了 `from <> import` 的搜索算法：

The from form uses a slightly more complex process:

- find the module specified in the from clause, loading and initializing it if necessary;
- for each of the identifiers specified in the import clauses:
  - check if the imported module has an attribute by that name
  - if not, attempt to import a submodule with that name and then check the imported module again for that attribute
  - if the attribute is not found, ImportError is raised.
  - otherwise, a reference to that value is stored in the local namespace,
    using the name in the as clause if it is present, otherwise using the attribute name

[realpython 的这篇博客][6]也描述了Python import 的工作机制：

- The first thing Python will do is look up the name abc in `sys.modules`.
  This is a cache of all modules that have been previously imported.
- If the name isn’t found in the module cache, Python will proceed to search through a list of **built-in modules**.
  These are modules that come pre-installed with Python and can be found in the Python Standard Library.
- If the name still isn’t found in the built-in modules, Python then searches for it in a list of directories defined by `sys.path`.
  This list usually includes the **current directory**, which is searched first.

## 模块加载机制

[stack overflow 的这个回答][7] 通俗易懂地解释了 Python 模块加载的工作机制：

- running vs importing
  - There is a big difference between directly running a Python file, and importing that file from somewhere else.
  - **Just knowing what directory a file is in does not determine what package Python thinks it is in.**
  - That depends, additionally, on how you load the file into Python (by running or by importing).

- Two ways to load a Python file
  - As the top-level script
    - A file is loaded as the top-level script if you execute it directly, for instance by typing python myfile.py on the command line.
    - There can only be one top-level script at a time; the top-level script is the Python file you ran to start things off.
  - As a module
    - A file is loaded as a module when an import statement is encountered inside some other file.

- Naming
  - When a file is loaded, it is given a name (which is stored in its `__name__` attribute).
  - If it was loaded as the top-level script, its name is `__main__`.
  - If it was loaded as a module, its name is the filename, preceded by the names of any packages/subpackages of which it is a part, separated by dots.
  - **If a module's name has no dots, it is not considered to be part of a package.**

- Relative imports vs module name
  - if your module's name is `__main__`, it is not considered to be in a package.
  - Its name has no dots, and therefore you cannot use `from .. import` statements inside it.
  - If you try to do so, you will get the "relative-import in non-package" error.

- Relative imports in interactive interpreter
  - When you run the interactive interpreter, the "name" of that interactive session is always `__main__`.
  - Thus you cannot do relative imports directly from an interactive session. Relative imports are only for use within module files.

## Python 官方约定的 Import 风格

[PEP-8 约定了 Import 语句的风格][4]：

- Imports should usually be on separate lines.
- Imports are always put at the top of the file, just after any module comments and docstrings, and before module globals and constants.
  - Imports should be grouped in the following order:
    - Standard library imports.
    - Related third party imports.
    - Local application/library specific imports.
- Absolute imports are recommended,
  - as they are usually more readable and
  tend to be better behaved (or at least give better error messages) if the import system is incorrectly configured
  (such as when a directory inside a package ends up on sys.path).
  - Explicit relative imports are an acceptable alternative to absolute imports,
    especially when dealing with complex package layouts where using absolute imports would be unnecessarily verbose
- When importing a class from a class-containing module, it's usually okay to import the class name.
- Wildcard imports (`from <module> import *`) should be avoided.

  [1]: https://www.python.org/dev/peps/pep-0328/#rationale-for-absolute-imports
  [2]: https://www.python.org/dev/peps/pep-0328/#rationale-for-relative-imports
  [3]: https://docs.python.org/3/reference/simple_stmts.html#the-import-statement
  [4]: https://www.python.org/dev/peps/pep-0008/#imports
  [5]: https://docs.python.org/3/tutorial/modules.html#the-module-search-path
  [6]: https://realpython.com/absolute-vs-relative-python-imports/#how-imports-work
  [7]: https://stackoverflow.com/a/14132912/11467929

