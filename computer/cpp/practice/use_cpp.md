# C++ 使用笔记

- assert 是一个宏，不适合写太复杂的语句，比如以下语句会报错

  ```cpp
  // error C3329: syntax error: expected '}' not ')'
  assert(s.validSequence("vbcca", "abc") == vector<int>{0, 1, 2});
  ```

- [cppman: C++ API 离线查询手册][1]

  ```sh
  sudo apt-get install cppman
  ```

- [devdocs: 各种编程语言的 API 查询网站][2]

  [1]: https://github.com/aitjcize/cppman
  [2]: https://devdocs.io/
