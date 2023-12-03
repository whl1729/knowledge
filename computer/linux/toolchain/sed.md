# sed 使用笔记

- 打印某个文件的某几行

  ```sh
  sed -n '10,20p' README.md
  ```

- 当替换操作完成后，打印替换后的行

  ```sh
  sed -n 's/John/Johnny/gp' employee.txt
  ```
