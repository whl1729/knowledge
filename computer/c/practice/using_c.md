# C 语言使用笔记

- 输入命令行运行C程序时，用双引号括起来的多个单词会被视为一个参数。

## gcc

- 使用未定义的 struct 指针，gcc 会有 warning，但可以编译通过并运行。

  ```c
  #include <stdio.h>

  void print_num(int *num) { printf("num = %d\n", *num); }

  int main() {
    int foo = 1;
    struct bar *ptr = &foo;
    print_num(ptr);
    return 0;
  }
  ```
