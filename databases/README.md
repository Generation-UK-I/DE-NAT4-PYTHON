# Databases

This module introduces learners to the key components of databases and database design. It's a large module with many topics so be sure not to set the pace too fast so learners have time to absorb it.

## Overview

- What is a database?
- SQL
- DDL / DML
- Modelling
- Connecting to a database from Python

## Timings

- This session is timetabled for 8 blocks at 1.5 hrs each, i.e. 2 elapsed training days
    - This is best split over 3 days to avoid learner fatigue
- The formative assessments occur during this and are included in that timing
- The exercises for this session (done in breakouts) are also included in that time

## Assessments

To check the learner progress in this session we have:

- Quizzes on DDL and DML
- Exercises in Breakouts on
    - Running a MySQL DB with Docker
    - Creating a DB
    - Creating tables
    - INSERT, UPDATE, DELETE
    - SELECT
    - JOINs
- Discussions on
    - INSERT, UPDATE, DELETE
    - SELECT
    - JOINS
- Emoji checks

## Prep

### Before the session

- Run through some of the JOINS W3C exercises yourself
    - https://www.w3resource.com/sql-exercises/sql-joins-exercises.php
    - The page is a little hard to navigate with all the ads in it, but it is a good resource
- Learners need to have Docker Desktop installed and running in advance
    - This should be good if the Docker session is run on the previous day
    - See the guidance in the [Docker README](../docker/README.md) session, there is troubleshooting info there
- Make sure everyone can at least run the following ok before the session starts:
    - `docker --version`
    - `docker pull mysql`
    - `docker pull adminer`
- Make sure everyone has cleaned out all old containers
    - This is also covered in the slides, as people will forget or just not do it.
    - tell them all to do this:
        - Run `docker ps -a`
        - If you have anything running, stop it with `docker stop <container_name>`
        - Remove all old containers with `docker rm <container_name>`
        - Run `docker ps -a` again - you should have zero containers now!

### For the session

- Create the session files (pdf and zip) using `make generate-session-files f=module_name`
- Review the slides and exercises
- Have the exercises PDF and zip file ready to distribute

For the instructor some useful files are provided;

- [./solutions/sample_session_results.sql](./solutions/sample_session_results.sql) - a file of all the sql an instructor might need to demo all the key points of the slides
- [./solutions/person_database.sql](./solutions/person_database.sql) - a file of all the sql needed to support the final Python exercise

## Session

- Run the slide deck
- Give learners plenty of time to attempt setting up a DB client and server in part 1 of the exercise handout
- Give learners plenty of time to attempt manipulating data in their new DB in part 2 of the exercise handout
- Give learners a reasonable amount of time to complete the W3 exercises - they can spend more time away from class to do them
- Try and get all learners by the end of the lesson to have them connect to their Database through the Python example code in the examples folder
