# Ubuntu 系统使用笔记

- [CDPATH: 为 cd 命令定义基础目录][1]

  ```sh
  export CDPATH=.:~:/etc:/var
  ```

- WSL Ubuntu 使用 Windows socks5 代理
  - 需要在 Shadowsocks 图标右键点击「允许其他设备连入」

- WSL Ubuntu access Windows network
  - Obtain the IP address of your host machine: cat /etc/resolv.conf
  - Copy the IP address following the term: nameserver
  - Connect to any Windows server using the copied IP address

> 备注：我的 WSL2 Ubuntu 无法以上述 IP 地址（172.20.16.1）来访问 Windows 端口，
> 但可以 Windows 系统的 WLAN IP 地址（192.168.14.185）来访问 Windows 端口。

  [1]: https://linux.101hacks.com/cd-command/cdpath/
