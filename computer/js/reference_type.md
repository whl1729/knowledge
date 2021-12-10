# JavaScript 引用类型

前天和同事讨论 JavaScript 函数参数传递时，发现自己对 JavaScript 的引用类型理解有误。
先上代码：

```javascript
function addWorld(str) {
  str += ' world'
}

let str = new String('hello')
addWorld(str)
console.log(str)
```

这段代码的打印结果是什么？我以为是'hello world'，我的推理逻辑如下：
1. String 类型属于 Object 类型
2. Object 类型都属于 引用类型
3. 把 String 变量传递给函数时，传递的是引用而非值，因此会修改原来的变量

但正确答案却是'hello'，这说明我的推理逻辑有误，我猜是第2点出了问题。
