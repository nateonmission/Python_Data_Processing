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
            print(list_item)
            # cursor_obj.execute(
            #     f"INSERT INTO music VALUES({i}, {list_item[0]}, {list[1]}, {list[2]}, {list[3]}, {list[4]}, {list[5]}, {list[6]}, {list[7]}, {list[8]}, {list[9]} )"
            # )
            # i += 1
            # db.commit()

    db = sql_connection(db_name)
    insert_data(db, data_list)
