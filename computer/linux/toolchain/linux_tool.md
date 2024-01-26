# Linux 实用工具

- cat 显示特殊字符

  ```sh
  # cat options:
  #  -e                       equivalent to -vE
  #  -E, --show-ends          display $ at end of each line
  #  -t                       equivalent to -vT
  #  -T, --show-tabs          display TAB characters as ^I
  #  -v, --show-nonprinting   use ^ and M- notation, except for LFD and TAB
  echo "$IFS" | cat -et
  ```

- [atop][4]

- ls

  ```sh
  # 查看当前目录下的所有子目录
  ls -d */
  ```

- lsof: ls open files

  ```sh
  lsof | less
  lsof /usr/bin/bash
  ```

- less
  - Scroll Down: Use the Spacebar to scroll down one page at a time.
  - Scroll Up: Press b to scroll up one page at a time.
  - Scroll Line by Line: Use the Enter key to scroll down one line at a time.
  - Scroll Backward: Press u to scroll backward one-half page at a time.
  - Search Forward: Press / and enter the search term. Use n to find the next occurrence.
  - Search Backward: Press ? and enter the search term. Use N to find the previous occurrence.
  - Jumping to a Specific Line: Press : to bring up the prompt at the bottom, then enter the line number and press Enter.

  ```sh
  less filename
  ```

- type
  - Tell you about aliases, functions, builtins

  ```sh
  $ type ls
  ls is aliased to `ls --color=auto'
  ```

- diff

  ```sh
  # -w: Ignore all whitespace
  diff -w foo.txt foo_new.txt
  ```

- cut

  ```sh
  cut -d: -f1,3 -s foo.txt
  cut -c 1,8 foo.txt
  ```

- sort

  ```sh
  sort -t: -u -k 3 foo.txt
  ```

- find

  ```sh
  find / -type f -size +100M
  find . -mtime +60
  find . –mtime -2
  find / -type f -name *.tar.gz -size +100M -exec rm -f {} \;
  find . -type f -name "index.md" -execdir mv {} README.md \;
  ```

- [paste]: merge lines of file

  ```sh
  # 将 ls 的输出结果合并为一行，中间以逗号分隔。末尾的 - 代表从标准输入读数据
  ls | paste -sd ',' -

  # 将 /tmp/log 的内容合并成一行
  paste -sd ',' /tmp/log
  ```

- [tldr][1]：Linux 命令用法查询工具，比 man 更简洁。

- Linux Performance Tools：性能测试工具

  ![Linux Performance Tools](images/linux_perf_tools_full.png)

## CD Command Hacks

- [CDPATH: 为 cd 命令定义基础目录][3]

  ```sh
  export CDPATH=.:~:/etc:/var
  ```

- Use cd alias to navigate up the directory effectively

  ```sh
  alias ..="cd .."
  alias ...="cd ../.."
  alias ....="cd ../../.."
  alias .....="cd ../../../.."
  alias ......="cd ../../../../.."
  ```

- Perform mkdir and cd using a single command

  ```sh
  function mkdircd () { mkdir -p "$@" && eval cd "\"\$$#\""; }
  ```

- Automatically correct mistyped directory names on cd

  ```sh
  shopt -s cdspell
  ```

## 参考资料

- [Linux 101 Hacks][2]

  [1]: https://github.com/tldr-pages/tldr
  [2]: https://linux.101hacks.com/toc/
  [3]: https://linux.101hacks.com/cd-command/cdpath/
  [4]: https://help.aliyun.com/zh/ecs/how-to-use-the-linux-system-atop-monitoring-tools/
