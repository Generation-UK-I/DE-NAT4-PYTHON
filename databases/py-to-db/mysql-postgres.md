# MySQL vs Postgres Syntax

There are a number of different Relational Database Management Systems (RDBMS), that can have small or large differences between them, and different use cases they're tailored for. A few examples of common RDBMS' include:

- MySQL: Commonly used for web application back-ends, content management systems, and e-commerce. Known for reliability and performance.
- PosgreSQL: Good for complex apps and financial modelling. Known for advanced compliance and extensibility.
- Microsoft SQL Server: Good for business intelligence and analytics, deeply integrated with MS' ecosystem.
- SQLite: Used for mobile apps, embedded systems, designed for lightweight storage.

>Note relational databases and SQL databases are the same thing.

## DE-NAT4 Databases - April '26

As you know, we've been trying to implement a more practical approach to the technical modules, in the case of databases Generation has a module which we've used for other programs, but unfortunately it is based on MySQL. 

Luckily, the syntax between them is very similar, but not identical. Therefore, you should work through this guide to learn about SQL databases, but also bear in mind the following differences between MySQL and Postgres.

### Comparison Table

|Difference|MySQL|Postgres|
|---|---|---|
|String Concatenation|`CONCAT('Hello', ' ', 'World')` or `'Hello' 'World'`|`'Hello' || ' ' || 'World'`|
||||