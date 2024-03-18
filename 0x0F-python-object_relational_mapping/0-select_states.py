#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
Script should take 3 arguments: mysql username, mysql
password and database name
Uses the module MySQLdb
Connects to a MySQL server running on localhost at port 3306
Results are sorted in ascending order by states.id
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states")
    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)
