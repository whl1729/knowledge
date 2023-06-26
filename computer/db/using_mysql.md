# MySQL 使用笔记

## FAQs

- Solve the error when connecting mysqld: `ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)`
  - add `--protocol=tcp` option.

- Solve the error when connecting mysqld: `ERROR 2026 (HY000): SSL connection error: unknown error number`
  - add `--ssl-mode=DISABLED` option. E.g. `mysql -h 172.31.0.2 -P 3401 -u maker-test -p --ssl-mode=DISABLED maker-test`

- When connecting to mysqld with non-default port, the host is required.

## Basic Knowledge

### Data Type

- Boolean data type
  - MySQL does not have a boolean (or bool) data type.
  - Instead, it converts boolean values into integer data types (`TINYINT`).
  - When you create a table with a boolean data type, MySQL outputs data as 0, if false, and 1, if true.

## Common Commands

### Account Management

- 创建用户

  ```sql
  CREATE USER 'newuser'@'localhost' IDENTIFIED BY 'newpassword';
  GRANT ALL PRIVILEGES ON * . * TO 'newuser'@'localhost';
  FLUSH PRIVILEGES;
  ```

- 删除用户

  ```sql
  DROP USER 'newuser'@'localhost';
  ```

- 查看用户

  ```sql
  USE mysql;

  -- show all users
  SELECT user from user;

  -- show current user
  SELECT USER();
  ```

- 切换用户

  ```mysql
  system mysql -u newuser -p
  ```

### Database

- 显示所有数据库

  ```sql
  SHOW DATABASES;
  ```

- 显示当前数据库

  ```sql
  SELECT DATABASE();
  ```

- 创建数据库

  ```sql
  CREATE DATABASE db_name;
  ```

- 使用数据库

  ```sql
  USE db_name;
  ```

### Table

- 显示表

  ```sql
  SHOW TABLES;
  ```

- 显示表的字段

  ```sql
  DESCRIBE tbl_name
  ```

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

- 删除一行

  ```sql
  DELETE FROM tbl_name
  WHERE id=1;
  ```

- 删除表

  ```sql
  DROP TABLE tbl_name;
  ```

- 查看外键

  ```sql
  SELECT
    TABLE_NAME,
    COLUMN_NAME,
    CONSTRAINT_NAME,
    REFERENCED_TABLE_NAME,
    REFERENCED_COLUMN_NAME
  FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
  WHERE
    REFERENCED_TABLE_NAME = 'My_Table';
  ```

### Select

- 去重

  ```sql
  SELECT DISTINCT c1, c2, c3 FROM t1;
  ```

- 限制条目数量

  ```sql
  SELECT * FROM tbl LIMIT 5;  # Retrieve first 5 rows
  ```

- [统计条目数量][5]

  ```sql
  SELECT COUNT(*) FROM pet;
  SELECT owner, COUNT(*) FROM pet GROUP BY owner;
  ```

- 筛选非空字符串

  ```sql
  SELECT * from devices WHERE mac is not NULL;  # 不能用 != NULL
  SELECT * from devices WHERE mac != "";
  ```

### Update

- 命令格式

  ```sql
  UPDATE [LOW_PRIORITY] [IGNORE] table_reference
      SET assignment_list
      [WHERE where_condition]
      [ORDER BY ...]
      [LIMIT row_count]

  value:
      {expr | DEFAULT}

  assignment:
      col_name = value

  assignment_list:
      assignment [, assignment] ...
  ```

- 更新 datetime 字段
  - MySQL recognizes DATETIME and TIMESTAMP values as a string in either 'YYYY-MM-DD hh:mm:ss' or 'YY-MM-DD hh:mm:ss' format.

  ```sql
  UPDATE products SET former_date='2011-12-18 13:17:17' WHERE id=1
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
  [5]: https://dev.mysql.com/doc/refman/8.0/en/counting-rows.html
