# [Techniques to improve reliability][1] 分析笔记

## 这篇文档的主题是什么

介绍如何提高 ChatGPT 解决复杂问题的可靠性

## 目前为止我知道什么

- 要想提高 ChatGPT 回答质量，提示词的设计十分重要。
- 提示词设计的一些技巧包括
  - 清楚描述期望的输出格式
  - 提供示例
  - 要求模型一步一步地思考，或者要求模型同时考虑正面和反面
  - 告诉模型在不确定时回答不知道，避免胡说八道
  - 检查提示词，确保没有语法错误和逻辑错误等
  - 正确设置 temperature 和 top_p 参数

## 目前为止我不知道什么

- 提示词设计的更多技巧

## 这篇文档的主要内容是什么

- 提示词加入 `Let's think step by step`
  - 适用于数学问题（多步计算、符号推理、统计和其他推理问题）
  - 解决难题的一个办法是将其分解成若干个子问题

- 提高 ChatGPT 解决复杂问题的可靠性的方法
  - 提供更清晰的命令
  - 将复杂任务拆解为若干个更简单的子任务
  - 将命令结构化（Structure the instruction to keep the model on task）
  - 要求模型在回答前给出解释
  - 要求模型对各种可能的答案进行分析，然后综合整理出答案
  - 生成多个输出，然后让模型选出最佳答案
  - 微调自定义模型以使性能最优（Fine-tune custom models to maximize performance）

- 将复杂任务拆解为若干个更简单的子任务
  - 提示词增加解题思路或解题方法论，要求模型按照这个思路或方法论来回答问题

- 要求模型在回答前给出解释
  - Zero-shot: `Let's think step by step` 或其变体（针对特定场景进行细化）
  - Few-shot: 提供一些例子（推理链）

  ```text
  First, think step by step about why X might be true.
  Second, think step by step about why Y might be true.
  Third, think step by step about whether X or Y makes more sense.
  ```

  [1]: https://github.com/openai/openai-cookbook/blob/main/techniques_to_improve_reliability.md
