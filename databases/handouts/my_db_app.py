############################################################
#
# This sample file assumes the learners have run commands on the db equivalent to `person_database.sql`
# and that the `databases/handouts/docker-compose.yml` file matches what is running in docker.
#
############################################################

import psycopg2 as psycopg
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host_name = os.environ.get("POSTGRES_HOST")
database_name = os.environ.get("POSTGRES_DB")
user_name = os.environ.get("POSTGRES_USER")
user_password = os.environ.get("POSTGRES_PASSWORD")

try:
    print('Opening connection...')
    # Connection string
    conn_string = f'host={host_name} dbname={database_name} user={user_name} password={user_password}'

    # TODO Establish a database connection
    # Hint: use "with ..."


    # This bit won't compile till the "with" is done...
    print('Opening cursor...')
    # TODO Add code here to open a cursor


    print('Inserting new record...')
    # TODO Add code here to insert a new record (use RETURNING)


    print('Committing...')
    # TODO Add code here to commit the INSERT


    print('Selecting all records...')
    # TODO Add code here to select all the records


    print('Displaying all records...')
    # TODO Add code here to print out all the records


    print('Closing cursor...')
    # TODO close the cursor


    # The connection will automatically close here
except Exception as ex:
    print('Failed to:', ex)

# Leave this line here!
print('All done!')
