# JavaScript 奇怪的语法

最近在学习JavaScript，发现有些语法设计得很奇怪，特此记录下来，再作推敲。

## 分号

以下代码片段如果不在行末加上分号，使用 node 来运行时会报错：

```javascript
let foo = [1, 2]
[foo[0], foo[1]] = [foo[1], foo[0]]
```

```javascript
console.log('Hello world')
(function () { console.log('Nice to meet you')})()
```

## 类型

### 字面常量 vs 原始类型

我特别不能理解对字面常量和原始类型进行`typeof`操作返回的结果：

```javascript
typeof 'abc'  // output: 'string'
typeof new String('abc')  // output: 'object'
```

我的困惑是：

- string 与 String 这两种类型有什么区别？
- object 与 Object 这两种类型有什么区别？
- typeof String 变量为啥不返回 'String' 而是返回 'object'？这有点违背直觉。

### 令人费解的 typeof 操作符

- "boolean" if the value is a Boolean
- 'string' if the value is a string
