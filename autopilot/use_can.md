# CAN 协议使用笔记

## CAN Specification

- 远程帧
  - 远程帧是一种特殊的CAN帧，用于请求其他节点发送对应的数据帧。它不包含数据字段，仅包含标识符（Identifier）和数据长度代码（DLC）。
  - 发送远程帧的节点希望获取某个特定标识符的数据，因此它使用与该数据帧相同的标识符发送远程帧。

```text
By sending a REMOTE FRAME a node requiring data may request another node to
send the corresponding DATA FRAME. The DATA FRAME and the corresponding
REMOTE FRAME are named by the same IDENTIFIER.
```

## 参考资料

- [CAN Specification][4]

- [周立功CAN总线技术干货知识库][3]

- [CANFD每秒最多可以发送多少帧报文？][2]

- [CAN 字节序：Inter、Motorola forward LSB、Motorola forward MSB][1]

  ![can_byte_order](./images/can_byte_order.jpg)

  [1]: https://www.race-technology.com/wiki/index.php/CANInterface/ByteOrdering
  [2]: https://mp.weixin.qq.com/s/VwFUit2CY8SFY9Xo5Vll8Q
  [3]: https://mp.weixin.qq.com/s/aM8hdcnOqvHBwE2ZxOOttg
  [4]: http://esd.cs.ucr.edu/webres/can20.pdf
