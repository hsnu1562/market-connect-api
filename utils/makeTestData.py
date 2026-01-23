import os
import psycopg2 as pg2
from dotenv import load_dotenv   


load_dotenv()
conn = pg2.connect(os.getenv("DATABASE_URL"))
cur = conn.cursor()

# 1. Create a dummy user (User ID 1)
print("Creating User...")
cur.execute("INSERT INTO users (line_uid, name) VALUES ('U12345', 'Test User') ON CONFLICT DO NOTHING;")

# 2. Create a time slot for Stall ID 1 (Slot ID will be auto-generated, likely 1)
print("Creating Time Slot...")
cur.execute("""
    INSERT INTO availability (stall_id, date, price, status) 
    VALUES (1, '2026-02-01', 500, 0); 
""")

conn.commit()
print("Data ready!")