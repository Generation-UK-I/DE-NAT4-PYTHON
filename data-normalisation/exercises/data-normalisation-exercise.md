## Normalisation Exercise

### The Scenario

The below table contains information about members of a movie tracking website. The website allows registered members to create a list of the movies they have seen.

Assumptions:

- The column `member` (email address) is unique to a single customer, but different customers could have the same name
- Members can specify just one single favourite genre
- The columns `movies` and `movie_years` contain lists of the movies a member has seen and the year that movie was released.

### The Goal

Normalise the data by working through each normal form one-by-one from 1NF to 3NF.

For each stage note what tables exist, and what attributes (columns) they contain. You do not need to show the actual data contained in the table, but may do so if it helps!

If there is no violation of the rules of a given normal form, there may be nothing to do at that step.

`member_movies` table:

| member (KEY)      | fav_genre | username        | movies           | movie_years  |
|-------------------|-----------|-----------------|------------------|--------------|
| tomk@example.com  | Horror    | tommy-k         | The Shining      | 1980         |
| johnd@example.com | Romance   | the-movie-guy   | Titanic          | 1997         |
| janed@example.com | Comedy    | i-love-minions  | Titanic, Minions | 1997, 2015   |
| maryw@example.com | Horror    | horror-fan-1990 | The Shining, IT  | 1980, 2017   |

The rules for each normal form has been added to each exercise for ease of reference.

### Exercise 1 - 1NF

Normalise the data so it satisfies first normal form.

The rules for First Normal Form (1NF):

1. Unique name for attributes/columns: Each column should have a unique name
2. Order doesn't matter: The order in which columns or rows appear should not affect the data
3. Attribute Domain should not change: Values stored in a column must represent the same sort of information for all rows/records
4. Single Valued Attributes: Each column in the table should hold a single value.

### Exercise 2 - 2NF

Normalise the data so it satisfies second normal form.

The rules for Second Normal Form (2NF):

1. The table should already be in 1NF
2. The table should have no Partial Dependency

### Exercise 3 - 3NF

Normalise the data so it satisfies third normal form, if there is anything further to be done.

The rules for Third Normal Form (3NF):

1. The table should already be in 2NF
2. There should be no Transitive Dependency
