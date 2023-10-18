# Windows 系统使用笔记

- Install Docker Desktop on Windows 10
  - Install WSL and Ubuntu

- Install WSL on Windows 10
  - Install Ubuntu from Windows store
  - Enable Virtualization in BIOS

- 使用 wmic 查看进程详细信息

```sh
wmic process where "name='chrome.exe'" get ProcessId,ExecutablePath,CommandLine
wmic process where "name like '%python.exe%'" get ProcessId,ExecutablePath,CommandLine
```

## Windows terminal

- 关闭光标闪烁
  - 打开「控制面板」-「键盘」-「光标闪烁速度」，将其设置为「无」即可。

- 解决 git bash 中文乱码的问题
  - 修改「设置」-「Git bash」-「命令行」，在后面加上 `--login -i` 的选项，然后「保存」即可。

