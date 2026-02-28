#!/usr/bin/python3
"""List all cities of a given state from hbtn_0e_4_usa (SQL injection safe).

Connects to a local MySQL server and prints city names for the provided
state name. The query is parameterized to prevent SQL injection and uses
a single execute() call. Results are ordered by cities.id.
"""

import sys

import MySQLdb


def fetch_cities(user, password, db_name, state_name):
    """Return a list of city names for state_name ordered by cities.id."""
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=user,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()
    cur.execute(
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s ORDER BY cities.id ASC",
        (state_name,)
    )
    rows = cur.fetchall()
    cur.close()
    db.close()
    return [row[0] for row in rows]


def main():
    """Parse command-line arguments and print cities separated by comma."""
    if len(sys.argv) != 5:
        return
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    cities = fetch_cities(user, password, db_name, state_name)
    if cities:
        print(", ".join(cities))
    else:
        print("")


if __name__ == "__main__":
    main()
