# curl 使用指南

- curl 发带有参数的 GET 请求时，需要将 url 部分用单/双引号括起来，否则无法正常传递参数。

- Download the contents of a URL to a file:

  ```sh
  curl http://example.com --output path/to/file
  ```

- Download a file, saving the output under the filename indicated by the URL:

  ```sh
  # -O, --remote-name: Write output to a local file named like the remote file we get.
  curl --remote-name http://example.com/filename
  ```

- Upload a file

  ```sh
  curl -F "user=foo" -F "token=bar" -F "image=@/home/user1/Desktop/test.jpg" localhost/uploader.php
  ```

- Send form-encoded data (POST request of type application/x-www-form-urlencoded). Use --data @file_name or --data @'-' to read from STDIN:

  ```sh
  # -d, --data <data>
  curl -d 'name=bob' http://example.com/form
  ```

- Send a request with an extra header, using a custom HTTP method:

  ```sh
  # -H, --header <header/@file>
  # -X, --request <command>
  curl -H 'X-My-Header: 123' -X PUT http://example.com
  ```

- Send data in JSON format, specifying the appropriate content-type header:

  ```sh
  curl -H 'Content-Type: application/json' -d '{"name":"bob"}' http://example.com/users/1234
  ```

- Pass a username and password for server authentication:
  
  ```sh
  # -u, --user <user:password>
  curl -u myusername:mypassword http://example.com
  ```

- Pass client certificate and key for a resource, skipping certificate validation:

  ```sh
  # -E, --cert <certificate[:password]>
  # -k, --insecure
  curl -E client.pem --key key.pem -k https://example.com
  ```
