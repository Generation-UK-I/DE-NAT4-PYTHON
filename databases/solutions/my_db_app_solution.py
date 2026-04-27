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
    # Establish a database connection
    with psycopg.connect(f"""
        host={host_name}
        dbname={database_name}
        user={user_name}
        password={user_password}
        """) as connection:

        print('Opening cursor...')
        # A cursor is an object that represents a DB cursor,
        # which is used to manage the context of a fetch operation.
        cursor = connection.cursor()

        print('Inserting new record...')
        # Insert a new record (use RETURNING)
        sql = """
            INSERT INTO person (first_name, last_name, age, email)
            VALUES (%s, %s, %s, %s)
            RETURNING person_id, first_name, last_name
        """
        data_values = ('Jane', 'Doe', 20, 'jane_doe@invalidemail.com')
        cursor.execute(sql, data_values)
        rows = cursor.fetchall()  # returns a row array with a dictionary of column values in it e.g. [(123, will, robinson)]
        print('insert result id = ', rows[0])
        # Commit the record
        connection.commit()

        print('Selecting all records...')
        # Execute SQL query
        cursor.execute('SELECT first_name, last_name, age FROM person ORDER BY person_id ASC')
        # Fetch all the rows into memory
        rows = cursor.fetchall()
        print(rows)

        print('Displaying all records...')
        # Gets all rows from the result
        for row in rows:
            print(f'First Name: {row[0]}, Last Name: {row[1]}, Age: {row[2]}')

        # Can alternatively get one result at a time with the below code
        # while True:
        #     row = cursor.fetchone()
        #     if row == None:
        #         break
        #     print(f'First Name: {row[0]}, Last Name: {row[1]}, Age: {row[2]}')

        print('Closing cursor...')
        # Closes the cursor so will be unusable from this point
        cursor.close()

        # The connection will automatically close here
except Exception as ex:
    print('Failed to:', ex)

# Leave this line here!
print('All done!')
