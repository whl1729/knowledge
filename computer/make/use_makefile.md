# Makefile 使用笔记

- 在 Makefile 使用 shell 变量
  - Makefile 默认 shell 为 `/bin/sh`，因此不能直接使用 bash 语法。比如变量赋值不支持 `$` 展开。
  - Makefile 的 target 里面每行命令相互独立，如果后面的命令需要依赖前面定义的变量，需要合在同一行。
  - Makefile 引用 shell 变量需要使用两个 `$`，因为一个 `$` 引用的是 make 变量，不是 shell 变量。

  ```make
  target:
    today=`date +%y-%m-%d`; \
    echo $${today};
  ```

- 获取 Makefile 所在的目录绝对路径

  ```makefile
  ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))
  ```

- [The Variable MAKEFILE_LIST][1]
  - As make reads various makefiles, including any obtained from the MAKEFILES variable, the command line, the default files, or from include directives,
    their names will be automatically appended to the `MAKEFILE_LIST` variable.
  - This means that if the first thing a makefile does is examine the last word in this variable, it will be the name of the current makefile.
  - Once the current makefile has used include, however, the last word will be the just-included makefile.

- [$(realpath names...)][2]
  - For each file name in names return the canonical absolute name.
  - A canonical name does not contain any `.` or `..` components, nor any repeated path separators (/) or symlinks.
  - In case of a failure the empty string is returned.

  [1]: https://ftp.gnu.org/old-gnu/Manuals/make-3.80/html_node/make_17.html
  [2]: https://www.gnu.org/software/make/manual/html_node/File-Name-Functions.html
