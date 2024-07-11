# Git 使用笔记

- 解决 gitk 中文乱码的问题

  ```sh
  git config --global gui.encoding utf-8
  ```

- Git diff 显示特殊字符

  ```sh
  git diff --ws-error-highlight=all
  ```

- Git 设置本地分支与远端分支的映射关系

  ```sh
  git branch -u origin/develop develop
  ```

- Git 查看本地分支与远端分支的映射关系

  ```sh
  git branch -vv
  ```

- [Git 设置使用 Beyond Compare 作为 diff 和 merge 工具][2]

  ```sh
  # 设置 diff 工具
  git config --global diff.tool bc
  git config --global difftool.bc.path "c:/Program Files/Beyond Compare 5/bcomp.exe"

  # 设置 merge 工具
  git config --global merge.tool bc
  git config --global mergetool.bc.path "c:/Program Files/Beyond Compare 5/bcomp.exe"

  # 对比差异
  git difftool

  # 合并
  git mergetool
  ```

- Git staging area
  - The staging area is a file, generally contained in your Git directory, that stores information about what will go into your next commit.
  - Its technical name in Git parlance is the “index”, but the phrase “staging area” works just as well.
  - 伍注：Git 暂存区对应的文件为 `.git/index`

- Show all authors

  ```bash
  # show all users & emails, and the number of commits in the CURRENT branch:
  git shortlog --summary --numbered --email

  # Or simply:
  git shortlog -sne

  # To show users from all branches you have to add --all flag:
  git shortlog -sne --all
  ```

- Show only date and commit message of logs
  - [git log documentation][1]

  ```bash
  git log --pretty=format:"%cs %s"
  ```

- Rename a git tag

  ```bash
  git tag new old           # Create a new local tag named `new` from tag `old`.
  git tag -d old            # Delete local tag `old`.
  git push origin new :old  # Push `new` to your remote named "origin", and delete
                            #     tag `old` on origin (by pushing an empty tag
                            #     name to it).
  ```

- Delete a git tag

  ```bash
  # You can push an 'empty' reference to the remote tag name:
  git push origin :tagname

  # Or, more expressively, use the --delete option (or -d if your git version is older than 1.8.0):
  git push --delete origin tagname
  ```

- Trace the evolution of a function

  ```bash
  git log -L "<funcname>:<file>"
  ```

- Unset a global proxy

  ```bash
  git config --global --unset http.proxy
  ```

- Show change diffs of some file on another branch

  ```bash
  git log <branch> -p -- <path/to/file>
  ```

- Delete remote branch

  ```bash
  git push origin -d branch-name
  ```

- Git Basic configuration

  ```sh
  git config --global user.name "along"
  git config --global user.email "wuhl6@mail2.sysu.edu.cn"
  git config --global push.default simple
  git config --global core.editor "vim"
  ```

- Git alias

  ```bash
  git config --global alias.a 'add'
  git config --global alias.br 'branch'
  git config --global alias.ci 'commit'
  git config --global alias.ciam 'commit --amend --no-edit'
  git config --global alias.co 'checkout'
  git config --global alias.d 'diff --ws-error-highlight=all'
  git config --global alias.l 'log'
  git config --global alias.last 'log -1 HEAD --stat'
  git config --global alias.ll 'log --oneline'
  git config --global alias.ln 'log --name-only'
  git config --global alias.ph 'push'
  git config --global alias.pl 'pull'
  git config --global alias.re 'remote'
  git config --global alias.st 'status'
  ```

  [1]: https://git-scm.com/docs/git-log
  [2]: https://www.scootersoftware.com/kb/vcs
