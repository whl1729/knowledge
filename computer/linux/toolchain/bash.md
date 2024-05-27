# bash 使用笔记

- [bash IFS 的用法][1]

  ```sh
  string=foo:bar:foobar
  old_ifs="$IFS"
  IFS=":"
  for i in $string
  do
    echo "'$i' is the splitted word"
  done
  # output:
  # 'foo' is the splitted word
  # 'bar' is the splitted word
  # 'foobar' is the splitted word
  ```

- for 循环加双引号与不加双引号的区别

  ```sh
  foo="hello world"
  for f in ${foo[@]}; do echo $f; done  # 打印两行，第一行是 "hello"，第二行是 "world"；跟 `for f in $foo` 效果一致
  for f in "${foo[@]}"; do echo $f; done  # 打印一行，内容为 "hello world"
  ```

- 获取当前脚本所在目录的绝对路径

  ```sh
  SCRIPT_DIR="$(cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P)"
  ```

  [1]: https://www.baeldung.com/linux/ifs-shell-variable
