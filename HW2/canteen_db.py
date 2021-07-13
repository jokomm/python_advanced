"""
TalTech Canteen Database.
This script creates a database of TalTech canteens with two tables.
Data is inserted as a list and as a separate statement.
Two queries are made and printed out
"""

import sqlite3

# Open the connection to database (Could not figure out how to do it as a function)
conn = sqlite3.connect('diner.db')
conn.execute("PRAGMA foreign_keys = ON")
print("Opened database successfully")
c = conn.cursor()


def create_tables():
    """Create tables for providers and canteens"""

    c.execute('''CREATE TABLE IF NOT EXISTS provider
                 (id integer PRIMARY KEY, 
                 provider_name text ) ''')

    print("Table provider created successfully")

    c.execute('''CREATE TABLE IF NOT EXISTS canteen
                 (id integer PRIMARY KEY,
                                    provider_id integer,
                                    name text, 
                                    location text, 
                                    time_open time, 
                                    time_closed time,
                                    FOREIGN KEY (provider_id) REFERENCES provider (id))''')
    print("Table canteen created successfully")


def createRecords():
    """Insert records into the tables."""

    # Declare TalTech providers list
    ttu_providers = [(1, "Rahva Toit"), (2, "Baltic Restaurants Estonia AS"), (3, "TTÜ Sport OU")]

    # Declare TalTech canteen list
    ttu_canteens = [
        (1, "Economics and social science building canteen", "Akadeemia tee 3 SOC building", "08:30:00", "18:30:00"),
        (1, "Library canteen", "Akadeemia tee 1/Ehitajate tee 7", "08:30:00", "19:00:00"),
        (2, "Main building Deli cafe", "Ehitajate tee 5 U01 building", "09:00:00", "16:30:00"),
        (2, "Main building Daily lunch restaurant", "Ehitajate tee 5 U01 building", "09:00:00", "16:30:00"),
        (1, "U06 building", "U06 building", "09:00:00", "16:00:00"),
        (2, "Natural Science building canteen", "Akadeemia tee 15 SCI building", "09:00:00", "16:00:00"),
        (2, "ICT building canteen", "Raja 15/Mäepealse 1", "09:00:00", "16:00:00"),
        (3, "Sports building canteen", "Männiliiva 7 S01 building", "11:00:00", "20:00:00")]

    # Adding data from the aboove lists
    c.executemany('INSERT INTO PROVIDER VALUES (?,?)', ttu_providers)
    c.executemany('INSERT INTO CANTEEN VALUES (NULL,?,?,?,?,?)', ttu_canteens)

    # Adding IT College diner to the table of providers
    c.execute('''INSERT INTO PROVIDER (provider_name) VALUES ("bitStop Kohvik OU")''')

    # Adding IT College diner to the table of canteens
    c.execute(
        '''INSERT INTO CANTEEN (provider_id, name, location, time_open, time_closed) VALUES (4, "bitStop KOHVIK", "IT College, Raja 4c", "9:30:00", "16:30:00")''')

    # Save (commit) the changes
    conn.commit()
    print("Records created successfully")


def print_result():
    """Create queries and print out the results."""

    # Query 1
    cursor = c.execute("""SELECT name FROM CANTEEN
                WHERE time_open < '16:15:00' and time_closed > '18:00:00'""")
    for row in cursor:
        print("NAME = ", row[0])

    # Query 2
    cursor = c.execute("""SELECT name FROM CANTEEN
                WHERE provider_id = (SELECT id FROM PROVIDER
                WHERE provider_name = "Rahva Toit")""")
    for row in cursor:
        print("NAME2 = ", row[0])


def closeconn():
    """ Close connection."""

    conn.close()
    print("Connection closed")


if __name__ == "__main__":
    create_tables()
    createRecords()
    print_result()
    closeconn()
