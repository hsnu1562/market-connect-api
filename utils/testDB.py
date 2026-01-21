import os
import psycopg2 as pg2
from dotenv import load_dotenv  

load_dotenv()  # take environment variables from .env file

# get db url from .env
DB_URL = os.getenv("DATABASE_URL")

if not DB_URL:
    raise ValueError("No DATABASE_URL found! Check your .env file.")

try:
	print("Attempting to connect")

	# establish the connection
	conn = pg2.connect(DB_URL)
	print("connection successful")

	# create a cursor
	# The cursor is the tool that actually writes the SQL and fetches results
	cur = conn.cursor()

	# execute a query (sending a message)
	cur.execute("SELECT version();")

	# fetch the result
	db_version = cur.fetchone()
	print(f"database version: {db_version}")

	# clean up
	cur.close()
	conn.close()
	print("connection closed");

except Exception as e:
	print("an error occured!")
	print(e)
