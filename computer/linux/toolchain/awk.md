# awk 使用笔记

- awk 打印多个目标片段
  - 当 action 用大括号括起来时，后面不需要加分号
  - 当没有 action，而紧跟着是一个新的 pattern 时，需要加分号来区分前后两个语句（如下面的 `flag;`）

  ```sh
  # 包含边界
  awk '/foo/ {flag=1} flag; /bar/ {flag=0}' file
  # 不包含边界
  awk '/foo/ {flag=1; next} /bar/ {flag=0} flag' file
  ```

- awk 使用 Shell 变量

  ```sh
  awk -v a="$var1" -v b="$var2" 'BEGIN {print a,b}'
  awk -v a="$var1" '$0~a' file
  ```

- awk 内置函数

  ```sh
  awk 'BEGIN {print log(10); print sqrt(20); print cos(30)}'
  ```

- awk 操作符
  - 字符串操作符：（空格）是连接字符串的操作符
  - 比较操作符
  - 正则表达式操作符：`~, !~`

  ```sh
  awk 'BEGIN {str1="Hello"; str2="World", str3=str1 str2; print "str3 is:", str3}'
  awk -F ',' '$5 <= 5' items.txt
  awk -F "," '$2 ~ "Tennis"' items.txt
  awk -F "," '$2 !~ "Tennis"' items.txt
  awk -F ':' '$NF ~ /\/bin\/bash/' /etc/passwd
  ```

- awk 内置变量
  - NR: Number of the Record
  - FILENAME
  - FNR: Number of the Record in the current File
  - NF: Number of fileds in the current input record, so `$NF` represents the last field

  ```sh
  awk '{printf "FILENAME=%s  NR=%d  FNR=%d", FILENAME, NR, FNR"}' foo.txt bar.txt
  ```

- awk 分隔符：FS、OFS、RS、ORS

  ```sh
  awk 'BEGIN {RS="-\n"; FS=","; ORS="\n---\n"; OFS=":";} {print $2, $3}' employee.txt
  ```

- awk 程序结构区域（BEGIN，body，END）
  - BEGIN 和 END 必须大写
  - BEGIN 和 END 区域的命令均只执行一次
  - BEGIN 区域适合用来打印报文头部信息，以及初始化变量
  - END 区域适合打印报文结尾信息，以及做一些清理动作
  - BEGIN 语法：`BEGIN {awk-commands}`
  - BODY 语法：`/pattern/ {action}`
  - END 语法：`END {awk-commands}`

  ```sh
  awk 'BEGIN {FS=":"; print "---header---" } \
  /mail/ {print $1} \
  END {print "---footer---"}' /etc/passwd
  ```
