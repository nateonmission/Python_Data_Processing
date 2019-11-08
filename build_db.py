# TASK 2 - LOAD DATA INTO A SQL DATABASE
import sqlite3
from sqlite3 import Error


def build_db(db_name):
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
        cursor_obj.execute(
            "INSERT INTO music(id integer PRIMARY KEY, url text, week_id date, chart_position intiger, song_title text, artist text, song_id text, prev_week intiger, peak_position intiger, weeks_on_chart intiger)"
        )
        db.commit()