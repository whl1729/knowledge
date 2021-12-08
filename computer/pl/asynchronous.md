# 异步编程

## 什么是异步编程？

要理解异步编程，那应该先理解「同步编程」。
不妨结合实例来理解：

```javascript
// 同步编程
function sayHello() {
  console.log('hello')
}

function sayWorld() {
  console.log('world')
}

function greet() {
  sayHello();
  sayWorld();
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

function sayWorld() {
  console.log('world')
}

function greet() {
  sayHello();
  sayWorld();
}
```

我们对比两个例子中的greet函数：

- 第一个例子中，首先执行sayHello函数，打印"hello"；再执行sayWorld函数，打印"world"。
- 第二个例子中，虽然也是首先执行sayHello函数，但还没打印"hello"就返回，接着执行sayWorld函数，打印"world"，1秒后再打印"hello"。

第二个例子可以说是异步编程的一个典型使用场景：

有些I/O任务比较耗时（比如读写大文件、等待用户输入、等待服务器响应等），
如果CPU一直等待I/O任务完成后再干其他事情，会很浪费CPU资源。
为了提高CPU利用率，可以在启动I/O任务后去干其他事情，
直到I/O任务完成、CPU收到通知后，再恢复运行原来的事情。

这里可以看出同步编程与异步编程的一个区别：

- 同步编程是按顺序执行，做完一个任务再做下一个任务。
- 异步编程是不能保证执行顺序的，可能同时启动多个任务。
  至于这些任务哪个先完成、哪个后完成，得看具体情况。

### 异步编程与并发编程有什么联系？

我目前认为：异步编程是并发编程的前提条件。

在我的理解中，并发编程一般指多线程编程、多进程编程。
无论是多线程还是多进程，都是多个任务同时运行，而不是先做完一个任务再做下一个任务。

那么异步编程与并发编程有什么区别？

我们需要注意到，JavaScript是单线程运行的，但它支持异步编程。

### 异步编程与生成器有什么联系？

## 怎样实现异步编程？

### 在JavaScript中能否不用promise来实现异步编程？

### 将上面的异步编程例子里的sayHello函数中的await关键字去掉，结果会怎样？

