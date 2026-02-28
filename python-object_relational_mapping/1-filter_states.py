#!/usr/bin/python3
"""
Lists all states with a name starting with N (uppercase) from the database
hbtn_0e_0_usa.

Usage:
    ./1-filter_states.py <mysql username> <mysql password> <database name>

Requirements:
- Use MySQLdb
- Connect to localhost on port 3306
- Print rows sorted by states.id
- Match only names starting with uppercase 'N'
- Do not execute code on import
"""
import sys
import MySQLdb


def main():
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=user, passwd=passwd,
                         db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id",
                   ("N%",))
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
