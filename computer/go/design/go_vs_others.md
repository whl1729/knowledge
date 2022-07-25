# 对比 Go 语言跟其他语言

## 语法

- 声明语法
  - 类型声明前置 vs 类型声明后置
    - C 采用「类型声明前置」的方式
    - Go、Python、TypeScript 或 Rust 等都采用「类型声明后置」的方式

  ```c
  int x;
  ```

  ```go
  var x int;
  ```

- 循环语句语法
  - for 后面是否加括号
    - C、Java 或 JavaScript 的 for 后面都要加括号
    - Go、Python 的 for 后面不加括号
  - 是否有 while 语句
    - C、JavaScript、Python 等除了 for 语句还有 while 语句
    - Go 的循环结构只有 for 语句，没有 while 语句，但 while 语句可以直接用 for 语句来表达

- if 语句语法
  - if 后面是否加括号
    - C、JavaScript 的 if 后面都要加括号
    - Go、Python 的 if 后面不加括号
  - if 后面是否可以接一个初始化语句
    - Go 的 if 后面可以接一个初始化语句
    - C、JavaScript、Python 均不支持

- switch 语句语法
  - Python 没有 switch 语法
  - fall-through
    - C、JavaScript 的 switch 语句都有 fall-through 的特性
    - Go 没有 fall-through 的特性，即 Go 只会运行匹配到的 case
  - case 的数据类型
    - C 的 case 必须为整数类型的常量
    - Go、JavaScript 的 case 可以为各种类型的常量或变量
  - switch 后面是否可以接一个初始化语句
    - Go 的 switch 后面可以接一个初始化语句
    - C、JavaScript、Python 均不支持

- pointer 语法
  - pointer 是否可以执行四则运算
    - C 指针可以执行四则运算
    - Go 指针不能执行四则运算

- 函数语法
  - defer 语法
    - Go 的 defer 语法可以在函数退出前做一些处理
    - C、JavaScript 都没有提供类似语法
    - Python 的 with 语句有点类似的效果，但个人觉得不够 defer 灵活
  - 是否可以返回多个值
    - C 的函数只能返回一个值。如果要返回多个值，可以返回 struct 或通过函数的指针参数来返回。
    - JavaScript 的函数只能返回一个值。如果要返回多个值，可以返回数组或 Object。
    - Python 的函数可以返回多个值。Python 是把返回的多个值当做一个 tuple。
  - 是否支持默认函数参数
    - C、Go 不支持默认函数参数
    - JavaScript、Python 支持默认函数参数

## 数据结构

- array
  - 是否存在定长数组
    - C、Go 的数组是定长的
    - JavaScript、Python 的数组是变长的
    - 但 Go 的定长数组与 C 有较大差别，C 的数组变量是指向数组首元素的指针，而 Go 的数组变量不是指针，而是值。
    - 因此 Go 的数组赋值、传递给函数时都会发生数组拷贝，而 C 则不会。
  - 添加元素的操作
    - JavaScript 的 array 调用 push 来添加元素
    - Python 的 list 调用 append 来添加元素
    - Go 的 slice 调用 append 来添加元素，但是还要将结果赋回给原来的 slice 变量，比较蹩脚

- map
  - C 没有 map。
  - 索引不存在的 key 时的行为
    - Go、JavaScript 在索引 map 时如果 key 不存在会返回空值，不会抛异常
    - Python 在索引 map 时如果 key 不存在会抛异常

## 操作系统

- 内存管理
  - 函数返回局部变量的地址是否合法
    - C 函数返回局部变量的地址是非法的，会触发 Segmentation Fault 错误
    - Go 函数可以返回局部变量的地址，函数返回后该变量对应的内存依然有效

## 编程范式

- 是否支持面向对象范式
  - C、Go 不支持面向对象范式
  - JavaScript、Python 支持面向对象范式

- 是否支持面向接口范式
  - Go 支持面向接口范式
  - C、JavaScript、Python 不支持面向接口范式
