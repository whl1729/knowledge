# JSON 使用笔记

- JSON 不支持十六进制格式

  ```python
  >>> import json
  >>> json.loads('{"name": "guojing", "age": 0x20}')  
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    File "C:\Users\minieye\AppData\Local\Programs\Python\Python38\lib\json\__init__.py", line 357, in loads
      return _default_decoder.decode(s)
    File "C:\Users\minieye\AppData\Local\Programs\Python\Python38\lib\json\decoder.py", line 337, in decode
      obj, end = self.raw_decode(s, idx=_w(s, 0).end())
    File "C:\Users\minieye\AppData\Local\Programs\Python\Python38\lib\json\decoder.py", line 353, in raw_decode
      obj, end = self.scan_once(s, idx)
  json.decoder.JSONDecodeError: Expecting ',' delimiter: line 1 column 29 (char 28)
  ```
