# Windows 系统使用笔记

- 使用 wmic 查看进程详细信息

```sh
wmic process where "name='chrome.exe'" get ProcessId,ExecutablePath,CommandLine
wmic process where "name like '%python.exe%'" get ProcessId,ExecutablePath,CommandLine
```
