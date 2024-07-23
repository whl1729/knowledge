# Python API 使用笔记

- `threading.Thread`
  - 创建线程时，如果只需要传入一个参数 `foo`，那么写成 `args=[foo]` 或者 `args=(foo,)`
  - 如果使用第二种写法，**一定不要忘记后面的逗号**，否则会报错，甚至出现线程没创建成功但也没报错的奇葩现象！

- `time.sleep`
  - 3.11 版本以后提高了时间精度，3.11 以前的版本可以考虑使用 `win32event.WaitForSingleObject`

  ```python
  # try to import win32event for event-based cyclic send task (needs the pywin32 package)
  USE_WINDOWS_EVENTS = False
  try:
      import pywintypes
      import win32event

      # Python 3.11 provides a more precise sleep implementation on Windows, so this is not necessary.
      # Put version check here, so mypy does not complain about `win32event` not being defined.
      if sys.version_info < (3, 11):
          USE_WINDOWS_EVENTS = True
  except ImportError:
      pass
  ```
