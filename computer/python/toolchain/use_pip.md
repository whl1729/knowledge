# pip 使用笔记

- 查看安装失败的 package 被谁依赖
  - 查看报错日志里 `from xxx` 的信息即可，比如：`Collecting PyYAML<6,>=3.10 (from docker-compose==1.29.2->-r requirements.txt (line 2))`

- pip 使用清华源
  - 临时使用清华源

  ```sh
  pip install <some-package> -i https://pypi.tuna.tsinghua.edu.cn/simple
  ```

  - 全局持续使用清华源
    - 方法1：`pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple`
    - 方法2：在 `~/.pip/pip.conf` 文件中新增以下配置
  
  ```conf
  [global]
  index-url = https://pypi.tuna.tsinghua.edu.cn/simple
  [install]
  trusted-host = https://pypi.tuna.tsinghua.edu.cn
  ```
