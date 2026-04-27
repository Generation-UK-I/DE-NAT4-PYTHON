/*
This file represents the full output of tables, relations and data one might generate as an instructor while running the session.
*/

-- Select data_engineering database in the DB dropdown

DROP TABLE IF EXISTS learner_classes;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS phone_numbers;
DROP TABLE IF EXISTS learners;
DROP TABLE IF EXISTS cohorts;

CREATE TABLE cohorts (
  cohort_id INTEGER GENERATED ALWAYS AS IDENTITY,
  name VARCHAR(100) NOT NULL,
  PRIMARY KEY(cohort_id)
);

ALTER TABLE cohorts ADD description VARCHAR(1000);

CREATE TABLE learners (
  learner_id INTEGER GENERATED ALWAYS AS IDENTITY,
  first_name VARCHAR(20) NOT NULL,
  last_name VARCHAR(20) NOT NULL,
  email VARCHAR(100),
  cohort_id INTEGER,
  PRIMARY KEY(learner_id),
  FOREIGN KEY(cohort_id) REFERENCES cohorts(cohort_id)
);

CREATE TABLE phone_numbers (
  phone_number_id INTEGER GENERATED ALWAYS AS IDENTITY,
  phone_number VARCHAR(20) NOT NULL,
  learner_id INTEGER NOT NULL,
  PRIMARY KEY(phone_number_id),
  FOREIGN KEY(learner_id) REFERENCES learners(learner_id)
);

CREATE TABLE classes (
  class_id INTEGER GENERATED ALWAYS AS IDENTITY,
  class_name VARCHAR(20) NOT NULL,
  PRIMARY KEY(class_id)
);

CREATE TABLE learner_classes (
  learner_id INTEGER NOT NULL,
  class_id INTEGER NOT NULL,
  PRIMARY KEY(learner_id, class_id),
  FOREIGN KEY(learner_id) REFERENCES learners(learner_id),
  FOREIGN KEY(class_id) REFERENCES classes(class_id)
);

INSERT INTO cohorts (name, description)
VALUES ('DELON9', 'What a bunch of lovely people on the Data Engineering London Cohort');
INSERT INTO cohorts (name, description)
VALUES ('LEEDS01', 'What a bunch of lovely people on the Data Engineering Leeds Cohort');
INSERT INTO cohorts (name, description)
VALUES ('MAN02', 'What a bunch of lovely people on the Data Engineering Manchester Cohort');

INSERT INTO learners (first_name, last_name, cohort_id) VALUES ('KATE', 'BUSH', 2);
INSERT INTO learners (first_name, last_name, cohort_id) VALUES ('JACK', ' Bennit', 3);
INSERT INTO learners (first_name, last_name, cohort_id) VALUES ('Paul', 'Ma', 1);
INSERT INTO learners (first_name, last_name, cohort_id) VALUES ('Jane', 'Trotsky', 3);

INSERT INTO phone_numbers (phone_number, learner_id) VALUES ('1234', 1);
INSERT INTO phone_numbers (phone_number, learner_id) VALUES ('2345', 2);
INSERT INTO phone_numbers (phone_number, learner_id) VALUES ('3456', 3);
INSERT INTO phone_numbers (phone_number, learner_id) VALUES ('4567', 4);

INSERT INTO classes (class_name) VALUES ('Docker');
INSERT INTO classes (class_name) VALUES ('Databases');
INSERT INTO classes (class_name) VALUES ('AWS cool stuff');
INSERT INTO classes (class_name) VALUES ('Warhammer 101');

INSERT INTO learner_classes (learner_id, class_id) VALUES (1, 2);
INSERT INTO learner_classes (learner_id, class_id) VALUES (1, 3);
INSERT INTO learner_classes (learner_id, class_id) VALUES (2, 2);
INSERT INTO learner_classes (learner_id, class_id) VALUES (3, 3);
INSERT INTO learner_classes (learner_id, class_id) VALUES (4, 1);
INSERT INTO learner_classes (learner_id, class_id) VALUES (4, 2);

SELECT * FROM cohorts;
SELECT * FROM learners;
SELECT * FROM phone_numbers;
SELECT * FROM cohorts;
SELECT * FROM learner_classes;

SELECT l.*, c.*
FROM learners l
JOIN learner_classes lc ON l.learner_id = lc.learner_id
JOIN classes c ON lc.class_id = c.class_id;
