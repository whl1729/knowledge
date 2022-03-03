# MySQL 使用笔记

## Installation

- [Install mysql-server][1]

  ```sh
  sudo apt-get install mysql-server
  ```

- [Install mysql-workbench][2]

  ```sh
  sudo dpkg -i mysql-workbench-community-xxx.deb
  sudo apt-get install -f
  sudo dpkg -i mysql-workbench-community-xxx.deb
  ```

## MySQL Server

- 安装完 mysql server 后， MySQL 服务器会自动启动。

- 可以通过`systemctl`来管理 MySQL 服务

  ```sh
  systemctl {start|stop|restart|status} mysql
  ```

- 创建新用户并连接 MySQL Server
  - 参考[How To Create a New User and Grant Permissions in MySQL][3]
  - 首先以 root 用户连接到 MySQL Server: `sudo mysql -u root -p`
  - 然后使用以下命令创建新用户：

  ```sql
  CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'newpassword';
  GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
  FLUSH PRIVILEGES;
  ```

  [1]: https://dev.mysql.com/doc/refman/8.0/en/linux-installation.html
  [2]: https://dev.mysql.com/downloads/workbench/
  [3]: https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql
