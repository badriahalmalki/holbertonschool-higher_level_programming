#!/usr/bin/python3
"""Filter states by name from the hbtn_0e_0_usa database.

The script connects to a local MySQL server and prints each row from the
states table where the name matches the provided argument exactly and
case-sensitively. Rows are ordered by id in ascending order.
"""

import sys

import MySQLdb


def fetch_states_by_name(user, password, db_name, state_name):
    """Return rows from states where name matches state_name
    (case-sensitive)."""
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=user,
                         passwd=password,
                         db=db_name)
    cur = db.cursor()
    # Escape single quotes in state_name to avoid SQL syntax errors.
    safe_name = state_name.replace("'", "\\'")
    query = ("SELECT * FROM states WHERE BINARY name = '{}' "
             "ORDER BY id ASC".format(safe_name))
    cur.execute(query)
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
    for row in fetch_states_by_name(user, password, db_name, state_name):
        print(row)


if __name__ == "__main__":
    main()
