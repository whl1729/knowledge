# USB 虚拟网络

本文研究USB虚拟网络的工作原理。
具体而言，我们将依次讨论以下问题：

- USB是什么？
- USB是如何传输信号的？
- USB接口是如何虚拟成网络的？

## USB是什么？

- USB(Universal Serial Bus) 是一个工业标准，
  它制定了连接计算机系统与外部设备的线缆、连接器、连接协议、通信协议及电源供应的规范。

> Universal Serial Bus (USB) is an industry standard that establishes specifications for cables, connectors and protocols for connection, communication and power supply (interfacing) between computers, peripherals and other computers. -- wiki

- USB设备
  - 14种连接器，其中最常用的是USB-C。
  - 鼠标
  - 键盘
  - U盘

## USB是如何传输信号的？

USB线如同一条公路，可以用来传输数字信号。
但也仅此而已，USB线本身不会控制信号的传输，也不关注它传输的是啥东西。
控制信号传输过程的，应该是USB驱动。

### USB传输信号需要哪些东西

- USB线
- USB 主控制器（USB host controller）
- 操作系统
  - Linux内核含有USB core
- USB驱动程序

## USB接口是如何虚拟成网络的？

## 参考资料

- [Wiki: USB](https://en.wikipedia.org/wiki/USB)
- [The GNU/Linux "usbnet" Driver Framework](http://www.linux-usb.org/usbnet/)
- [Wiki: Network Interface Controller](https://en.wikipedia.org/wiki/Network_interface_controller)
