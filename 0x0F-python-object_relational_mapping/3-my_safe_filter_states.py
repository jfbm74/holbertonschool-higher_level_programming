#!/usr/bin/python3
""" print all states start by N from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    MY_USER = sys.argv[1]
    MY_PASS = sys.argv[2]
    MY_DB = sys.argv[3]
    MY_PAR = sys.argv[4]

    MY_HOST = "localhost"

    db = MySQLdb.connect(
        host=MY_HOST,
        port=3306,
        user=MY_USER,
        passwd=MY_PASS,
        db=MY_DB)

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name=%s"
                "ORDER BY 'states.id';", (MY_PAR,))
    rows = cur.fetchall()
    for row in rows:
        print("{:}".format(row))
    cur.close()
    db.close()
