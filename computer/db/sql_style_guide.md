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

### Tables

- Never give a table the same name as one of its columns and vice versa.

- Avoid, where possible, concatenating two table names together to create the name of a relationship table.
  - Rather than cars_mechanics prefer services.

### Columns

- Always use the singular name.

- **Where possible avoid simply using id as the primary identifier for the table.**

- Do not add a column with the same name as its table and vice versa.

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

### Choosing data types

- Only use REAL or FLOAT types where it is strictly necessary for floating point mathematics otherwise prefer NUMERIC and DECIMAL at all times.
  Floating point rounding errors are a nuisance!

### Specifying default values

- The default value must be the same type as the column—if a column is declared a DECIMAL do not provide an INTEGER default value.

- Default values must follow the data type declaration and come before any NOT NULL statement.

### Constraints and keys

- Keeping the key as simple as possible whilst not being scared to use compound keys where necessary.

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

  [1]: https://www.sqlstyle.guide/
  [2]: https://www.sqlshack.com/learn-sql-naming-conventions/
