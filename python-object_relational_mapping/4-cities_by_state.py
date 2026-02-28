#!/usr/bin/python3
"""List all cities from the hbtn_0e_4_usa database.

Connect to a local MySQL server and print each row from the cities table
joined with its state name. Rows are ordered by cities.id in ascending
order. Only one execute() call is used.
"""

import sys

import MySQLdb


def fetch_cities(user, password, db_name):
    """Return rows of (city_id, city_name, state_name) ordered by city id."""
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=user,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    rows = cur.fetchall()
    cur.close()
    db.close()
    return rows


def main():
    """Read CLI args and print each city row as a tuple."""
    if len(sys.argv) != 4:
        return
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    for row in fetch_cities(user, password, db_name):
        print(row)


if __name__ == "__main__":
    main()
