# flask 使用笔记

- [flask 变量指定为 `path` 才能允许包含斜杠][1]

  ```python
  # input 不能匹配包含斜杠的字符串
  @app.route("/<string:input>")
  def hello(input):
    pass

  # input 可以匹配包含斜杠的字符串
  @app.route("/<path:input>")
  def hello(input):
    pass
  ```

- 如果想让服务监听所有 IP 地址，需要将 host 设置为 `0.0.0.0`
  - 特别地，如果你是在容器里面跑 flask 服务，并且想在容器外面访问该服务，就需要这样设置。

  ```py
  app.run(host="0.0.0.0", port=8080)
  ```

  [1]: https://stackoverflow.com/a/24533109/11467929
