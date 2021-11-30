# 生成器

目前不少语言都支持生成器，比如JavaScript和Python。下面分别讨论。

## JavaScript 生成器

### 什么是生成器？

MDN的定义是：

> The Generator object is returned by a generator function and it conforms to both the iterable protocol and the iterator protocol.

翻译一下：生成器对象是由生成器函数返回的，并且符合可迭代协议和迭代器协议。

这里有三个关键词需要理解：

- 生成器函数：使用`function*`来声明，返回生成器对象。（「生成器对象」和「生成器函数」似有循环定义的问题）
- 可迭代协议
  - 可迭代对象必须实现`@@iterator`方法。
  - 这意味着对象（或者它原型链上的某个对象）必须有一个键为`@@iterator`的属性，可通过常量`Symbol.iterator`访问该属性。
- 迭代器协议
  - 定义了产生一系列值（可以是有限个或无限个）的标准方式。
  - 当值为有限个时，所有的值都被迭代完毕后，则会返回一个默认返回值。
  - 只有实现了一个拥有特定语义的`next()`方法，一个对象才能成为迭代器。特定语义是指：
    - `next()` 方法必须返回一个对象，该对象应当有两个属性：done 和 value。

顺便说一下「可迭代对象」与「迭代器」的区别：

很简单，前者含有返回后者的方法。即可迭代对象定义了一个`@@iterator`方法，这个方法返回一个迭代器。

## 参考资料

1. [MDN: Generator][1]
2. [Iteration protocols][2]
3. [What exactly are iterator, iterable, and iteration?][3]

  [1]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator
  [2]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols
  [3]: https://stackoverflow.com/questions/9884132/what-exactly-are-iterator-iterable-and-iteration
