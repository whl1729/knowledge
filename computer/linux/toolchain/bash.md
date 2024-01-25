# bash 使用笔记

- for 循环加双引号与不加双引号的区别

  ```sh
  foo="hello world"
  for f in ${foo[@]}; do echo $f; done  # 打印两行，第一行是 "hello"，第二行是 "world"
  for f in "${foo[@]}"; do echo $f; done  # 打印一行，内容为 "hello world"
  ```

- 获取当前脚本的绝对路径

  ```sh
  SCRIPTPATH="$(cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P)"
  ```
