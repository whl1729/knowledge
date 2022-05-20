# SQL 样式指南

## General

- Object-oriented design principles should not be applied to SQL or database structures.

## Naming Conventions

- Avoid Plurals — use the more natural collective term where possible instead.
  - For example staff instead of employees or people instead of individuals.

- Keep the length to a maximum of 30 bytes —
  in practice this is 30 characters unless you are using a multi-byte character set.

- Names must begin with a letter and may not end with an underscore.

- Only use letters, numbers and underscores in names.

### Database

- 库名与应用名称尽量一致。

### Tables

- 表的命名最好是遵循「业务名称_表的作用」 。举例：`alipay_task/force_project/trade_config`。

- Always use **singular** for table names.

- If possible, use a single word that exactly describes what is in the table.
  If there is a need to use more than 1 word to describe what is in the table – do it so.

- Never give a table the same name as one of its columns and vice versa.

- For relations between two tables, it's good to use these two tables' names
  and maybe add a verb between these names to describe what that action is.

### Columns

- 数据库字段名的修改代价很大，因为无法进行预发布，所以字段名称需要慎重考虑。

- Always use the singular name.

- A primary key column
  - You should usually have only 1 column serving as a primary key.
  - It would be the best to simply name this column "id".
  - You should also name your PK constraint in a meaningful way. E.g., in our database, the PK of the call table is named call_pk.

- Foreign key columns
  - Since they store values from the range of primary key of the referenced table, you should use that table name and "id".

- Data columns
  - You should use the least possible words to describe what is stored in that column.

- Dates
  - For dates, it's good to describe what the date represents. Names like start_date and end_date are pretty descriptive.

- Flags
  - We could have flags marking if some action took place or not. We could use names like is_active, is_deleted.

- Do not add a column with the same name as its table and vice versa.

### Index

- 主键索引名为`pk_字段名`；唯一索引名为`uk_字段名`； 普通索引名则为`idx_字段名`。

### Aliasing or correlations

- Should relate in some way to the object or expression they are aliasing.

- As a rule of thumb the correlation name should be the first letter of each word in the object’s name.

- If there is already a correlation with the same name then append a number.

- Always include the AS keyword—makes it easier to read as it is explicit.

- For computed data (`SUM()` or `AVG()`) use the name you would give it were it a column defined in the schema.

### Stored procedures

- The name must contain a verb.

### Uniform suffixes

The following suffixes have a universal meaning ensuring the columns can be read and understood easily from SQL code.
Use the correct suffix where appropriate.

- `_id`: a unique identifier such as a column that is a primary key.
- `_status`: flag value or some other status of any type such as publication_status.
- `_total`: the total or sum of a collection of values.
- `_num`: denotes the field contains any kind of number.
- `_name`: signifies a name such as first_name.
- `_seq`: contains a contiguous sequence of values.
- `_date`: denotes a column that contains the date of something.
- `_tally`: a count.
- `_size`: the size of something such as a file size or clothing.
- `_addr`: an address for the record could be physical or intangible such as ip_addr.

## Comments

- Include comments in SQL code where necessary.

- Use the C style opening `/*` and closing `*/` where possible
  otherwise precede comments with `--` and finish them with a new line.

## Create syntax

- 表必备三字段：`id`, `create_time`, `update_time`。
  - 其中`id`必为主键，类型为`bigint unsigned`、单表时自增、步长为 1。
  - `create_time`, `update_time` 的类型均为`datetime`类型，前者现在时表示主动式创建，后者过去分词表示被动式更新。

- 字段允许适当冗余，以提高查询性能，但必须考虑数据一致。冗余字段应遵循：
  - 不是频繁修改的字段。
  - 不是唯一索引的字段。
  - 不是`varchar`超长字段，更不能是`text`字段。

- 单表行数超过 500 万行或者单表容量超过 2GB，才推荐进行分库分表。
  - 如果预计三年后的数据量根本达不到这个级别，请不要在创建表时就分库分表。

- 禁止使用存储过程，存储过程难以调试和扩展，更没有移植性。

### Choosing data types

- Only use REAL or FLOAT types where it is strictly necessary for floating point mathematics otherwise prefer NUMERIC and DECIMAL at all times.
  Floating point rounding errors are a nuisance!

- 表达是与否概念的字段，必须使用`is_xxx`的方式命名，数据类型是`unsigned tinyint`（1 表示「是」， 0 表示「否」）。

- 小数类型为`decimal`，禁止使用`float`和`double`。

- 如果存储的字符串长度几乎相等，使用`char`定长字符串类型。

- `varchar`是可变长字符串，不预先分配存储空间，长度不要超过 5000.
  如果存储长度大于此值，定义字段类型为`text`，独立出来一张表，用主键来对应，避免影响其它字段索引效率。

### Specifying default values

- The default value must be the same type as the column—if a column is declared a DECIMAL do not provide an INTEGER default value.

- Default values must follow the data type declaration and come before any NOT NULL statement.

### Constraints and keys

- Keeping the key as simple as possible whilst not being scared to use compound keys where necessary.

- 不得使用外键与级联，一切外键概念必须在应用层解决。
  - 外键与级联更新适用于单机低并发，不适合分布式、高并发集群；
  - 级联更新是强阻塞，存在数据库更新风暴的风险；
  - 外键影响数据库的插入速度。

#### Constraints' Layout and order

- Specify the primary key first right after the `CREATE TABLE` statement.

- Constraints should be defined directly beneath the column they correspond to.
  Indent the constraint so that it aligns to the right of the column name.

- If it is a multi-column constraint then consider putting it as close to both column definitions as possible
  and where this is difficult as a last resort include them at the end of the `CREATE TABLE` definition.

- If it is a table-level constraint that applies to the entire table then it should also appear at the end.

- Use alphabetical order where `ON DELETE` comes before `ON UPDATE`.

#### Constraints' validation

- Use `LIKE` and `SIMILAR` TO constraints to ensure the integrity of strings where the format is known.

- Where the ultimate range of a numerical value is known it must be written as a range `CHECK()`
  to prevent incorrect values entering the database or the silent truncation of data too large to fit the column definition.
  In the least it should check that the value is greater than zero in most cases.

- `CHECK()` constraints should be kept in separate clauses to ease debugging.

### Create Index

- 业务上具有唯一特性的字段，即使是组合字段，也必须建成唯一索引。
  - 不要以为唯一索引影响了 insert 速度，这个速度损耗可以忽略，但提高查找速度是明显的；
  - 另外，即使在应用层做了非常完善的校验控制，只要没有唯一索引，根据墨菲定律，必然有脏数据产生。

- 超过三个表禁止 join。
  - 需要 join 的字段，数据类型保持绝对一致；
  - 多表关联查询时，保证被关联的字段需要有索引。

- 在 varchar 字段上建立索引时，必须指定索引长度，没必要对全字段建立索引，根据实际文本区分度决定索引长度。

- 如果有 order by 的场景，请注意利用索引的有序性。
  - order by 最后的字段是组合索引的一部分，并且放在索引组合顺序的最后，避免出现 file_sort 的情况，影响查询性能。

- 利用覆盖索引来进行查询操作，避免回表。

- 建组合索引的时候，区分度最高的在最左边。

- 防止因字段类型不同造成的隐式转换， 导致索引失效。

- 创建索引时避免有如下极端误解：
  - 索引宁滥勿缺。 认为一个查询就需要建一个索引。
  - 吝啬索引的创建。 认为索引会消耗空间、 严重拖慢记录的更新以及行的新增速度。
  - 抵制惟一索引。 认为惟一索引一律需要在应用层通过「先查后插」方式解决。

## Designs to avoid

- Object-oriented design principles do not effectively translate to relational database designs — avoid this pitfall.

- Placing the value in one column and the units in another column.
  The column should make the units self-evident to prevent the requirement to combine columns again later in the application.
  Use `CHECK()` to ensure valid data is inserted into the column.

- Entity–Attribute–Value (EAV) tables — use a specialist product intended for handling such schema-less data instead.

- Splitting up data that should be in one table across many tables because of arbitrary concerns such as time-based archiving or location in a multinational organisation.
  Later queries must then work across multiple tables with UNION rather than just simply querying one table.

## 参考资料

- [SQL Style Guide][1]
- [Learn SQL: Naming Conventions][2]
- [阿里云数据库设计规范][3]

  [1]: https://www.sqlstyle.guide/
  [2]: https://www.sqlshack.com/learn-sql-naming-conventions/
  [3]: https://developer.aliyun.com/article/709387
