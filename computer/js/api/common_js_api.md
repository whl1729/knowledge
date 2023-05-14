# JavaScript 常用 API

- 获取某个对象 obj 的所有方法（类似 Python 的 dir()）

  ```javascript
  Object.getOwnPropertyNames(Object.getPrototypeOf(obj))

  // 如果你已经知道对象的原型，比如是 Array，则可以化简为
  Object.getOwnPropertyNames(Array)
  ```
