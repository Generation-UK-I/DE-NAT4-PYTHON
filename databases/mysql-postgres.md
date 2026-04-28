# MySQL vs Postgres Syntax

There are a number of different Relational Database Management Systems (RDBMS), that can have small or large differences between them, and different use cases they're tailored for. A few examples of common RDBMS' include:

- MySQL: Commonly used for web application back-ends, content management systems, and e-commerce. Known for reliability and performance.
- PosgreSQL: Good for complex apps and financial modelling. Known for advanced compliance and extensibility.
- Microsoft SQL Server: Good for business intelligence and analytics, deeply integrated with MS' ecosystem.
- SQLite: Used for mobile apps, embedded systems, designed for lightweight storage.

>Note relational databases and SQL databases are the same thing.

## DE-NAT4 Databases - April '26

As you know, we've been trying to implement a more practical approach to the technical modules, in the case of databases Generation has a module which we've used for other programs, but unfortunately it is based on MySQL.

Luckily, the syntax between them is very similar, but not identical. Therefore, you should read through this guide to learn about SQL databases, but also bear in mind the following differences between MySQL and Postgres.

### Comparison Table

|Difference|MySQL|Postgres|
|---|---|---|
|String Concatenation|`CONCAT('Hello', ' ', 'World')` or `'Hello' 'World'`|`'Hello' \|\| ' ' \|\| 'World'`|
|LIMIT / OFFSET|`LIMIT 10 OFFSET 5` or `LIMIT 5, 10`|`LIMIT 10 OFFSET 5` (same, but no comma syntax)|
|ILIKE for case-insensitive search|`LIKE` (case-insensitive by default)|`ILIKE` for case-insensitive (standard `LIKE` is case-sensitive)|
|Auto-increment / Serial|`id INT AUTO_INCREMENT PRIMARY KEY`|`id SERIAL PRIMARY KEY` or `id INTEGER GENERATED ALWAYS AS IDENTITY`|
|Boolean Literals|`TRUE`/`FALSE` (actually 1/0, stored as TINYINT)|Proper `TRUE`/`FALSE` as `BOOLEAN` type|
|Date/Time Intervals|`INTERVAL 7 DAY`, `DATE_ADD(NOW(), INTERVAL 1 MONTH)`|`NOW() + INTERVAL '7 days'`, `NOW() + INTERVAL '1 month'`|
|Regular Expressions|`REGEXP` or `RLIKE`|`~` (case-sensitive), `~*` (case-insensitive)|
|String Functions: Length|`LENGTH()`|`LEN()` or `CHAR_LENGTH()`|
|String Functions: Position|`LOCATE('sub', str)`|`POSITION('sub' IN str)`|
