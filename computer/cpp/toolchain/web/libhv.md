# libhv 使用指南

Github 地址：[libhv][1]

## 解析请求数据

### 解析 JSON 格式的请求数据

```cpp
int Handler::test(const HttpContextPtr& ctx) {
    bool foo = ctx->get<bool>("foo");
    int bar = ctx->get<int>("bar");
    float cat = ctx->get<float>("cat");
    std::string dog = ctx->get("dog");
}
```

  [1]: https://github.com/ithewei/libhv
