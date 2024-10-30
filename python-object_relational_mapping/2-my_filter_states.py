#!/usr/bin/python3

"""
This module contains a script to list states from hbtn_0e_0_usa
who match the name provided as an argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
    cur = conn.cursor()

    # Vulnérable à l'injection SQL
    query = (
        "SELECT * FROM states "
        "WHERE name LIKE '{}%' "
        "ORDER BY id ASC"
    ).format(argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
