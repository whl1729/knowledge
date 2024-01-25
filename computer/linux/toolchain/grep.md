# grep 使用笔记

- 使用 `-F, --fixed-strings` 来过滤特殊字符

  ```sh
  # 过滤 foo.txt 文件中含有左方括号的行
  grep -F [ foo.txt
  ```
