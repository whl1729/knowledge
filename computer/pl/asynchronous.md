# 异步编程

### 什么是异步编程？

要理解异步编程，那应该先理解「同步编程」。
同步编程的概念很简单，就是逐步执行，上一步未执行完成就不会执行下一步。
而异步编程中就不是这样子了：上一步的语句可能会晚于下一步的语句执行。
举个例子：

```javascript
// 同步编程
function sayHello() {
  console.log('hello')
}

function greet() {
  sayHello();
  console.log('world')
}
```

```javascript
// 异步编程
function sleep(timeoutInMilliseconds) {
  return new Promise((resolve, reject) => {
    const timer = setTimeout(() => {
      clearTimeout(timer)
      resolve()
    }, timeoutInMilliseconds)
  })
}

async function sayHello() {
  await sleep(1000)
  console.log('hello')
}

function greet() {
  sayHello();
  console.log('world')
}
```

我们对比两个例子中的greet函数：

- 第一个例子中，首先执行sayHello函数，打印"hello"；再执行第二行，打印"world"。
- 第二个例子中，虽然也是首先执行sayHello函数，但还没打印"hello"就返回，接着执行第二行，打印"world"，1秒后再打印"hello"。

### 能否不用promise来举例说明异步编程？

### 将上面的异步编程例子里的sayHello函数中的await关键字去掉，结果会怎样？
