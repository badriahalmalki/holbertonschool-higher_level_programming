#!/usr/bin/python3
"""List states with a name starting with N from hbtn_0e_0_usa.

Connect to a local MySQL server and print each row from the states table
where the name starts with an uppercase N. Rows are ordered by id.
"""

import sys

import MySQLdb


def fetch_states_starting_with_n(user, password, db_name):
    """Return rows from states where name starts with 'N', ordered by id."""
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=user, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                ("N%",))
    rows = cur.fetchall()
    cur.close()
    db.close()
    return rows


def main():
    """Read CLI args and print each matching state row as a tuple."""
    if len(sys.argv) != 4:
        return
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    for row in fetch_states_starting_with_n(user, password, db_name):
        print(row)


if __name__ == "__main__":
    main()
