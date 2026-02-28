#!/usr/bin/python3
"""Safe filter: list states matching a given name from hbtn_0e_0_usa.

Connects to a local MySQL server and prints each row from the states table
where the name matches the provided argument. The query uses parameterized
arguments to prevent SQL injection. Results are ordered by id.
"""

import sys

import MySQLdb


def fetch_states_safe(user, password, db_name, state_name):
    """Return rows from states where name equals state_name (safe query)."""
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=user,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC",
                (state_name,))
    rows = cur.fetchall()
    cur.close()
    db.close()
    return rows


def main():
    """Read CLI args and print each matching state row as a tuple."""
    if len(sys.argv) != 5:
        return
    user = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    for row in fetch_states_safe(user, password, db_name, state_name):
        print(row)


if __name__ == "__main__":
    main()
