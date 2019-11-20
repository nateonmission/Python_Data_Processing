# TASK 2 - LOAD DATA INTO A SQL DATABASE

import sqlite3
from datetime import datetime
from sqlite3 import Error
import os_stuff
import db_tools


def build_db(db_name, data_list):
    os_stuff.clear()
    print('TASK 2 - LOAD THE LIST FROM TASK 1 INTO A SQLite DATABASE')
    print('---------------------------------------------------------')
    print(' ')
    print(f'Each line from the original CSV will be parsed and saved to a SQLite DB called {db_name},')
    print(f"which will be saved to the current directory. First, let's built the DB")
    print(' ')
    pause_me = input('Press ENTER key to begin.')

    def create_sql_table(db):
        cursor_obj = db.cursor()
        cursor_obj.execute(
            "CREATE TABLE music(id integer PRIMARY KEY, url text, week_id text, chart_position intiger, song_title text, artist text, song_id text)"
        )
        db.commit()

    db = db_tools.sql_connection(db_name)
    create_sql_table(db)
    print("DB has been built")
    pause_me = input('Press ENTER key to continue')


def load_data_into_db(db_name, data_list):
    print("Now, let's load that DB with the data from our data list.")
    print("This will take a minute... or ten... or more... Seriously, do you have a book to read?")
    print(" ")
    pause_me = input("Press ENTER key to continue.")

    def insert_data(db, data_list):
        cursor_obj = db.cursor()
        i = 0
        for list_item in data_list:
            datetime_object = datetime.strptime(list_item[1], '%m/%d/%Y')
            index = i
            url = str(list_item[0])
            date_ref = str(datetime_object)
            chart_pos = int(list_item[2])
            title = list_item[3]
            artist = list_item[4]
            song_id = list_item[5]
            print('Loading ' + title + ' by ' + artist + ' (week of ' + date_ref + ')')
            print(str(index) + ' of ' + str(len(data_list)))
            cursor_obj.execute(
                f'INSERT INTO music VALUES(?,?,?,?,?,?,?)', (
                    index, url, date_ref, chart_pos, title, artist, song_id
                )
            )
            i += 1
            db.commit()

    db = db_tools.sql_connection(db_name)
    insert_data(db, data_list)
    db.close()
    print("Whew... So, that's done.")
    pause_me = input('Press ENTER key to continue.')
