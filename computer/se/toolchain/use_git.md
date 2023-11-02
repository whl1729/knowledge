# Git 使用笔记

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