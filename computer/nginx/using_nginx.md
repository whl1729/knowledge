# Nginx 使用笔记

## 配置 Nginx

- 将 http 请求重定向到 https
  - 这种配置方法可以将所有 method 都重定向

  ```text
  server {
    listen 80;
    server_name pa-test.minieye.tech;
    return 301 https://$host$1;
  }
  ```

## 安装 Nginx

按照[官方安装教程][1]进行安装即可。

## 启动 Nginx

在 Ubuntu 20.04 安装 Nginx 后，执行`nginx`会报以下错误：

```bash
along:~$ nginx
nginx: [alert] could not open error log file: open() "/var/log/nginx/error.log" failed (13: Permission denied)
2022/05/08 11:50:01 [warn] 112291#112291: the "user" directive makes sense only if the master process runs with super-user privileges, ignored in /etc/nginx/nginx.conf:2
2022/05/08 11:50:01 [emerg] 112291#112291: mkdir() "/var/cache/nginx/client_temp" failed (13: Permission denied)
```

改用`sudo nginx`后不会报错，并且使用`ps -elf | grep nginx`可以看到1个 nginx master process 和8个 nginx work process。

```bash
along:~$ ps -elf | grep nginx
1 S root      112783    2400  0  80   0 -  2191 -      11:56 ?        00:00:00 nginx: master process nginx
5 S nginx     112784  112783  0  80   0 -  2353 -      11:56 ?        00:00:00 nginx: worker process
5 S nginx     112785  112783  0  80   0 -  2353 -      11:56 ?        00:00:00 nginx: worker process
5 S nginx     112786  112783  0  80   0 -  2353 -      11:56 ?        00:00:00 nginx: worker process
5 S nginx     112787  112783  0  80   0 -  2353 -      11:56 ?        00:00:00 nginx: worker process
5 S nginx     112788  112783  0  80   0 -  2353 -      11:56 ?        00:00:00 nginx: worker process
5 S nginx     112789  112783  0  80   0 -  2353 -      11:56 ?        00:00:00 nginx: worker process
5 S nginx     112790  112783  0  80   0 -  2353 -      11:56 ?        00:00:00 nginx: worker process
5 S nginx     112791  112783  0  80   0 -  2353 -      11:56 ?        00:00:00 nginx: worker process
```

  [1]: https://nginx.org/en/docs/install.html
