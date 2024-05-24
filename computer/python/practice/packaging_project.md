# Python 项目打包

## `setup.py` 文件示例

- [A sample Python project][2]
  - [setup.py example][3]

## 如何支持 pip git+ 安装

如果你不想将你的Python库上传到PyPI，而希望通过GitLab仓库地址直接安装，你可以使用`pip`的`git+`协议来安装。这种方法通常用于开发过程中，或者当你想要安装一个尚未发布到PyPI的库时。
为了允许他人通过`pip install`从GitLab仓库安装你的库，你需要确保你的仓库包含一个`setup.py`文件，这个文件定义了如何安装你的库。以下是步骤：

1. **配置`setup.py`**:
   确保你的仓库中有一个`setup.py`文件，它包含了安装你的库所需的信息。这个文件应该定义你的库的名称、版本、作者、描述等。请参考上面的示例来创建`setup.py`。
2. **更新`README.md`和`LICENSE`**:
   你的仓库应该包含一个`README.md`文件，描述你的库以及如何安装和使用它。同时，确保你有一个`LICENSE`文件，定义了你的库的使用许可。
3. **（可选）创建`requirements.txt`**:
   如果你的库依赖于其他Python包，你可以创建一个`requirements.txt`文件，列出所有依赖项。
4. **使用`pip`安装**:
   用户可以通过以下命令从GitLab仓库安装你的库：

   ```bash
   pip install git+https://gitlab.com/your_username/your_package_name.git@branch_or_tag
   ```

   在这里，`your_username`是你的GitLab用户名，`your_package_name`是你的仓库名称，`branch_or_tag`是你想要安装的分支或标签的名称。如果不指定分支或标签，`pip`将默认安装`master`分支（或`main`分支，取决于你的仓库设置）。
请注意，这种方法要求安装者有一个有效的Python环境，并且已经安装了`git`。此外，由于这种安装方式直接从源代码安装，用户可能需要在安装前满足你的库的依赖项。在你的`README.md`中提供安装说明是一个好主意，这样用户就知道如何安装你的库了。

## 参考资料

- [花了两天，终于把 Python 的 setup.py 给整明白了][1]

  [1]: https://zhuanlan.zhihu.com/p/276461821
  [2]: https://github.com/pypa/sampleproject
  [3]: https://github.com/pypa/sampleproject/blob/db5806e0a3204034c51b1c00dde7d5eb3fa2532e/setup.py
