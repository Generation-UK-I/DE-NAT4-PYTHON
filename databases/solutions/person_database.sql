/*
Used in the Python part of the session.
Sample full set of SQL for the person table.
This file can be run in an Adminer window vs MySQL.
The `my_db_app_solution.py` file assumes this is the SQL that has been run in Adminer.
...and that the `databases/handouts/docker-compose.yml` matches what is running in docker.
*/

DROP DATABASE IF EXISTS test;

CREATE DATABASE test;

-- Select test database in the DB dropdown

CREATE TABLE person (
  person_id INTEGER GENERATED ALWAYS AS IDENTITY,
  first_name VARCHAR(255) NOT NULL,
  last_name VARCHAR(255) NOT NULL,
  age INTEGER,
  PRIMARY KEY(person_id)
);

ALTER TABLE person
ADD email varchar(255);

INSERT INTO person (first_name, last_name, age, email)
  VALUES ('Jane', 'Bloggs', 32, 'jane@email.com');

INSERT INTO person (first_name, last_name, age, email)
  VALUES ('Alice', 'Babbs', 45, 'alice@email.com');

INSERT INTO person (first_name, last_name, age, email)
  VALUES ('Mark', 'Smith', 51, 'mark@email.com');

INSERT INTO person (first_name, last_name, age, email)
  VALUES ('Grace', 'Matthews', 68, 'grace@email.com');

SELECT * FROM person ORDER BY person_id ASC;
