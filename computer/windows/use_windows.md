# Windows 系统使用笔记

- Windows 查看可执行文件的路径：`(get-command git.exe).Path`

- Windows 安装和配置 OpenSSH 服务器
  - [适用于 Windows 的 OpenSSH 入门][2]
  - [Setting up OpenSSH for Windows using public key authentication][3]
  - [为 Windows 中的 OpenSSH 配置默认 shell][4]

- [Running curl via powershell][1]
  - Use `curl.exe` instead of `curl`
  - In PowerShell `curl` is a built in alias to `Invoke-WebRequest` cmdlet

- Install Docker Desktop on Windows 10
  - Install WSL and Ubuntu

> 一开始我先安装 Docker Desktop，后安装 WSL 和 Ubuntu，结果 Ubuntu 无法正常使用 docker 命令。
> 后来卸载重装 Docker Desktop，问题解决。因此，应该先安装 WSL 再 Docker Desktop。

- Install WSL on Windows 10
  - Install Ubuntu from Windows store
  - Enable Virtualization in BIOS

- 使用 wmic 查看进程详细信息

```sh
wmic process where "name='chrome.exe'" get ProcessId,ExecutablePath,CommandLine
wmic process where "name like '%python.exe%'" get ProcessId,ExecutablePath,CommandLine
```

## Windows 系统推荐安装的工具

- Everything

- [Ventoy][5]: 新一代多系统启动U盘解决方案

- 管培喆推荐的电影下载工具
  - [jxxghp-nas-tools][6]: 影视资源整合
  - [qBittorrent - A BitTorrent client in Qt][7]: 影视资源下载
  - [jellyfin][8]: 在线观看

## Windows terminal

- 关闭光标闪烁
  - 打开「控制面板」-「键盘」-「光标闪烁速度」，将其设置为「无」即可。

- 解决 git bash 中文乱码的问题
  - 修改「设置」-「Git bash」-「命令行」，在后面加上 `--login -i` 的选项，然后「保存」即可。

  [1]: https://stackoverflow.com/questions/30807318/running-curl-via-powershell-how-to-construct-arguments
  [2]: https://learn.microsoft.com/zh-cn/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui
  [3]: https://stackoverflow.com/a/50502015/11467929
  [4]: https://learn.microsoft.com/zh-cn/windows-server/administration/openssh/openssh_server_configuration#configuring-the-default-shell-for-openssh-in-windows
  [5]: https://www.ventoy.net/cn/
  [6]: https://github.com/carolcoral/jxxghp-nas-tools
  [7]: https://github.com/qbittorrent/qBittorrent
  [8]: https://github.com/jellyfin/jellyfin
