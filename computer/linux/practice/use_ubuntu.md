# Ubuntu 系统使用笔记

- 在 Ubuntu 中配置开机自启动 bash 脚本（以 `cyber-dail-news` 为例）
  - 在 `/etc/systemd/system` 目录下创建新文件 `cyber-daily-news.service`，并添加以下内容
  
  ```bash
  [Unit]
  Description=Cyber Daily News
  After=network.target

  [Service]
  Type=forking
  ExecStart=/home/along/src/cyber-daily-news/script/start.sh
  Restart=on-failure
  RestartSec=10
  StartLimitIntervalSec=60
  StartLimitBurst=5

  [Install]
  WantedBy=multi-user.target
  ```

  - `sudo systemctl daemon-reload`
  - `sudo systemctl restart cyber-daily-news.service`

- [在 Ubuntu 系统访问 Windows 共享目录][2]

  ```sh
  sudo mount -t cifs //IP_ADDRESS/FOLDER_NAME /mnt/windows -o username=USERNAME,password=PASSWORD
  ```

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
  [2]: https://www.javatpoint.com/how-to-access-windows-shared-folder-from-ubuntu
