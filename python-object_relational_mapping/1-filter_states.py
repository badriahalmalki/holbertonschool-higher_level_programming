#!/usr/bin/python3
"""
Lists all states with a name starting with N from the database hbtn_0e_0_usa.

Usage:
    ./1-filter_states.py <mysql username> <mysql password> <database name>

This module is documented to satisfy Holberton's requirement that the module
contains a top-level docstring. It connects to a MySQL server, queries the
`states` table for names beginning with 'N', and prints each matching row.
"""
import sys
import MySQLdb


def main():
    """
    Connect to the MySQL server and print states whose name starts with 'N'.

    Expects three command-line arguments: mysql username, mysql password,
    and database name. Uses a parameterized query to avoid SQL injection.
    """
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]), file=sys.stderr)
        sys.exit(1)

    user, passwd, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", user=user, passwd=passwd, db=db_name)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM `states` WHERE `name` LIKE %s ORDER BY `id`",
                       ("N%",))
        for state in cursor.fetchall():
            print(state)
    except MySQLdb.Error as e:
        print("MySQL error:", e, file=sys.stderr)
        sys.exit(1)
    finally:
        try:
            cursor.close()
            db.close()
        except Exception:
            pass


if __name__ == "__main__":
    main()
