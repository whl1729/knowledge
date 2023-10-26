# Linux 实用工具

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

  [1]: https://github.com/tldr-pages/tldr