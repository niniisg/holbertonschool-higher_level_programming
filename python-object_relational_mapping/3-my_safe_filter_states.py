#!/usr/bin/python3

"""
writing a script that takes arguments and displays all values
in the states and matches argument
"""

import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
        charset="utf8",
    )
    cur = conn.cursor()
    cur.execute(
        """SELECT * FROM states WHERE name = %s
                ORDER BY states.id ASC""", (sys.argv[4],)
    )
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == sys.argv[4]:
            print(row)
    cur.close()
    conn.close()
