# bash 使用笔记

## bash 基础配置

```bash
function mkdircd () { mkdir -p "$@" && eval cd "\"\$$#\""; }

alias ll="ls -al"

alias ..="cd .."
alias ...="cd ../.."
alias ....="cd ../../.."
alias .....="cd ../../../.."
alias ......="cd ../../../../.."

shopt -s cdspell

export GOROOT=${HOME}/go
export GOPATH=${HOME}/gopath
export PATH=${PATH}:${GOROOT}/bin:${GOPATH}/bin
export PATH=${PATH}:${HOME}/.local/bin

if test "${PS1+set}"; then
    export CDPATH=.:/mnt/c/Users/
fi
```

- [Bash Reference Manual][1]

  [1]: https://www.gnu.org/software/bash/manual/bash.html
