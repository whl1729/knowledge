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
