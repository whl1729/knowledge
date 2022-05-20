# 数据库范式

## 数据库范式是什么

这是维基百科词条[Database normalization][1]给出的定义：

> Database normalization is the process of structuring a database, usually a relational database,
> in accordance with a series of so-called normal forms in order to reduce data redundancy and improve data integrity.

这是[中文版的定义][2]：

> 数据库规范化，又称正规化、标准化，是数据库设计的一系列原理和技术，以减少数据库中数据冗余，增进数据的一致性。

根据这个定义，数据库规范化的目的是 **减少数据冗余，增进数据一致性**。

## 为什么引入数据库范式

维基百科词条[「Database normalization」的「Objectives」一节][3]给出了原因，以下是我的简单概括：

- 增进数据一致性，避免数据更新/添加/删除出现异常。
- 提高数据库的拓展性，在拓展数据库时变动更小（代价更小）。

## 第一范式

这是维基百科词条[First normal form][4]的描述：

> First normal form (1NF) is a property of a relation in a relational database.
> A relation is in first normal form if and only if no attribute domain has relations as elements.
> Or more informally, that no table column can have tables as values (or no repeating groups).

这是[中文版的定义][5]:

> 第一范式（1NF）是数据库正规化所使用的正规形式。
> 第一范式是为了要排除 重复组 的出现，要求数据库的每个列的论域都是由不可分割的原子值组成；每个字段的值都只能是单一值。

维基百科词条[「Database normalization」的「Satisfying 1NF」一节][6]给出了以下描述：

> To satisfy First normal form, each column of a table must have a single value.
> Columns which contain sets of values or nested records are not allowed.

综上所述，第一范式要求数据库的每个字段由单一值组成，不能包含集合或嵌套的值。

## 第二范式

这是维基百科词条[Second normal form][10]给出的定义：

> A relation is in the second normal form if it fulfills the following two requirements:
>
> It is in first normal form.
> It does not have any non-prime attribute that is functionally dependent on any proper subset of any candidate key of the relation.
>
> Put simply, a relation is in 2NF if it is in 1NF and every non-prime attribute of the relation is dependent on the whole of every candidate key.

这是[极客时间课程《MySQL 必知必会》对「第二范式」的解释][12]：

> 第二范式：在满足第一范式的基础上，数据表中所有非主键字段，必须完全依赖全部主键字段，不能存在部分依赖主键字段的字段。

## 第三范式

这是维基百科词条[Third normal form][11]给出的定义：

> A database relation (e.g. a database table) is said to meet third normal form standards
> if all the attributes (e.g. database columns) are functionally dependent on solely the primary key.

该词条也提供了[Codd 对「第三范式」的定义」][11]:

> Codd's definition states that a table is in 3NF if and only if both of the following conditions hold:
>
> The relation R (table) is in second normal form (2NF).
> Every non-prime attribute of R is non-transitively dependent on every key of R.

这是[极客时间课程《MySQL 必知必会》对「第三范式」的解释][12]：

> 第三范式：在满足第二范式的基础上，数据表中不能存在可以被其他非主键字段派生出来的字段，或者说，不能存在依赖于非主键字段的字段。

## 一些核心概念

### Primary key （主键）

这是维基百科词条[Primary key][7]给出的定义：

> A primary key is a specific choice of a minimal set of attributes (columns) that uniquely specify a tuple (row) in a relation (table).

### Candidate key （候选键）

这是维基百科词条[Candidate key][8]给出的定义：

> A candidate key, or simply a key, of a relational database is a minimal superkey.
> In other words, it is any set of columns that have a unique combination of values in each row (which makes it a superkey),
> with the additional constraint that removing any column would possibly produce duplicate rows (which makes it a minimal superkey).

### Super key （超键）

这是维基百科词条[Super key][9]给出的定义：

> In the relational data model a superkey is a set of attributes that uniquely identifies each tuple of a relation.

  [1]: https://en.wikipedia.org/wiki/Database_normalization
  [2]: https://zh.wikipedia.org/wiki/%E6%95%B0%E6%8D%AE%E5%BA%93%E8%A7%84%E8%8C%83%E5%8C%96
  [3]: https://en.wikipedia.org/wiki/Database_normalization#Objectives
  [4]: https://en.wikipedia.org/wiki/First_normal_form
  [5]: https://zh.wikipedia.org/zh-cn/%E7%AC%AC%E4%B8%80%E6%AD%A3%E8%A6%8F%E5%8C%96
  [6]: https://en.wikipedia.org/wiki/Database_normalization#Satisfying_1NF
  [7]: https://en.wikipedia.org/wiki/Primary_key
  [8]: https://en.wikipedia.org/wiki/Candidate_key
  [9]: https://en.wikipedia.org/wiki/Superkey
  [10]: https://en.wikipedia.org/wiki/Second_normal_form
  [11]: https://en.wikipedia.org/wiki/Third_normal_form
  [12]: https://time.geekbang.org/column/article/367615
