# docker 使用笔记

- 查看镜像日志：`docker logs <container-name>`

## docker compose

- 端口映射
  - docker compose 的 ports 参数可以用来配置端口映射 `-${HOST_PORT}:${CONTAINER_PORT}`
  - 但是需要注意，你配置的容器映射的端口，与你容器所运行的服务监听的端口，是两回事
  - 举个例子，MySQL 容器，你配置了 `3411:3306`，同时环境变量 `MYSQL_TCP_PORT` 配置为 3411，那么该容器监听的端口是 3411

- 环境变量文件
  - 如果 `docker-compose.yml` 所在目录下含有 `.env` 文件，那么执行 `docker compose` 时会默认加载此文件
  - 如果想修改加载的文件名，可以使用以下命令：`docker compose -f docker-compose.yml --env-file .env.test up`

## Dockerfile

- `LABEL` 指令的一个用途：为中间镜像指定一个 LABEL，方便后面根据 LABEL 清理中间镜像。
  - 举例，若在 Dockerfile 里面为中间镜像指定了 `LABEL stage=build`，
    那么可以使用 `docker image prune --filter label=stage=build -f` 将其清除。

### Dockerfile 易忘命令

- COPY
  - `<dest>` 可以是容器内的绝对路径，也可以是相对于工作目录的相对路径（工作目录可以用 WORKDIR 指令来指定）。
  - 目标路径不需要事先创建，如果目录不存在会在复制文件前先行创建缺失目录。
  - 如果源路径为文件夹，复制的时候不是直接复制该文件夹，而是将文件夹中的内容复制到目标路径。

  ```docker
  COPY [--chown=<user>:<group>] <src>... <dest>
  COPY [--chown=<user>:<group>] ["<src>",... "<dest>"]
  ```

## 常见问题

- `docker pull` 报错：`access denied, repository does not exist or may require 'docker login'`
  - 大概率是镜像地址填写有误。

  ```bash
  $ docker pull asdfgh
  Using default tag: latest
  Error response from daemon: pull access denied for asdfgh, repository does not exist or may require 'docker login':
  denied: requested access to the resource is denied
  ```

- alpine 镜像中运行 elf 报错：`/bin/sh: /docker-gs-ping-roach: not found`
  - 使用 ldd 命令查看 elf 文件的依赖库，发现其中依赖 libc，而 alpine 不包含 libc，导致无法运行 elf。
  - 可以在 Dockerfile 里面增加 `apk add gcompat` 来安装 glibc。（参考[stack overflow][5]）

  ```bash
    / # ldd docker-gs-ping-roach
    /lib64/ld-linux-x86-64.so.2 (0x7fd94dd0b000)
    libpthread.so.0 => /lib64/ld-linux-x86-64.so.2 (0x7fd94dd0b000)
    libc.so.6 => /lib64/ld-linux-x86-64.so.2 (0x7fd94dd0b000)
  ```

- `docker build` 偶尔报错 `net/http: TLS handshake timeout` 的解决方案
  - 这是网络不稳定导致的，可以编写 bash 脚本不断循环 build 直至成功。

  ```bash
  for i in {0..1000}; do docker build; if (($? == 0)); then break; fi done
  ```

- [配置 docker hub 镜像][4]
  - 检查 `/lib/systemd/system/docker.service` 的 `ExecStart=` 的值，如果含有 `--registry-mirror` 参数，则将此参数及其值删除。
  - 在 `/etc/docker/daemon.json` 中添加如下内容（若文件不存在则新建之）：

  ```json
  {
    "registry-mirrors": [
      "https://hub-mirror.c.163.com",
      "https://mirror.baidubce.com"
    ]
  }
  ```

  - 重新启动服务。

  ```bash
  sudo systemctl daemon-reload
  sudo systemctl restart docker
  ```

- 安装 docker
  - [Docker 官方文档][2] 默认让用户安装 Docker Desktop，如果你不想使用桌面版，可以只安装 [Docker Engine][3]。

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
  [2]: https://docs.docker.com/desktop/
  [3]: https://docs.docker.com/engine/install/
  [4]: https://yeasy.gitbook.io/docker_practice/install/mirror
  [5]: https://stackoverflow.com/a/68284294
