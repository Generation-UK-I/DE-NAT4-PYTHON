# Python Individual Challenge

At this point you're about half way through your first Python Project, and you will soon start to incorporate different technologies, therefore before we move on, we want to consolidate and evidence your individual progress.

To do so, we're going to ask you to apply the skills and strategies you've developed to complete an individual half day project sprint.

## Task Overview

As a developer, you are tasked with submitting a proposal for a solution to a client, which meets their requirements **as closely as possible**.

**You will complete the task in a single sprint of approximately 3 hours.**

At the end of the sprint you will be expected to submit a link to a GitHub repository containing your code, which you should create within your cohort's GitHub organisation (*ask your instructor to confirm if you do not know where this is*).

>All of the required files comprising your project should be present in the repository. Your instructor expects to be able to simple `clone` it, and run it. You may wish to test this by cloning into a clean test directory before submission.

One final requirement is to provide evidence of your planning; Ideally this will be in the form of screenshots (*or pictures of any hand-drawn diagrams or notes*) which are also uploaded to your repository. You may submit them via another method such as DM or email if you wish. An additional mark is available under the *best practice* criteria for submitting this evidence.

Submit your link using this [Google Form](https://forms.gle/gsj6fndQMVBqEVRF6)

### Assessment

Assessment criteria will be based upon meeting the clients requirements outlined in the **pseudo code**, with each one simply `met` or `not met`.

There are a total of **14** marks available for the main requirements. **4** additional marks for stretch goals, and **2** final marks for following coding best practices, for a total of **20**.

>The results are for internal use only, to ascertain suitable support options which may be offered to help you achieve your program outcomes.

## Client Requirements

The client requires a user management system to to sit in front of their customer facing applications.

The app should have the following features:

- An interface to add new users.
- A method of storing currently active users.
- A method of storing user accounts which are disabled.
- A way to view current active and disabled users.
- A way to manually disable/enable user accounts.

### Stretch Goals

If possible within the timescale, the client would also like:

- A password system with usernames and passwords stored together
- A method of testing login functionality (*i.e. verify that a provided username/password combo match an existing dictionary*)
- The user data should be persisted to a CSV or text file.

## Pseudo Code

>It is recommended that you read all of the pseudo code before commencing your project.

```text

START APP
    CREATE ACTIVE USER LIST
    CREATE DISABLED USER LIST

DISPLAY MENU:
    MENU ITEM 1 = ADD USER
    MENU ITEM 2 = VIEW ACTIVE AND DISABLED USER LISTS
    MENU ITEM 3 = ENABLE/DISABLE USERS
    MENU ITEM 0 = EXIT APP

IF MENU ITEM 1
    # CAPTURE USER INFO
    INPUT NEW USERNAME
    ADD TO USER LIST

IF MENU ITEM 2
    LIST ACTIVE USERS
    LIST DISABLED USERS

IF MENU ITEM 3
    DISABLE USER - MOVE TO DISABLED LIST
    ENABLE USER - MOVE TO ACTIVE LIST

IF MENU ITEM 0
    EXIT APP

# STRETCH GOAL

INCLUDE PASSWORDS
    EACH USER SHOULD BE A DICTIONARY WITH NAME AND PASSWORD KEYS
    USER LIST SHOULD BE A LIST OF DICTIONARIES
    ADD_USER FUNCTION CAPTURES USERNAME AND PASSWORD

CREATE MENU ITEM 4 = TEST LOGIN
    IF USERNAME AND PASSWORD INPUT == STORED USERNAME AND PASSWORD
    PRINT "ACCESS GRANTED"

PERSIST USERS TO CSV

# BEST PRACTICE

FUNCTIONS ARE SEPARATED FROM MAIN CODE

PROVIDE EVIDENCE OF PLANNING
```
