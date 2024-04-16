# MQTT & MQTT 5 Essentials 阅读笔记

## Message Filtering

- Message Filtering Options
  - Option 1: Subject-based filtering (Topic)
  - Option 2: Content-based filtering
  - Option 3: Type-based filtering

- 2 tips
  - For subject-based filtering, both publisher and subscriber need to know which topics to use.
  - Keep in mind the message delivery. The publisher can’t assume that somebody is listening to the messages that are sent.
    In some instances, it is possible that no subscriber reads a particular message.

## Topics & Best Practices

- 2 different kinds of wildcards
  - single-level: `+`
  - multi-level": `#`

- The $-symbol topics are reserved for internal statistics of the MQTT broker

- Best Practices
  - Never use a leading forward slash
  - Never use spaces in a topic
  - Keep the topic short and concise
  - Use only ASCII characters, avoid non printable characters

## Retained Message

- A retained message makes sense when you want newly-connected subscribers to receive messages immediately.

## 参考资料

- [MQTT Getting started][1]

  [1]: https://mqtt.org/getting-started/
