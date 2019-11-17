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
    repeat = 1
    while repeat == 1:
        os_stuff.clear()
        print('******************** PICK A QUERY ********************')
        print('01 - Songs in Top 10 for a given year')
        print('02 - Songs in Top 10 for a given year and month')
        print('03 - Search by Artist')
        print('99 - EXIT')
        print('')
        selection = input("Query number: ")
        if selection.isdigit():
            if int(selection) == 1:
                top_10_by_year(db_name)
                repeat = 1
            elif int(selection) == 2:
                top_10_by_yr_and_mo(db_name)
                repeat = 1
            elif int(selection) == 3:
                query_by_artist(db_name)
                repeat = 1
            elif int(selection) == 99:
                break
            else:
                pass
        else:
            pass
    print('GOOD BYE')


def top_10_by_year(db_name):
    db = db_tools.sql_connection(db_name)
    print('opening data...')
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
    db_response = date_query(cur, selected_year)
    print_db_results(db_response)
    db.close()


def top_10_by_yr_and_mo(db_name):
    db = db_tools.sql_connection(db_name)
    print('opening data...')
    cur = db.cursor()
    cur.execute('SELECT min(week_id) FROM music')
    min_year = int(cur.fetchone()[0][:4])
    cur.execute('SELECT max(week_id) FROM music')
    max_year = int(cur.fetchone()[0][:4])
    os_stuff.clear()
    print("DB contains data from " + str(min_year) + " to " + str(max_year) + ".")
    repeat = 1
    while repeat == 1:
        selected_year = input("Enter a year: ")
        if not selected_year.isdigit():
            print("Invalid year!")
            pause_me = input("Press any key to continue")
        elif int(selected_year) < min_year or int(selected_year) > max_year:
            print("Invalid year!")
            pause_me = input("Press any key to continue")
        else:
            repeat = 0
    repeat = 1
    while repeat == 1:
        selected_month = input("Enter a month as a 2 digit number (e.g. May = 05): ")
        if not selected_month.isdigit():
            print("Invalid month!")
            pause_me = input("Press any key to continue")
        elif int(selected_month) < 1 or int(selected_month) > 12:
            print("Invalid month!")
            pause_me = input("Press any key to continue")
        else:
            repeat = 0
    date_string = selected_year + "-" + selected_month
    db_response = date_query(cur, date_string)
    print_db_results(db_response)
    db.close()


def query_by_artist(db_name):
    db = db_tools.sql_connection(db_name)
    print('opening data...')
    cur = db.cursor()
    selected_artist = input("Enter a SOLO ARTIST or a BAND: ")
    ex_str = f'SELECT * FROM music WHERE artist LIKE "%{selected_artist}%" AND chart_position <= 10 GROUP BY song_id'
    cur.execute(ex_str)
    db_response = cur.fetchall()
    print_db_results(db_response)
    db.close()


def date_query(cur, date_string):
    ex_str = f'SELECT * FROM music WHERE week_id LIKE "%{date_string}%" AND chart_position <= 10 GROUP BY song_id'
    cur.execute(ex_str)
    db_response = cur.fetchall()
    return db_response


def print_db_results(db_response):
    for item in db_response:
        print(item[4] + " by " + item[5])
    print('')
    print(str(len(db_response)) + " total songs found.")
    pause_me = input('Press any key to continue')


def db_query(db_name):
    intro(db_name)
    query_menu(db_name)
