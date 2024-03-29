# Git 使用笔记

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
  git config --global alias.d 'diff'
  git config --global alias.l 'log'
  git config --global alias.last 'log -1 HEAD --stat'
  git config --global alias.ll 'log --oneline'
  git config --global alias.ln 'log --name-only'
  git config --global alias.ph 'push'
  git config --global alias.pl 'pull'
  git config --global alias.re 'remote'
  git config --global alias.st 'status'
  ```