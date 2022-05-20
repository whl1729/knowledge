# docker 使用笔记

- [解决由于权限不足导致执行 `docker images` 报错的问题][1]

  ```bash
  along:~$ docker images

  Got permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock:
  Get "http://%2Fvar%2Frun%2Fdocker.sock/v1.24/images/json": dial unix /var/run/docker.sock: connect: permission denied
  ```

  ```bash
  # Solution:
  sudo setfacl --modify user:<user name or ID>:rw /var/run/docker.sock
  ```

  [1]: https://stackoverflow.com/a/54504083
