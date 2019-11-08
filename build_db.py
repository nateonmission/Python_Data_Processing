# TASK 2 - LOAD DATA INTO A SQL DATABASE
import sqlite3
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
            "CREATE TABLE music(id integer PRIMARY KEY, url text, week_id date, chart_position intiger, song_title text, artist text, song_id text, prev_week intiger, peak_position intiger, weeks_on_chart intiger)"
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
            # print(list_item[3])
            cursor_obj.execute(
                f"INSERT INTO music VALUES({i}, {list_item[0]}, {list_item[1]}, {list_item[2]}, {list_item[3]}, {list_item[4]}, {list_item[5]}, {list_item[6]}, {list_item[7]}, {list_item[8]} )"
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
