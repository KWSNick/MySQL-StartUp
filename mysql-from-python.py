import os
import datetime
import pymysql

# Get username from Gitpod workspace
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        list_of_names = ['Jim', 'Bob']
        # Prepare a string with the same number of placehodlers as in list_of_names
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will still display a warning (not error) if the table already exists.
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit()
finally:
    # Close the connection, regardless of whether the above was successful
    connection.close()
