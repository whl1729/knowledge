# YAML 学习笔记

- YAML 的字符串转换为布尔值现象
  - 在 YAML 配置文件中，某些字符串（如 OFF、ON、YES、NO、TRUE、FALSE 等）会被自动解析为布尔值。
  - 这是因为 YAML 规范中定义了一个布尔类型的转换规则，这些特定的字符串会被视为布尔值。
  - 为避免自动转换，可以加上双引号/单引号来避免这种情况。