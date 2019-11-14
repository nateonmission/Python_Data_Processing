# TASK 3 - QUERY THE SQLite DB AND GENERATE INFORMATION FROM THE DATA

import sqlite3
from datetime import datetime
from sqlite3 import Error
import os_stuff


def intro(db_name):
    os_stuff.clear()
    print("TASK 3 - QUERYING THE DB")
    print('------------------------')
    print(' ')
    print(f"In this step, you'll walk through pulling information from the DB file ({db_name})"
          f" in a structured manner.")
    print(' ')
    pause_me = input('Press any key to begin.')
    print('')
    print("DOH! This feature hasn't been implemented, yet! ")
    print('#GracefulExit')


def db_query(db_name):
    intro(db_name)
