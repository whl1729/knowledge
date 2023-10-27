# pip 使用笔记

- pip 使用清华源
  - 临时使用清华源

  ```sh
  pip install <some-package> -i https://pypi.tuna.tsinghua.edu.cn/simple
  ```

  - 全局持续使用清华源
    - 在 `~/.pip/pip.conf` 文件中新增以下配置
  
  ```conf
  [global]
  index-url = https://pypi.tuna.tsinghua.edu.cn/simple
  [install]
  trusted-host = https://pypi.tuna.tsinghua.edu.cn
  ```
