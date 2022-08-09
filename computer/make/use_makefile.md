# Makefile 使用笔记

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
