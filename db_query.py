# TASK 3 - QUERY THE SQLite DB AND GENERATE INFORMATION FROM THE DATA

import sqlite3
from datetime import datetime
from sqlite3 import Error
import os_stuff
import db_tools


def intro(db_name):
    os_stuff.clear()
    print("TASK 3 - QUERYING THE DB")
    print('------------------------')
    print(' ')
    print(f"In this step, you'll walk through pulling information from the DB file ({db_name})"
          f" in a structured manner.")
    print(' ')
    pause_me = input('Press any key to begin.')
    # print('')
    # print("DOH! This feature hasn't been implemented, yet! ")
    # print('#GracefulExit')


def query_menu(db_name):
    db = db_tools.sql_connection(db_name)
    print('Building menu...')
    cur = db.cursor()
    cur.execute('SELECT min(week_id) FROM music')
    min_year = int(cur.fetchone()[0][:4])
    cur.execute('SELECT max(week_id) FROM music')
    max_year = int(cur.fetchone()[0][:4])
    os_stuff.clear()
    print("DB contains data from " + str(min_year) + " to " + str(max_year) + ".")
    repeat = 1
    while repeat == 1:
        selected_year = input("Enter a year to explore: ")
        if int(selected_year) < min_year or int(selected_year) > max_year:
            print("Invalid year!")
            pause_me = input("Press any key to continue")
        else:
            repeat = 0
    ex_str = f'SELECT * FROM music WHERE week_id LIKE "%{selected_year}%" AND chart_position <= 10 GROUP BY song_id'
    print(ex_str)
    cur.execute(ex_str)
    db_response = cur.fetchall()
    for item in db_response:
        print(item[4] + " by " + item[5])



def db_query(db_name):
    intro(db_name)
    query_menu(db_name)
