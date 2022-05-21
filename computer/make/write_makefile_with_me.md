# 《跟我一起写 Makefile》笔记

## makefile 介绍

### makefile 的规则

```make
target target-name : prerequisite-file-name
    command1
    command2
    ...
```

- makefile 的规则
  - prerequisites 中如果有一个以上的文件比 target 文件要新的话， command 所定义的命令就会被执行。

### 一个示例

```make
edit : main.o kbd.o command.o display.o \
       insert.o search.o files.o utils.o
    cc -o edit main.o kbd.o command.o display.o \
           insert.o search.o files.o

main.o : main.c defs.h
    cc -c main.c

kbd.o : kbd.c defs.h command.h
    cc -c kbd.c

command.o : command.c defs.h command.h
    cc -c command.c

display.o : display.c defs.h buffer.h
    cc -c display.c

insert.o : insert.c defs.h buffer.h
    cc -c insert.c

search.o : search.c defs.h buffer.h
    cc -c search.c

files.o : files.c defs.h buffer.h command.h
    cc -c files.c

utils.o : utils.c defs.h
    cc -c utils.c

clean:
    rm edit main.o kbd.o command.o display.o \
    insert.o search.o files.o utils.o
```

- 注意：定义好依赖关系后，后续的那一行command必须以一个Tab键作为开头。

### makefile 是如何工作的

- makefile 的工作过程
  - make 会一层又一层地去找文件的依赖关系，直到最终编译出第一个目标文件。
  - 在找寻的过程中，如果出现错误，比如最后被依赖的文件找不到，那么 make 就会直接退出，并报错。
  - 对于所定义的命令的错误，或是编译不成功， make 根本不理。
  - make 只管文件的依赖性，即，如果在我找了依赖关系之后，冒号后面的文件还是不在，那么对不起，我就不工作啦。

- Makefile 每行命令在一个单独的 shell 中执行
  - 这些 shell 之间没有继承关系
  - 比如下面代码执行后，取不到 foo 的值， 因为两行命令在两个不同的进程执行。
  - 解决办法一是将两行命令写在一行，中间用分号分隔。
  - 解决办法二是在换行符前加反斜杠转义。

  ```make
  export foo=bar
  echo "foo=[$$foo]"
  ```

- make 的常见功能
  - 在 Unix 世界中，软件发布时，特别是 GNU 这种开源软件的发布时，其 makefile 都包含了编译、安装、打包等功能。
  - 我们可以参照这种规则来书写我们的 makefile 中的目标。

### makefile 中使用变量

```make
objects =  main.o kbd.o command.o display.o \
      insert.o search.o files.o utils.o

edit: $(objects)
    cc -o edit $(objects)
```

### 让 make 自动推导

GNU make 看到一个 whatever.o 文件时，会自动的把对应的 whatever.c 文件加在依赖关系中，并且`cc -c whatever.c`也会被推导出来。
这使得我们在写依赖关系时可以更简洁。

```make
# 由于 make 会自动推导出来 make.c，此处省略不写。
main.o : defs.h
```

### 清空文件的规则

- 由于 clean 没有被第一个目标文件直接或间接关联，那么它后面所定义的命令将不会被自动执行。

- 我们可以通过执行 `make clean` 显式要 make 执行，以此来清除所有的目标文件，以便重编译。

- 下面是更稳健的clean写法。
  - `.PHONY` 表示 clean 是一个「伪目标」。
  - rm 命令前面加了一个小减号的意思就是，也许某些文件出现问题，但不要管，继续做后面的事。
  - 如果没有 `.PHONY` 语句显式声明这是伪目标，则存在以下问题：
    如果当前目录中，正好有一个文件叫做clean，那么这个命令不会执行。
    因为Make发现clean文件已经存在，就认为没有必要重新构建了，就不会执行指定的rm命令。

  ```make
  .PHONY: clean
  clean:
      -rm edit $(objects)
  ```

### Makefile 里有什么？

- Makefile 里主要包含了五个东西：显式规则、隐晦规则、变量定义、文件指示和注释。
  - 显式规则。显式规则说明了如何生成一个或多个目标文件。这是由 Makefile 的书写者明显指出要生成的文件、文件的依赖文件和生成的命令。
  - 隐晦规则。由于我们的 make 有自动推导的功能，所以隐晦的规则可以让我们比较简略地书写 Makefile，这是由 make 所支持的。
  - 变量的定义。在 Makefile 中我们要定义一系列的变量，变量一般都是字符串，
    这个有点像C语言中的宏，当 Makefile 被执行时，其中的变量都会被扩展到相应的引用位置上。
  - 文件指示。这个包括了三个部分：
    - 在一个 Makefile 中引用另一个 Makefile，就像C语言中的 `#include` 一样；
    - 根据某些情况指定 Makefile 中的有效部分，就像C语言中的预编译 `#if` 一样；
    - 定义一个多行的命令。
  - 注释。
    - Makefile中只有行注释，和UNIX的Shell脚本一样，其注释是用 # 字符，这个就像C/C++中的 // 一样。
    - 如果你要在你的Makefile中使用 # 字符，可以用反斜杠进行转义，如： `\#` 。

- 最后，还值得一提的是，在 Makefile 中的命令，必须要以 Tab 键开始。

### Makefile 的文件名

- GNU make 默认的 Makefile 文件名
  - 默认情况下，make 命令会在当前目录下依次找三个文件：GNUmakefile、makefile、Makefile。
  - 一旦找到，就开始读取这个文件并执行。

- 为 make 命令指定其他名字的 Makefile
  - 使用 make的 `-f` 或 `--file` 参数。
  - 举例：`make –f hchen.mk`

### 引用其它的 Makefile

```make
include <filename>
```

- include 前面可以有一些空字符，但是绝不能是 Tab 键开始。

- make 查找 include 所指出的 Makefile 的流程
  - make 首先会在当前目录下寻找
  - 如果当前目录下没有找到，make 还会在下面的几个目录下找：
    - 如果 make 执行时，有 `-I` 或 `--include-dir` 参数，那么 make 就会在这个参数所指定的目录下去寻找。
    - 如果目录 `<prefix>/include` （一般是： `/usr/local/bin` 或 `/usr/include`）存在的话，make 也会去找。

- 如果有文件没有找到的话，
  - make会生成一条警告信息，但不会马上出现致命错误。
  - 它会继续载入其它的文件，一旦完成makefile的读取，make会再重试这些没有找到或不能读取的文件。
  - 如果还是不行，make才会出现一条致命信息。
  - 如果你想让make不理那些无法读取的文件，而继续执行，你可以在include前加一个减号`-`。

### make 的工作方式

- GNU make 的执行步骤
  - 读入所有的 Makefile。
  - 读入被 include 的其它 Makefile。
  - 初始化文件中的变量。
  - 推导隐晦规则，并分析所有规则。
  - 为所有的目标文件创建依赖关系链。
  - 根据依赖关系，决定哪些目标要重新生成。
  - 执行生成命令。

- 对 GNU make 执行步骤的备注
  - 第 1-5 步为第一个阶段， 第 6-7 步为第二个阶段。
  - 第一个阶段中，如果定义的变量被使用了，那么， make会把其展开在使用的位置。
  - 但 make 并不会完全马上展开， make 使用的是拖延战术，
    如果变量出现在依赖关系的规则中，那么仅当这条依赖被决定要使用了，变量才会在其内部展开。

## 书写规则

- make 的最终目标
  - Makefile 中只应该有一个最终目标，其它的目标都是被这个目标所连带出来的，所以一定要让 make 知道你的最终目标是什么。
  - 一般来说，定义在Makefile中的目标可能会有很多，但是第一条规则中的目标将被确立为最终的目标。
  - 如果第一条规则中的目标有很多个，那么，第一个目标会成为最终的目标。

### 规则的语法

- 规则告诉make两件事，文件的依赖关系和如何生成目标文件。

- 如果命令太长，你可以使用反斜杠 `\` 作为换行符。make 对一行上有多少个字符没有限制。

- 一般来说，make 会以 UNIX 的标准 shell，也就是 `/bin/sh` 来执行命令。
  - 如果想改用其他 shell（比如说 bash），在你的 makefile 开头加上 `SHELL := /bin/bash` 即可。

### 在规则中使用通配符

- make支持三个通配符： `*`， `?` 和 `~`。这是和Unix的B-Shell是相同的。

- `wildcard`
  - 功能
    - 在 Makefile 规则中，通配符会被自动展开。但变量的定义和函数引用时，通配符将失效。
      比如：`objects = *.o` 代表 `objects` 的值就是 `*.o`，而不是展开后的值。
    - 这种情况下如果需要通配符有效，就需要使用函数`wildcard`
  - 用法
    - `$(wildcard PATTERN...)`
    - `$(wildcard \*.c)` 获取工作目录下的所有的 `.c` 文件列表。
    - `$(patsubst %.c,%.o,$(wildcard \*.c))`，获取工作目录下的所有的 `.o` 文件列表。
  - 原理
    - 在 Makefile 中，它被展开为已经存在的、使用空格分开的、匹配此模式的所有文件列表。
    - 如果不存在任何符合此模式的文件，函数会忽略模式字符并返回空。

### 文件搜寻

- `VPATH` 特殊变量
  - 如果没有指明这个变量，make 只会在当前的目录中去找寻依赖文件和目标文件。
  - 如果定义了这个变量，make 就会在当前目录找不到的情况下，到所指定的目录中去找寻文件了。

- `vpath` 关键字
  - `vpath <pattern> <directories>` 为符合模式 `<pattern>` 的文件指定搜索目录 `<directories>`。
  - `vpath <pattern>` 清除符合模式 `<pattern>` 的文件的搜索目录。
  - `vpath` 清除所有已被设置好了的文件搜索目录。

### 伪目标

- `.PHONY`
  - 用来显式地指明一个目标是「伪目标」。
  - 建议：显式指明伪目标是一个好习惯。

### 多目标

- Makefile 的规则中的目标可以不止一个，其支持多目标。

- 有可能我们的多个目标同时依赖于一个文件，并且其生成的命令大体类似。于是我们就能把其合并起来。

### 静态模式

- 语法
  - targets 定义了一系列的目标文件，可以有通配符。是目标的一个集合。
  - target-pattern 指明了 targets 的模式，也就是的目标集模式。
  - prereq-patterns 是目标的依赖模式，它对 target-pattern 形成的模式再进行一次依赖目标的定义。

  ```make
  <targets ...> : <target-pattern> : <prereq-patterns ...>
      <commands>
      ...
  ```

- 示例1
  - `%.o` 表明要所有以 `.o` 结尾的目标，也就是 `foo.o bar.o` ，也就是变量 $object 集合的模式。
  - 依赖模式 `%.c` 则取模式 `%.o` 的 `%` ，也就是 `foo bar`，并为其加下 `.c` 的后缀，于是，我们的依赖目标就是 `foo.c bar.c`。

  ```make
  objects = foo.o bar.o

  all: $(objects)

  $(objects): %.o: %.c
      $(CC) -c $(CFLAGS) $^ -o $@
  ```

- 示例2

  ```make
  files = foo.elc bar.o lose.o

  $(filter %.o,$(files)): %.o: %.c
      $(CC) -c $(CFLAGS) $< -o $@

  $(filter %.elc,$(files)): %.elc: %.el
      emacs -f batch-byte-compile $<
  ```

### 自动生成依赖性

- `-M` 或 `-MM`
  - 大多数的 C/C++ 编译器都支持一个 `-M` 的选项，即自动找寻源文件中包含的头文件，并生成一个依赖关系。
  - 如果你使用 GNU 的 C/C++ 编译器，你得用 `-MM` 参数，因为 `-M` 参数会把一些标准库的头文件也包含进来。

- 依赖关系单独放在一个文件中
  - GNU 组织建议把编译器为每一个源文件的自动生成的依赖关系放到一个文件中
  - 为每一个 `name.c` 的文件都生成一个 `name.d` 的 Makefile 文件， `.d` 文件中就存放对应 `.c` 文件的依赖关系。

- 自动产生 `.d` 文件的模式规则
  - 这个规则把依赖关系 `main.o : main.c defs.h` 转成 `main.o main.d : main.c defs.h`。

  ```make
  %.d: %.c
      @set -e; rm -f $@; \
      $(CC) -M $(CPPFLAGS) $< > $@.$$$$; \
      sed 's,\($*\)\.o[ :]*,\1.o $@ : ,g' < $@.$$$$ > $@; \
      rm -f $@.$$$$
  ```

- 把自动生成的规则放进主 Makefile 中

  ```make
  sources = foo.c bar.c

  include $(sources:.c=.d)
  ```

## 书写命令

### 显示命令

- `@` 关闭命令显示
  - 通常 make 会把其要执行的命令行在命令执行前输出到屏幕上。
  - 当我们用 `@` 字符在命令行前，那么，这个命令将不被 make 显示出来。

- 如何实现默认情况下不打印Makefile中的命令，而用户给出要求时可以打印？
  - 在Makefile定义`V=@`，在执行编译链接等语句前都加上`$(V)`，这样直接make时不会打印Makefile中的命令，而输入`make "V="`时则会打印。

- `-n` 或 `--just-print`
  - 只是显示命令，但不会执行命令

- `-s` 或 `-silent` 或 `-quiet`
  - 全面禁止命令的显示。

### 命令执行

- `;` 在同一个 shell 里面执行多条命令
  - 如果你要让上一条命令的结果应用在下一条命令时，你应该使用分号分隔这两条命令。
  - 比如你的第一条命令是 cd 命令，你希望第二条命令得在 cd 之后的基础上运行，那么你应该把这两条命令写在一行上，用分号分隔。

### 命令出错

- 命令出错的后果
  - 每当命令运行完后，make会检测每个命令的返回码。
  - 如果命令返回成功，那么make会执行下一条命令。
  - 当规则中所有的命令成功返回后，这个规则就算是成功完成了。
  - 如果一个规则中的某个命令出错了（命令退出码非零），那么make就会终止执行当前规则，这将有可能终止所有规则的执行。

- `-` 忽略错误
  - 有时我们需要忽略命令的出错（比如创建一个目录，如果目录已存在也不报错），
    可以在 Makefile 的命令行前加一个减号 `-` （在 Tab 键之后），标记为不管命令出不出错都认为是成功的。

- `-i` 或 `--ignore-errors`
  - Makefile 中所有命令都会忽略错误。

- `-k` 或 `--keep-going`
  - 如果某规则中的命令出错了，那么就终止该规则的执行，但继续执行其它规则。

- `$(MAKE)`
  - makefile 脚本中往往定义 `$(MAKE)` 宏变量，其原因是：也许我们的 make 需要一些参数，所以定义成一个变量比较利于维护。

- makefile 参数传递
  - 我们把根目录下的 Makefile 叫做「总控 Makefile」
  - 总控 Makefile 的变量可以传递到下级的Makefile 中（如果你显式的声明），但是不会覆盖下层的 Makefile 中所定义的变量，除非指定了 `-e` 参数。
  - 如果你要传递变量到下级 Makefile 中，那么你可以使用这样的声明：`export <variable ...>;`
  - 如果你要传递所有变量，只要一个 export 就行了，后面什么也不用跟：`export`
  - 如果你不想让某些变量传递到下级 Makefile 中，那么你可以这样声明: `unexport <variable ...>;`
  - 不管你是否 export，`SHELL` 和 `MAKEFLAGS` 这两个变量总是传递到下层 Makefile 中
    - MAKEFLAGS 是一个系统级的环境变量
    - MAKEFLAGS 变量包含了 make 的参数信息
    - 如果我们执行「总控 Makefile」时有 make 参数或是在上层 Makefile 中定义了这个变量，
      那么 MAKEFLAGS变量将会是这些参数，并会传递到下层 Makefile 中。
  - make 命令中的有几个参数并不往下传递，它们是：-C, -f, -h, -o 和 -W。
  - 如果你定义了环境变量 MAKEFLAGS ，那么你得确信其中的选项是大家都会用到的，
    如果其中有 -t, -n 和 -q 参数，那么将会有让你意想不到的结果，或许会让你异常地恐慌
  - `-w` 或 `--print-directory` 会在 make 的过程中输出一些信息，让你看到目前的工作目录

### 定义命令包

- 定义命令包的语法
  - 如果Makefile中出现一些相同命令序列，那么我们可以为这些相同的命令序列定义一个变量。
  - 定义这种命令序列的语法以 define 开始，以 endef 结束
  - 使用这个命令包时，就好像使用变量一样。

  ```make
  define run-yacc
  yacc $(firstword $^)
  mv y.tab.c $@
  endef

  foo.c : foo.y
      $(run-yacc)
  ```

## 使用变量

### 变量的基础

- 变量在声明时需要给予初值。

- 变量在使用时，需要在变量名前加上 $ 符号，但最好用小括号 `()` 或是大括号 `{}` 把变量括起来。

- 如果你要使用真实的 $ 字符，那么你需要用 $$ 来表示。

- 变量会在使用它的地方精确地展开，就像 C/C++ 中的宏一样。

### 变量中的变量

- `=` vs `:=`
  - `=` 右侧中的变量不一定非要是已定义好的值，也可以使用后面定义的值。
  - `:=` 右侧只能使用前面已定义好的变量。

- [Setting Variables][1]
  - Variables defined with `=` are recursively expanded variables.
  - Variables defined with `:=` or `::=` are simply expanded variables;
    these definitions can contain variable references which will be expanded before the definition is made.
  - Variables defined with `?=` are set to a value only if they'are not already set.

- `MAKELEVEL`
  - 记录了我们的当前 Makefile 的调用层数。

  ```make
  ifeq (0,${MAKELEVEL})
  cur-dir   := $(shell pwd)
  whoami    := $(shell whoami)
  host-type := $(shell arch)
  MAKE := ${MAKE} host-type=${host-type} whoami=${whoami}
  endif
  ```

- 定义一个取值为空格的变量

  ```make
  nullstring :=
  space := $(nullstring) # end of the line
  ```

### 变量高级用法

- 变量值的替换

  ```make
  # 把变量 var 中所有以 a 字串结尾的 a 替换成 b 字串
  $(var:a=b)
  # or
  ${var:a=b}

  # 把变量 foo 中所有以 .o 结尾的字符串中的 .o 替换成 .c
  bar := $(foo:.o=.c)
  # or
  bar := $(foo:%.o=%.c)`
  ```

- 把变量的值再作为变量

  ```make
  x = y
  y = z
  a := $($(x))
  ```

### 追加变量值

- `+=`
  - += 操作符给变量追加值。
  - 如果之前没有定义过该变量，那么， += 会自动变成 =
  - 如果之前定义过该变量，那么 += 会继承于前次操作的赋值符。
  - 如果前一次定义时使用的操作符是 := ，那么 += 会以 := 作为其赋值符。

### override 指示符

- 如果某变量通常是在 make 的命令行参数设置的，那么 Makefile 中对这个变量的赋值会被忽略。

- 如果你想在 Makefile 中设置这类参数的值，那么你可以使用 `override` 指示符。

### 环境变量

- 如果我们在环境变量中设置了 CFLAGS 环境变量，那么我们就可以在所有的 Makefile 中使用这个变量了。
  这对于我们使用统一的编译参数有比较大的好处。

- 如果 Makefile 中定义了 CFLAGS，那么则会使用 Makefile 中的这个变量，如果没有定义则使用系统环境变量的值。
  一个共性和个性的统一，很像「全局变量」和「局部变量」的特性。

### 目标变量

- Target-specific Variable
  - 我们可以为某个目标设置局部变量，这种变量被称为「Target-specific Variable」，它可以和「全局变量」同名。
  - 因为它的作用范围只在这条规则以及连带规则中，所以其值也只在作用范围内有效，而不会影响规则链以外的全局变量的值。

```make
<target ...> : <variable-assignment>;
<target ...> : overide <variable-assignment>
```

### 模式变量

- Pattern-specific Variable
  - 我们可以给定一种「模式」，可以把变量定义在符合这种模式的所有目标上。

```make
<pattern ...>; : <variable-assignment>;
<pattern ...>; : override <variable-assignment>;
```

## 使用条件判断

- 语法

  ```make
  <conditional-directive>
  <text-if-true>
  endif
  ```

  ```make
  <conditional-directive>
  <text-if-true>
  else
  <text-if-false>
  endif
  ```

- 四种 `<conditional-directive>`

  ```make
  ifeq (<arg1>, <arg2>)
  ifneq (<arg1>, <arg2>)
  ifdef <variable-name>
  ifndef <variable-name>
  ```

## 使用函数

### 字符串处理函数

- `$(subst <from>,<to>,<text>)`
  - 把字串 `<text>` 中的 `<from>` 字符串替换成 `<to>` ，并返回被替换过后的字符串。

- `$(patsubst <pattern>,<replacement>,<text>)`
  - 查找 `<text>` 中的单词（单词以空格、Tab、回车符或换行符分隔）是否符合模式 `<pattern>`，如果匹配的话，则以 `<replacement>` 替换。
  - `<pattern>` 可以包括通配符 % ，表示任意长度的字串。
  - 如果 `<replacement>` 中也包含 % ，那么， `<replacement>` 中的这个 % 将是 `<pattern>` 中的那个 % 所代表的字串。
  - 如果要表示真实含义的 % 字符，可以用 `\%`。
  - 返回被替换过后的字符串。

- `$(strip <string>)`
  - 去掉 `<string>` 字串中开头和结尾的空字符。

- `$(findstring <find>,<in>)`
  - 在字串 `<in>` 中查找 `<find>` 字串。如果找到，那么返回 `<find>` ，否则返回空字符串。

- `$(filter <pattern...>,<text>)`
  - 以 `<pattern>` 模式过滤 `<text>` 字符串中的单词，保留符合模式 `<pattern>` 的单词。可以有多个模式。
  - 最终返回符合模式 `<pattern>` 的字串。

- `$(filter-out <pattern...>,<text>)`
  - 以 `<pattern>` 模式过滤 `<text>` 字符串中的单词，去除符合模式 `<pattern>` 的单词。可以有多个模式。
  - 最终返回不符合模式 `<pattern>` 的字串。

- `$(sort <list>)`
  - 给字符串 `<list>` 中的单词排序（升序）。返回排序后的字符串。

- `$(word <n>,<text>)`
  - 返回字符串 `<text>` 中第 n 个单词。
  - 如果 n 比 `<text>` 中的单词数要大，那么返回空字符串。

- `$(wordlist <s>,<e>,<text>)`
  - 返回字符串 `<text>` 中取从 s 开始到 e 的单词串。 s 和 e 是一个数字。
  - 如果 s 比 `<text>` 中的单词数要大，那么返回空字符串。
  - 如果 e 比 `<text>` 中的单词数要大，那么返回从 s 开始，到 `<text>` 结束的单词串。

- `$(words <text>)`
  - 返回 `<text>` 中的单词数。

- `$(firstword <text>)`
  - 取字符串 `<text>` 中的第一个单词。

### 文件名处理函数

- `$(dir <names...>)`
  - 从文件名序列 `<names>` 中取出目录部分。目录部分是指最后一个反斜杠（/ ）之前的部分。
  - 如果没有反斜杠，那么返回 `./`。

- `$(notdir <names...>)`
  - 从文件名序列 `<names>` 中取出非目录部分。非目录部分是指最後一个反斜杠（/ ）之后的部分。

- `$(suffix <names...>)`
  - 从文件名序列 `<names>` 中取出各个文件名的后缀。
  - 返回文件名序列 `<names>` 的后缀序列，如果文件没有后缀，则返回空字串。

- `$(basename <names...>)`
  - 从文件名序列 `<names>` 中取出各个文件名的前缀部分。
  - 返回文件名序列 `<names>` 的前缀序列，如果文件没有前缀，则返回空字串。

- `$(addsuffix <suffix>,<names...>)`
  - 把后缀 `<suffix>` 加到 `<names>` 中的每个单词后面。返回加过后缀的文件名序列。

- `$(addprefix <prefix>,<names...>)`
  - 把前缀 `<prefix>` 加到 `<names>` 中的每个单词后面。返回加过前缀的文件名序列。

- `$(join <list1>,<list2>)`
  - 把 `<list2>` 中的单词对应地加到 `<list1>` 的单词后面。
  - 如果 `<list1>` 的单词个数要比 `<list2>` 的多，那么 `<list1>` 中的多出来的单词将保持原样。
  - 如果 `<list2>` 的单词个数要比 `<list1>` 的多，那么 `<list2>` 多出来的单词将被复制到 `<list1>` 中。
  - 返回连接过后的字符串。

### 其他

- `$(foreach <var>,<list>,<text>)`
  - 把参数 `<list>` 中的单词逐一取出放到参数 `<var>` 所指定的变量中，然后再执行 `<text>` 所包含的表达式。
  - 每一次 `<text>` 会返回一个字符串，循环过程中， `<text>` 的所返回的每个字符串会以空格分隔。
  - 最后当整个循环结束时， `<text>` 所返回的每个字符串所组成的整个字符串（以空格分隔）将会是 foreach 函数的返回值。

- `$(call <expression>,<parm1>,<parm2>,...,<parmn>)`
  - call 函数是唯一一个可以用来创建新的参数化的函数。
  - 你可以写一个非常复杂的表达式，这个表达式中，你可以定义许多参数，然后你可以 call 函数来向这个表达式传递参数。
  - 当 make 执行这个函数时， `<expression>` 参数中的变量，如 `$(1)`、`$(2)` 等，会被参数 `<parm1>`、`<parm2>`、`<parm3>` 依次取代。
  - `<expression>` 的返回值就是 call 函数的返回值。

- `$(origin <variable>)`
  - origin 函数不像其它的函数，它并不操作变量的值，它只是告诉你你的这个变量是哪里来的。
  - 注意，`<variable>` 是变量的名字，不应该是引用。所以你最好不要在 `<variable>` 中使用 $ 字符。
  - origin 函数会以其返回值来告诉你这个变量的「出生情况」：
    - undefined 如果 `<variable>` 从来没有定义过， origin 函数返回这个值 undefined
    - default 如果 `<variable>` 是一个默认的定义，比如“CC”这个变量，这种变量我们将在后面讲述。
    - environment 如果 `<variable>` 是一个环境变量，并且当 Makefile 被执行时， -e 参数没有被打开。
    - file 如果 `<variable>` 这个变量被定义在 Makefile 中。
    - command line 如果 `<variable>` 这个变量是被命令行定义的。
    - override 如果 `<variable>` 是被 override 指示符重新定义的。
    - automatic 如果 `<variable>` 是一个命令运行中的自动化变量。

- `$(shell command args ...)`
  - 这个函数会新生成一个 Shell 程序来执行命令，所以你要注意其运行性能。
  - 如果你的Makefile 中有一些比较复杂的规则，并大量使用了这个函数，那么对于你的系统性能是有害的。
  - 特别是 Makefile 的隐晦的规则可能会让你的 shell 函数执行的次数比你想像的多得多。

- 控制 make 的函数
  - `$(error <text ...>)` 产生一个致命错误，并让 make 退出
  - `$(warning <text ...>)` 输出一段警告信息，而make继续执行。

## make 的运行

### 指定目标

- make 的常见目标
  - all: 这个伪目标是所有目标的目标，其功能一般是编译所有的目标。
  - clean: 这个伪目标功能是删除所有被 make 创建的文件。
  - install: 这个伪目标功能是安装已编译好的程序，其实就是把目标执行文件拷贝到指定的目标中去。
  - print: 这个伪目标的功能是例出改变过的源文件。
  - tar: 这个伪目标功能是把源程序打包备份。也就是一个 tar 文件。
  - dist: 这个伪目标功能是创建一个压缩文件，一般是把 tar 文件压成 Z 文件。或是 gz 文件。
  - TAGS: 这个伪目标功能是更新所有的目标，以备完整地重编译使用。
  - check 和 test: 这两个伪目标一般用来测试 makefile 的流程。

### 检查规则

- `-n, --just-print, --dry-run, --recon`
  - 不执行参数，这些参数只是打印命令，不管目标是否更新，把规则和连带规则下的命令打印出来，但不执行，
    这些参数对于我们调试makefile很有用处。

- `-t, --touch`
  - 这个参数的意思就是把目标文件的时间更新，但不更改目标文件。
    也就是说，make假装编译目标，但不是真正的编译目标，只是把目标变成已编译过的状态。

- `-q, --question`
  - 这个参数的行为是找目标的意思，也就是说，如果目标存在，那么什么也不会输出，当然也不会执行编译，
    如果目标不存在，其会打印出一条出错信息。

- `-W <file>, --what-if=<file>, --assume-new=<file>, --new-file=<file>`
  - 这个参数需要指定一个文件。一般是是源文件（或依赖文件），Make 会根据规则推导来运行依赖于这个文件的命令，
    一般来说，可以和 `-n` 参数一同使用，来查看这个依赖文件所发生的规则命令。

## 隐含规则

### 使用隐含规则

- 在 make 的「隐含规则库」中，每一条隐含规则都在库中有其顺序，越靠前的则是越被经常使用的。
  所以，这会导致我们有些时候即使我们显示地指定了目标依赖，make 也不会管。

- 如果你不希望任何隐含规则推导，那么你最好同时写出依赖规则和命令。

### 隐含规则一览

- 编译C程序的隐含规则
  - `<n>.o` 的目标的依赖目标会自动推导为 `<n>.c`，并且其生成命令是 `$(CC) –c $(CPPFLAGS) $(CFLAGS)`

- 编译C++程序的隐含规则
  - `<n>.o` 的目标的依赖目标会自动推导为 `<n>.cc` 或 `<n>.C` ，并且其生成命令是 `$(CXX) –c $(CPPFLAGS) $(CXXFLAGS)`。
    （建议使用 .cc 作为C++源文件的后缀，而不是 .C ）

- 汇编和汇编预处理的隐含规则
  - `<n>.o` 的目标的依赖目标会自动推导为 `<n>.s`，默认使用编译器 as，并且其生成命令是： `$(AS) $(ASFLAGS)`。
  - `<n>.s` 的目标的依赖目标会自动推导为 `<n>.S`，默认使用C预编译器 cpp，并且其生成命令是： `$(AS) $(ASFLAGS)`。

- 链接Object文件的隐含规则
  - `<n>` 目标依赖于 `<n>.o`，通过运行C的编译器来运行链接程序生成（一般是 ld），其生成命令是：
    `$(CC) $(LDFLAGS) <n>.o $(LOADLIBES) $(LDLIBS)`。
  - 这个规则对于只有一个源文件的工程有效，同时也对多个Object文件（由不同的源文件生成）的也有效。

### 隐含规则使用的变量

- 关于命令的变量
  - AR : 函数库打包程序。默认命令是 ar
  - AS : 汇编语言编译程序。默认命令是 as
  - CC : C语言编译程序。默认命令是 cc
  - CXX : C++语言编译程序。默认命令是 g++
  - CO : 从 RCS文件中扩展文件程序。默认命令是 co
  - CPP : C程序的预处理器（输出是标准输出设备）。默认命令是 $(CC) –E

- 关于命令参数的变量（如果没有指明默认值，那么其默认值都是空）
  - ARFLAGS : 函数库打包程序AR命令的参数。默认值是 rv
  - ASFLAGS : 汇编语言编译器参数。（当明显地调用 .s 或 .S 文件时）
  - CFLAGS : C语言编译器参数。
  - CXXFLAGS : C++语言编译器参数。
  - CPPFLAGS : C预处理器参数。（C 和 Fortran 编译器也会用到）。

- 自动化变量
  - `$@` 表示规则中的目标文件集。在模式规则中，如果有多个目标，那么， `$@` 就是匹配于目标中模式定义的集合。
    比如，`make foo` 的 `$@` 就指代 foo。
  - `$%` 仅当目标是函数库文件中，表示规则中的目标成员名。
    如果目标不是函数库文件（Unix下是 .a ，Windows下是 .lib ），那么，其值为空。
    比如，如果一个目标是 foo.a(bar.o) ，那么，`$%` 就是 bar.o，$@ 就是 foo.a。
  - `$<` 依赖目标中的第一个目标名字。如果依赖目标是以模式（即 % ）定义的，那么 `$<` 将是符合模式的一系列的文件集。
    注意，它是一个一个取出来的。
  - `$?` 所有比目标新的依赖目标的集合，以空格分隔。 - 比如，规则为 `t: p1 p2`，其中 p2 的时间戳比 t 新，`$?` 就指代 p2。
  - `$^` 所有的依赖目标的集合。以空格分隔。如果在依赖目标中有多个重复的，那么这个变量会去除重复的依赖目标，只保留一份。
  - `$+` 这个变量很像 `$^`，也是所有依赖目标的集合。只是它不去除重复的依赖目标。
  - `$*` [The stem with which an implicit rule matches][2]. 粗略地说，这个变量表示目标模式中 % 匹配的内容。
    比如，如果目标是 a.foo.b，并且目标的模式是 a.%.b，那么 `$*` 的值就是 foo。
    但如果目标是 dir/a.foo.b ，并且目标的模式是 a.%.b ，那么， `$*` 的值就是 dir/foo 。

> 伍注：`$*` 的准确含义请参考 GNU make 手册，平时使用的话，理解好以上例子的两种情况应该就够了。

- 自动化变量加上 D 或 F 的含义
  - `$(@D)` 表示 `$@` 的目录部分（不以斜杠作为结尾），如果 `$@` 值是 dir/foo.o ，那么 `$(@D)` 就是 dir，
    如果 $@ 中没有包含斜杠的话，其值就是 . （当前目录）。
  - `$(@F)` 表示 `$@` 的文件部分，如果 `$@` 值是 dir/foo.o ，那么 `$(@F)` 就是 foo.o ， `$(@F)` 相当于函数 `$(notdir $@)` 。
  - `$(*D)` 和 `$(*F)` 取文件的目录部分和文件部分。对于上面的那个例子， `$(*D)` 返回 dir ，而 `$(*F)` 返回 foo。
  - `$(%D)` 和 `$(%F)` 分别表示了函数包文件成员的目录部分和文件部分。
    这对于形同 archive(member) 形式的目标中的 member 中包含了不同的目录很有用。
  - `$(<D)` 和 `$(<F)` 分别表示依赖文件的目录部分和文件部分。
  - `$(^D)` 和 `$(^F)` 分别表示所有依赖文件的目录部分和文件部分。（无相同的）
  - `$(+D)` 和 `$(+F)` 分别表示所有依赖文件的目录部分和文件部分。（可以有相同的）
  - `$(?D)` 和 `$(?F)` 分别表示被更新的依赖文件的目录部分和文件部分。

### 隐含规则链

- 有些时候，一个目标可能被一系列的隐含规则所作用。
  - 例如，一个 .o 的文件生成，可能会是先被 Yacc的 .y 文件先成 .c，然后再被C的编译器生成。
  - 我们把这一系列的隐含规则叫做「隐含规则链」。
  - 我们把这种 .c 的文件（或目标），叫做中间目标。

- 对于中间目标，它和一般的目标有两个地方所不同：
  - 第一个不同是除非中间的目标不存在，才会引发中间规则。
  - 第二个不同是，只要目标成功产生，那么，产生最终目标过程中，所产生的中间目标文件会被以 `rm -f` 删除。

### 定义模式规则

- 模式规则
  - 你可以使用模式规则来定义一个隐含规则。
  - 一个模式规则就好像一个一般的规则，只是在规则中，目标的定义需要有 % 字符。
  - % 的意思是表示一个或多个任意字符。在依赖目标中同样可以使用 % ，只是依赖目标中的 % 的取值，取决于其目标。

## 参考资料

- [跟我一起写Makefile](http://wiki.ubuntu.com.cn/index.php?title=%E8%B7%9F%E6%88%91%E4%B8%80%E8%B5%B7%E5%86%99Makefile&variant=zh-cn)

- [跟我一起写 Makefile （seisman整理的版本）](https://github.com/seisman/how-to-write-makefile)

- [阮一峰：Make 命令教程](https://blog.csdn.net/a_ran/article/details/43937041)

- [GNU make's manual](https://www.gnu.org/software/make/manual/html_node/index.html#SEC_Contents)

  [1]: https://www.gnu.org/software/make/manual/html_node/Setting.html
  [2]: https://www.gnu.org/software/make/manual/html_node/Automatic-Variables.html
