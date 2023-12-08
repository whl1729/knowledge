# sed 使用笔记

- GNU sed 专有的替换标识：`\l, \L, \u, \U, \E`

  ```sh
  sed 's/^\([^:]*)\)\(.*\)/\U\1\E\2/' /etc/passwd
  ```

- 替换命令分界符

  ```sh
  sed 's@/usr/local/bin@/usr/bin@' path.txt
  ```

- 替换命令组合

  ```sh
  sed -n 's/manager/Director/igpw output.txt' employee.txt
  ```

- i: 忽略大小写标志

  ```sh
  sed 's/john/Johnny/i employee.txt'
  ```

- w: 把模式空间内容写到文件中

  ```sh
  sed '3,10 w output.md' README.md
  ```

- `-e`: 执行多个操作

  ```sh
  sed -n -e '/^root/p' -e '/^along/p' /etc/passwd
  ```

- 打印某个文件的某几行

  ```sh
  sed -n '10,20p' README.md
  ```

- p: 当替换操作完成后，打印替换后的行

  ```sh
  sed -n 's/John/Johnny/gp' employee.txt
  ```
