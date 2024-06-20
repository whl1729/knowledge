# [Prompt Engineering Guide][1] 分析笔记

## 大纲

### 英文版

- Six strategies for getting better results
  - Write clear instructions
    - Include details in your query to get more relevant answers
    - Ask the model to adopt a persona
    - Provide examples
    - Use delimiters to clearly indicate distinct parts of the input
    - Specify the steps required to complete a task
    - Specify the desired length of the output
  - Provide reference text
    - Instruct the model to answer using a reference text
    - Instruct the model to answer with citations from a reference text
  - Split complex tasks into simpler subtasks
    - Use intent classification to identify the most relevant instructions for a user query
    - For dialogue applications that require very long conversations, summarize or filter previous dialogue
    - Summarize long documents piecewise and construct a full summary recursively
  - Give the model time to "think"
    - Instruct the model to work out its own solution before rushing to a conclusion
    - Use inner monologue or a sequence of queries to hide the model's reasoning process
    - Ask the model if it missed anything on previous passes
  - Use external tools
    - Use embeddings-based search to implement efficient knowledge retrieval
    - Use code execution to perform more accurate calculations or call external APIs
    - Give the model access to specific functions
  - Test changes systematically
    - Evaluate model outputs with reference to gold-standard answers

### 中文版（由 ChatGPT 翻译）

- 获得更好结果的六种策略
  - 写清楚的指令
    - 在查询中包含详细信息以获得更相关的答案
    - 提供示例
    - 使用分隔符明确指示输入的不同部分
    - 让模型采用特定角色
    - 指定完成任务所需的步骤
    - 指定输出的期望长度
  - 提供参考文本
    - 指示模型使用参考文本回答
    - 指示模型在回答中引用参考文本
  - 将复杂任务拆解为简单子任务
    - 使用意图分类识别最相关的用户查询指令
    - 对于需要长时间对话的对话应用，汇总或过滤之前的对话
    - 分段汇总长文档并递归构建完整摘要
  - 给模型时间“思考”
    - 指示模型在得出结论前自行解决问题
    - 使用内心独白或一系列查询隐藏模型的推理过程
    - 询问模型在之前的操作中是否遗漏了什么
  - 使用外部工具
    - 使用基于嵌入的搜索实现高效知识检索
    - 使用代码执行进行更准确的计算或调用外部API
    - 赋予模型访问特定功能的权限
  - 系统性地测试更改
    - 参考黄金标准答案评估模型输出

> 记忆：我认为策略1和策略4最重要。
>
> 策略1的记忆方法：3点关于输入（细节、示例、分隔符），3点关于输出（角色、步骤、长度）
>
> 策略4的记忆方法：自行解决、检验

  [1]: https://platform.openai.com/docs/guides/prompt-engineering
