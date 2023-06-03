# Prompt Engineering Guide 分析笔记

## 这个文档的主要内容是什么

### 简介

- 提示词的组成
  - 命令
  - 上下文
  - 输入数据
  - 输出格式

- 提示词的两种格式
  - `<Question>?`
  - `<Instruction>`

- zero-shot prompting
  - 没有例子

  ```text
  Q: <Question>?
  A:
  ```

- few-shot prompting
  - 提供一些例子
  - 不一定要使用 QA 格式

  ```text
  Q: <Question>?
  A: <Answer>
  Q: <Question>?
  A: <Answer>
  Q: <Question>?
  A: <Answer>
  Q: <Question>?
  A:
  ```

- 提示词设计的通用 Tips
  - 从简单入手，不停迭代
  - 命令
    - Explain, Write, Classify, Summarize, Translate, Order, etc
    - 将命令放在开头，或者使用 "###" 之类的分隔符来区分指令和上下文
  - 将大任务分解成若干个更简单的子任务
  - 特异性、简洁性、准确性
  - 说「做什么」，不要说「不要做什么」

- 任务类型
  - 文本概括
  - 信息提取
  - 回答问题
  - 文本分类
  - 对话
  - 代码生成
  - 推理

- 技巧
  - Zero-shot Prompting （没有示例）
  - Few-shot Prompting（提供若干个示例）
  - Chain-of-Thought Prompting （提供分析过程）

### 好的提示词示例

#### 概括文本

要求输出符合一定的格式：

```text
Extract the name of places in the following text.
Desired format:
Place: <comma_separated_list_of_company_names>
Input: "Although these developments are encouraging to researchers, much is still a mystery.
 “We often have a black box between the brain and the effect we see in the periphery,” says Henrique Veiga-Fernandes, a neuroimmunologist at the Champalimaud Centre for the Unknown in Lisbon.
  “If we want to use it in the therapeutic context, we actually need to understand the mechanism.""
```

简洁清晰地表达需求：（2到3个句子、高中生能看看懂的水平）

```text
Use 2-3 sentences to explain the concept of prompt engineering to a high school student.
```

```text
Explain antibiotics
A:
```

#### 提取信息

```text
(A paragraph)
Mention the large language model based product mentioned in the paragraph above:
```

#### 回答问题

```text
Answer the question based on the context below. Keep the answer short and concise. Respond "Unsure about answer" if not sure about the answer.
```

#### 生成代码

```text
/*
Ask the user for their name and say "Hello"
*/
```

```text
Table departments, columns = [DepartmentId, DepartmentName]
Table students, columns = [DepartmentId, StudentId, StudentName]
Create a MySQL query for all students in the Computer Science Department
```
