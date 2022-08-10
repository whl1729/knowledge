# Go 语法

- [iota][1]
  - 代表连续的无类型的整数常量。
  - 取值为对应的 const 声明语句的下标，从 0 开始。
  - 如果第一个 const 语句的右边表达式使用了 iota，后面的 const 语句可以省略右边表达式。

  ```go
  const (
    c0 = iota  // c0 == 0
    c1 = iota  // c1 == 1
    c2 = iota  // c2 == 2
  )

  const (
    bit0, mask0 = 1 << iota, 1<<iota - 1  // bit0 == 1, mask0 == 0  (iota == 0)
    bit1, mask1                           // bit1 == 2, mask1 == 1  (iota == 1)
    _, _                                  //                        (iota == 2, unused)
    bit3, mask3                           // bit3 == 8, mask3 == 7  (iota == 3)
  )
  ```

  [1]: https://go.dev/ref/spec#Iota
