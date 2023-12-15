# sed 使用笔记

- 把保持空间的内容追加到模式空间（先加上换行符再追加）：命令G

  ```sh
  sed -n -e '/Manager/!h' -e '/Manager/{x;G;s/\n/:/;p}' empnametitle.txt
  ```

- 把保持空间的内容复制到模式空间：命令g（get）

  ```sh
  sed -n -e '/Manager/!h' -e '/Manager/{g;p}' empnametitle.txt
  ```

- 把模式空间的内容追加到保持空间（先加上换行符再追加）：命令H

  ```sh
  sed -n -e '/Manager/!h' -e '/Manager/{H;x;p}' empnametitle.txt
  ```

- 把模式空间的内容复制到保持空间：命令h（hold）

  ```sh
  sed -n -e '/Manager/!h' -e '/Manager/{x;p}' empnametitle.txt
  ```

- 用保持空间替换模式空间：命令x (exchange)

  ```sh
  sed -n -e '{x;n}' -e '/Manager/{x;p}' empnametitle.txt
  ```

- 执行多个命令：用大括号括起来，各命令之间用分号隔开

  ```sh
  sed -e "{s/John/Johnny/; s/Jane/Janny/}" employee.txt
  ```

- 显示每一行的行号

  ```sh
  sed -e "=" employee.txt | sed '{N;s/\n/ /}'
  ```

- 读取下一行并附加到模式空间

  ```sh
  sed -e '{N;s/\n/:/}' empnametitle.txt
  ```

- 附加命令：a, i, c

  ```sh
  # 在 log.txt 第2行下面添加一行内容
  sed '2 a hello world' log.txt

  # 在 log.txt 第2行上面添加一行内容
  sed '2 i hello world' log.txt

  # 将 log.txt 第2行修改为 hello world
  sed '2 c hello world' log.txt
  ```

- 备份文件再原地修改

  ```sh
  # 先备份 employee.txt 为 employee.txt.bak，再原地修改 employee.txt
  sed -i.bak 's/John/Johnny/g' employee.txt
  ```

- sed 正则表达式：`\+,\?, \{n\}, \b`

  ```sh
  sed -n '/log: \+/ p' log.txt
  sed -n '/log: \?/ p' log.txt
  sed -n '/[0-9]\{5\}/ p' log.txt
  sed -n '/\bthe\b/ p' words.txt
  ```

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
