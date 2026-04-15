# Docker

## Overview

- A Brief History of Software Delivery
- An Introduction to Docker
- Commands to work with Docker containers
- Creating your own Docker containers
- Sharing your containers with the world

## Timings

- This session is timetabled for 2 blocks at 1.5 hrs each, so 0.5 day
- The formative assessments occur during this and are included in that timing
- The exercises for this session (done in breakouts) are also included in that time

## Assessments

To check the learner progress in this session we have:

- Quizzes on Docker fundamentals
- Periodic emoji checks
- Exercises on docker commands, building a dockerfile, and docker-compose

## Prep

### Important! - the day before, if not earlier...

This is critical otherwise some learners will be unable to take part in this session or the following Databases session, which uses a MySQL container.

- Get everyone to validate docker works
    - This can take a several hours so allow time i.e. in Project time, especially as there will be a random collection of laptops being used with random different issues
    - get everyone to _successfully_ run:

    ```bash
    docker --version
    ```

- Get everyone to pull the required images for the session:

    ```bash
   docker pull docker/whalesay
   docker pull debian
   docker pull python:3.9
   docker pull adminer
   docker pull mysql
   ```

### Common setup issues and FAQ type stuff

- In the motherboard BIOS, "Virtualisation" must be enabled - it may be off on personal / non-work machines especially. And can be called something else. _Usually_ this being disabled results in a specific error message when starting Docker Desktop.
- Docker needs Admin privileges, so make sure people run the installer as an Admin, esp on Windows.
- In Windows, you need a clean setup of WSL2. Make sure there are no old VMS with `docker` in the name before installing (see commands below).
- Useful Stack Overflows:
    - ["Docker Desktop Starting..." forever on Windows](https://stackoverflow.com/questions/71238673/docker-desktop-starting-forever-on-windows/71258405#71258405)
    - [Docker forever in "Docker is starting.." at Windows task](https://stackoverflow.com/questions/43041331/docker-forever-in-docker-is-starting-at-windows-task)
    - [Ubuntu WSL with docker could not be found](https://stackoverflow.com/questions/63497928/ubuntu-wsl-with-docker-could-not-be-found/67688891#67688891)
- If docker desktop starts, check the settings, esp on Windows, match the virtualisation you are using i.e. WSL2, not older engines.
- A complete "reinstall all" set for Windows;
    - Uninstall docker from Settings
    - Uninstall wsl from Settings
    - Shut down, count to 10 (cold boot)
    - Startup
    - Make sure wsl is up to date; In an Admin powershell terminal try these;
        - `wsl --install`
        - `wsl -v` the version should be 2, if not run `wsl --set-default-version 2`
        - `wsl --list --online`  (list all available Unix versions)
        - `wsl --install Ubuntu`
        - `wsl -l -v` list local versions, should only have Ubuntu v2 in it
    - if there are any docker wsl vms listed, remove them, e.g;
        - `wsl --unregister docker-desktop`
        - `wsl --unregister docker-desktop-data`
    - re-install Docker desktop as admin

### On the day (if not before!)

- Create the session files (pdf and zip) using `make generate-session-files f=module_name`
- Review the slides and exercises

## Session

- Run the presentation
- For every command you show on the slides or run, get the learners to repeat it for themselves
    - But - _do not_ let the class push to docker hub! - this takes ages and will require them all to be logged into it locally - this can be a big time sink!
- Distribute the cheatsheet
- The final exercise of "Dockerise the mini project" is probably best done in groups of around 4, usually offline in Project time.
