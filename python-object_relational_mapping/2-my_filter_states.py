#!/usr/bin/python3

"""
This module containt a script to list state from hbtn_0e_0_usa
who write in 4th arguments.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    search_term = argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
                (search_term + '%',))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
