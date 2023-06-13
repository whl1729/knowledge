# 如何命名

> 「名不正则言不顺，言不顺则事不成。」 ——孔子
>
> 「There are only two hard things in Computer Science: cache invalidation and naming things.」 —— Phil Karlton

在编程中，命名是非常重要的一件事情，直接影响代码的可读性。
同时，命名并非一件容易的事情。下文将介绍命名的一些基本原则及具体规范，
希望能够帮助大家以后在编程中尽可能使用好的名字。

## 关于命名的一些原则

- 名字要完全、准确地描述出该变量所代表的事物。（《代码大全》认为的最重要的命名原则）

  | 变量用途 | 好名字，好描述 | 坏名字，差描述 |
  | -------- | -------------- | -------------- |
  | 到期的支票累计额 | runningTotal, checkTotal | written, ct, checks, CHKTTL, x, x1, x2 |
  | 高速列车的运行速度 | velocity, trainVelocity, velocityInMph | velt, v, tv, x, x1, x2, train |
  | 当前日期 | currentDate, todaysDate | cd, current, c, x, x1, x2, date |
  | 每页的行数 | linesPerPage | lpp, lines, l, x, x1, x2 |

- 使用**揭示意图**的名字
  - 好的名字应该告诉你，它为什么会存在，它做什么事，应该怎么用。
  - 如果名称需要注释来补充，说明它没有完成揭示意图的任务。

  ```cpp
  // 差的变量名
  int d; // elapsed time in days

  // 好的变量名
  int elapsedTimeInDays;
  ```

- 一个好名字能让我一眼看出函数的用途，而不必查看其实现代码。
  - 一个改进函数名字的好办法：先写一句注释描述这个函数的用途，再把这句注释变成函数的名字。

- 以问题为导向
  - 好的名字反映的通常都是问题，而不是解决方案。
  - 好的名字通常表达的是「什么」（what）而不是「如何」（how）。
  - 举例1：一条员工数据记录
    - inputRec 是一个反映输入、记录这些计算概念的计算机术语
    - employeeData 则直指问题领域，与计算的世界无关
  - 举例2：表示打印机状态的位域
    - bitFlag 比 printerReady 更具计算机特征

- 好好取名，需要时重命名。(Name Well; Rename When Needed.)

- 把限定词加到名字的最后
  - 突出重点。变量中代表主要含义的部分应当位于最前面。
  - 统一风格，避免歧义。避免在程序中同时使用totalRevenue和revenueTotal。
  - 举例
    - revenueTotal（总收入）, revenueAverage （平均收入）
    - expenseTotal (总支出), expenseAverage （平均支出）

- 对仗词的使用要准确
  - begin/end
  - first/last
  - locked/unlocked
  - min/max
  - next/previous
  - old/new
  - opened/closed
  - visible/invisible
  - source/target
  - source/destination
  - up/down

- 做有意义的区分
  - 不要使用数字后缀来区分名字。
    - 举例：a1, a2, ..., aN
  - 不要使用废话来区分名字。
    - 废话举例：NameString， CustomerObject 和 moneyAmount

## 为特定类型的数据命名

- 为循环下标命名
  - 对于简单的循环，使用i, j和k这些约定俗成的名字。
  - 对于复杂的循环，最好使用更有意义的名字。

- 为状态变量命名
  - 取一个比flag更好的名字。

  ```cpp
  // 含义模糊的状态变量名字
  if (flag) ...
  if (statusFlag & 0x0F) ...
  if (printFlag == 16) ...
  if (computeFlag == 0) ...

  flag = 0x1;
  statusFlag = 0x80;
  printFlag = 16;
  computeFlag = 0;
  ```

  ```cpp
  // 好的状态变量名字
  if (dataReady) ...
  if (characterType & PRINTABLE_CHAR) ...
  if (reportType == ReportType_Annual) ...
  if (recalcNeeded = false) ...

  dataReady = true;
  characterType = CONTROL_CHARACTER;
  reportType = ReportType_Annual;
  recalcNeeded = false;
  ```

- 为临时变量命名
  - 警惕「临时」变量。你程序中的大多数变量都是临时性的。把其中几个称为临时的，可能表明你还没有弄清它们的实际用途。

  ```cpp
  // 不提供信息的「临时」变量名

  // Compute solutions of a quadratic equation.
  // This assumes that (b^2-4*a*c) is positive.
  temp = sqrt(b^2 - 4*a*c);
  solution[0] = (-b + temp) / (2 * a);
  solution[1] = (-b - temp) / (2 * a);
  ```

  ```cpp
  // 用真正的变量替代「临时」变量

  // Compute solutions of a quadratic equation.
  // This assumes that (b^2-4*a*c) is positive.
  discriminant = sqrt(b^2 - 4*a*c);
  solution[0] = (-b + discriminant) / (2 * a);
  solution[1] = (-b - discriminant) / (2 * a);
  ```

- 为布尔变量命名
  - 谨记典型的布尔变量名
    - done 表示某件事情已经完成
    - error 表示有错误发生
    - found 表示某个值已经找到了
    - success或ok 表示一项操作是否成功。如果可以，请用一个更具体的名字代替success。
  - 给布尔变量赋予隐含「真/假」含义的名字
    - 好的例子：done, found
    - 差的例子：status, sourceFile
    - `if (isFound)`的可读性要略差于`if (found)`
  - 使用肯定的布尔变量名
    - 双重否定的可读性很差。举例：`if not notFound`

- 类名
  - 类名和对象名应该是名词或名词短语。
  - 举例：Customer, WikiPage, Account, AddressParser

- 方法名
  - 方法名应该是动词或动词短语。
  - 举例：PostPayment, deletePage, save

## 参考资料

- Clean Code, Chapter 2: "Meaningful Names" （《代码整洁之道》第2章：「有意义的命名」）
- Code Complete, Chapter 11: "The Power of Variable Names" (《代码大全》第11章：「变量名的力量」)
- Refactoring: Improving the Design of Existing Code (《重构：改善既有代码的设计》)
- The Pragmatic Programmer, Topic 44: "Naming Things" (《程序员修炼之道》第44条：「事物命名」)
