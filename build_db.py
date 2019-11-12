# TASK 2 - LOAD DATA INTO A SQL DATABASE
import sqlite3
from datetime import datetime
from sqlite3 import Error


def build_db(db_name, data_list):
    def sql_connection(db_name):
        try:
            db = sqlite3.connect(db_name)
            print("Connection to database has been established")
            return db
        except Error:
            print(Error)

    def create_sql_table(db):
        cursor_obj = db.cursor()
        cursor_obj.execute(
            "CREATE TABLE music(id integer PRIMARY KEY, url text, week_id text, chart_position intiger, song_title text, artist text, song_id text)"
        )
        db.commit()

    db = sql_connection(db_name)
    create_sql_table(db)
    print("DB has been built")


def load_data_into_db(db_name, data_list):
    def sql_connection(db_name):
        try:
            db = sqlite3.connect(db_name)
            print("Connection to database has been established")
            return db
        except Error:
            print(Error)

    def insert_data(db, data_list):
        cursor_obj = db.cursor()
        i = 0
        for list_item in data_list:
            datetime_object = datetime.strptime(list_item[1], '%m/%d/%Y')
            index = i
            print(index)
            print(type(index))
            url = str(list_item[0])
            print(url)
            print(type(url))
            date_ref = str(datetime_object)
            print(date_ref)
            print(type(date_ref))
            chart_pos = int(list_item[2])
            print(chart_pos)
            print(type(chart_pos))
            title = list_item[3]
            print(title)
            print(type(title))
            artist = list_item[4]
            print(artist)
            print(type(artist))
            song_id = list_item[5]
            print(song_id)
            print(type(song_id))
            cursor_obj.execute(
                f'INSERT INTO music VALUES(?,?,?,?,?,?,?)', (
                    index, url, date_ref, chart_pos, title, artist, song_id
                )
            )
            i += 1
            db.commit()

    db = sql_connection(db_name)
    insert_data(db, data_list)

    # db_index = i
    # db_url = list_item[0]
    # db_date = list_item[1]
    # db_position = list_item[2]
    # db_title = list_item[3]
    # db_artist = list_item[4]
    # db_id = list_item[5]
    # db_prev = list_item[6]
    # db_peak = list_item[7]
    # db_dur = list_item[8]
