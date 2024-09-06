# BeautifulSoup 使用笔记

- [`.string` vs `.text`][1]
  - 参考 [bs4 官方文档][2]，当 tag 包含多个子 tag 时，前者会返回 None；后者会返回所有子 tag 合并后的字符串
  - 简单而言，使用 `.text` 更安全

  [1]: https://stackoverflow.com/a/25328374/11467929
  [2]: https://www.crummy.com/software/BeautifulSoup/bs4/doc/#string
