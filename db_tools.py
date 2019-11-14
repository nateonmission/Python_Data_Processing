import sqlite3
from _sqlite3 import Error


def sql_connection(db_name):
    try:
        db = sqlite3.connect(db_name)
        print("Connection to database has been established")
        return db
    except Error:
        print(Error)
