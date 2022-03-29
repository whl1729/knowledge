# MySQL 使用笔记

## Common Commands

### Table

- 重命名某一列

  ```sql
  ALTER TABLE tbl_name
  RENAME COLUMN old_col_name to new_col_name
  ```

- 在特定位置添加新的列
  - 注：下面的`column_definition`指的是类型和约束等，比如`int not null`

  ```sql
  ALTER TABLE tbl_name
  MODIFY COLUMN col_name column_definition
  [FIRST | AFTER col_name]
  ```

### Index

- 创建索引

  ```sql
  /* 直接给数据表创建索引 */
  CREATE INDEX index_name ON TABLE tbl_name (key_part, ...)

  /* 在创建表的同时创建索引 */
  CREATE TABLE tbl_name
  (
    col_name data_type,
    ...
    {INDEX | KEY} index_name (key_part, ...)
  )

  /* 修改表时创建索引 */
  ALTER TABLE tbl_name ADD {INDEX | KEY} index_name (key_part, ...)
  ```

- 删除索引

  ```sql
  DROP INDEX index_name ON tbl_name
  ```

- 查看索引

  ```sql
  SHOW INDEX FROM tbl_name
  ```

## MySQL Internal

- 查看 MySQL 数据保存位置

  ```sql
  SELECT @@DATADIR;
  ```

## Import data

- 命令行下可以使用[mysqlimport][4]来导入数据。
  - 文件名去掉后缀后跟表名保持一致。
  - 文件中值为 NULL 的数据使用`\N`来表示。

  ```mysql
  mysqlimport --ignore-lines=1 \
              --fields-terminated-by=, \
              --local -u root \
              -p DatabaseName \
              TableName.csv
  ```

- mysql-cli 里面可以使用`LOAD DATA`语句导入数据。

  ```mysql
  LOAD DATA
  INFILE 'file_name'
  INTO TABLE 'tbl_name'
  [FIELDS TERMINATED BY 'string']
  [LINES TERMINATED BY 'string']
  [IGNORE number {LINES | ROWS}]
  ```

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
  [4]: https://dev.mysql.com/doc/refman/8.0/en/mysqlimport.html