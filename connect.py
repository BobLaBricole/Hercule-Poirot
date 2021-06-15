#!/usr/bin/python3

import psycopg2

HOST = "//localhost:5432/"
USER = "postgres"
PASSWORD = "cluedo"
DATABASE = "fnaeg"

# Connect to an existing database

conn = psycopg2.connect("host=%s dbname=%s user=%s password=%s" % (HOST, DATABASE, USER, PASSWORD))
print (conn)

# Close connection

conn.close()
print (conn)