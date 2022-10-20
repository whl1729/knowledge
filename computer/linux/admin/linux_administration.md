# Linux 系统管理

## 账号管理

- `adduser` vs `useradd`
  - `useradd` is a low level utility for adding users. On Debian, administrators should usually use `adduser` instead. (from manpage)
  - `useradd` 不会自动创建 HOME 目录；`adduser` 会自动创建 HOME 目录，并且还会提示你设置密码及基本信息，用户友好度更高。

- 切换用户
  - `sudo -iu <username>`

- 修改用户默认 shell
  - `usermod -s <shell-absolute-path>`

## 参考资料

- [Linux Foundation Referenced Specifications][1]
- [UNIX and Linux System Administration Handbook, Fifth Edition][2]

  [1]: https://refspecs.linuxfoundation.org/
  [2]: https://admin.com/
