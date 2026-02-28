#!/usr/bin/python3
"""List all states from the hbtn_0e_0_usa database.

The script connects to a local MySQL server and prints each row from the
states table ordered by id in ascending order.
"""

import MySQLdb
import sys


def fetch_states(user, password, db_name):
    """Connect to MySQL and return a tuple list of rows from states ordered by id."""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    cur.close()
    db.close()
    return rows


def main():
    """Read command-line arguments and print each state row as a tuple."""
    if len(sys.argv) != 4:
        return
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    for row in fetch_states(user, password, db_name):
        print(row)


if __name__ == "__main__":
    main()
