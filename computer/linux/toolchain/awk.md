# awk 使用笔记

- awk 分隔符：FS、OFS、RS、ORS

  ```sh
  awk 'BEGIN {RS="-\n"; FS=","; ORS="\n---\n"; OFS=":";} {print $2, $3}' employee.txt
  ```

- awk 程序结构区域（BEGIN，body，END）
  - BEGIN 和 END 必须大写
  - BEGIN 和 END 区域的命令均只执行一次
  - BEGIN 区域适合用来打印报文头部信息，以及初始化变量
  - END 区域适合打印报文结尾信息，以及做一些清理动作

  ```sh
  awk 'BEGIN {FS=":"; print "---header---" } \
  /mail/ {print $1} \
  END {print "---footer---"}' /etc/passwd
  ```
