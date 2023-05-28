# GET STARTED 分析笔记

## 这篇文档的主题是什么

介绍 OpenAI API 的基础知识

## 目前为止我知道什么

- 简单使用过 ChatGPT
- GPT 好像是生成式预训练的意思
- ChatGPT 大概是根据输入来计算概率，从而生成输出

## 目前为止我不知道什么

- ChatGPT 的工作原理
- ChatGPT 的使用技巧
  - 如何让 ChatGPT 回答得更好
  - 如何让 ChatGPT 发挥更大的作用
  - 如何使用 OpenAI API 来提高工作效率

## 这篇文档的主要内容是什么

- 关键概念
  - Prompts（提示词、输入文本）
  - Token（符号）：`1 Token ~= 4 字母 ~= 0.75 单词`
  - Models（模型）：GPT-3.5-Turbo

- ChatGPT 能够做什么：（补全文字）
  - 内容生成
  - 代码生成
  - 总结
  - 解释
  - 对话
  - 创造性写作
  - 风格转换

- 使用好的提示词
  - 添加一些例子

- 修改配置
  - temperature：数值越高，回答越多样化

  ```text
  Use "temperature" value of 1 in our conversation.
  Use "deversity_penalty" value of 0.9 in our conversation.
  Use "presence_penalty" value of 0.2 in our conversation.
  Use "frequency_penalty" value of 1.5 in our conversation.
  Use "generate_breaks" value of 1.2 in our conversation.
  Use "Top-p" value of 0.1 in our conversation.
  ```

- 调用 API
  - 在 `.env` 添加 `OPENAI_API_KEY` 环境变量
  - 在 Node.js 中，可以通过 `openai.createCompletion` 来调用 API
