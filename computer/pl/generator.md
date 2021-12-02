# 生成器

目前不少语言都支持生成器，比如JavaScript和Python。下面结合这些语言进行讨论。

## 什么是生成器？

### JavaScript 生成器

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

### Python 生成器

## 生成器与迭代器有什么联系与区别？

## 为什么需要生成器？

按照[PEP 255][4]的说法，生成器是为了解决生产者函数在实现复杂的任务时需要维护状态的问题而诞生的。
简而言之，生成器可以使我们编程更简单。但到底简单了哪里，需要实践来加深理解。
可以对比同一个问题使用生成器来解决和不使用生成器来解决的情况，来理解生成器的作用。

### 案例1：作为迭代器的生成器

作为迭代器的生成器，意味着它是一个可迭代对象，可以出现在循环、数组解构赋值、展开语法等位置。 这给编程带来了方便。
我感觉它的一个好处是将数据生成的逻辑封装起来，构成一个数据源，与数据处理隔离开来。一定程度上可以降低复杂性。

#### 使用生成器

```javascript
function* fib() {
  let a = 0
  let b = 1
  let temp
  for (let i = 0; i < 100; i++) {
    yield b
    temp = a
    a = b
    b = b + temp
  }
}

// for-of loops
for (let f of fib()) {
  console.log(f)
}

// Array destructuring
let [a, b, c] = fib()

// Spread operator
let arr = [...fib()]

// Array.from()
let arr2 = Array.from(fib())

// Set constructor
let set = new Set(fib())
```

#### 不使用生成器

不使用生成器的话，我们只能事先生成一遍数据，并保存到一个数组中。
如果数据量很大的话，将会消耗较多内存空间。
而且如果是无穷序列的话，我们将无法采取事先生成的方案。

### 案例2：计算Fibonacci数列的元素

实现一个函数fib，每次调用该函数时会返回Fibonacci数列的一个元素。

#### 使用生成器

```python
def fib():
    a, b = 0, 1
    while 1:
        yield b
        a, b = b, a+b
```

#### 不使用生成器

```python
a, b = 0, 1

def fib():
    global a, b
    a, b = b, a+b
    return a
```

#### 对比

使用生成器的封装性更好。
这个问题是不断返回一个无穷序列的元素，因此需要维持状态，
如果不使用生成器，需要在函数外部维持状态，从而破坏了封装性。

## 生成器与异步编程有什么联系？

## 参考资料

1. [MDN: Generator][1]
2. [Iteration protocols][2]
3. [What exactly are iterator, iterable, and iteration?][3]
4. [PEP 255 -- Simple Generators][4]

  [1]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Generator
  [2]: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Iteration_protocols
  [3]: https://stackoverflow.com/questions/9884132/what-exactly-are-iterator-iterable-and-iteration
  [4]: https://www.python.org/dev/peps/pep-0255/
