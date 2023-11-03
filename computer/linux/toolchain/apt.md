# apt 使用笔记

## Use mirror

1. 先将 `/etc/apt/sources.list` 备份
2. 备份后，将此文件里面的所有`archive.ubuntu.com` 和 `security.ubuntu.com` 均替换为以下任一镜像。

```text
http://mirrors.aliyun.com/ubuntu/
https://mirrors.tuna.tsinghua.edu.cn/ubuntu/
https://mirrors.ustc.edu.cn/ubuntu/
http://mirrors.163.com/ubuntu/
```

## Use a socks5 proxy for `apt` on Ubuntu 20.04 (by ChatGPT)

To use a SOCKS proxy for `apt` on Ubuntu 20.04, you typically use a program like `tsocks` or `proxychains` to enforce the SOCKS proxy settings on `apt`.
Here's how to set it up using `proxychains`:

1. **Install `proxychains`**:

   ```bash
   sudo apt update
   sudo apt install proxychains
   ```

2. **Configure `proxychains`**:

   Open the `proxychains` configuration file in your preferred text editor (we'll use `nano` here):

   ```bash
   sudo nano /etc/proxychains.conf
   ```

   Find the line(s) that start with `socks4` or `socks5`. Comment them out if you don't need them. Then, add your SOCKS proxy details.
   For example, if you have a SOCKS5 proxy running on `127.0.0.1` at port `1080`, add the following line:

   ```text
   socks5  127.0.0.1 1080
   ```

   Save the file and exit the text editor.

3. **Use `proxychains` with `apt`**:

   When you want to use `apt` with the SOCKS proxy, prepend your command with `proxychains`. For example:

   ```bash
   sudo proxychains apt update
   sudo proxychains apt install <package-name>
   ```

Remember that using a SOCKS proxy can slow down the connection, depending on the proxy's quality and location.
