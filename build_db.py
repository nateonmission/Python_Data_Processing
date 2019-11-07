# TASK 2 - LOAD DATA INTO A SQL DATABASE
import sqlite3
from sqlite3 import Error


def build_db(db_name, data_list):
    def sql_connection():
        try:
            db = sqlite3.connect(db_name)
            print("Connection to database has been established")
            return db
        except Error:
            print(Error)

    def sql_table(db):
        cursor_obj = db.cursor()
        cursor_obj.execute(
            "CREATE TABLE employees(id integer PRIMARY KEY, url text, week_id date, chart_position intiger, song_title text, artist text, song_id text, prev_week intiger, peak_position intiger, weeks_on_chart intiger)"
        )
        db.commit()


    db = sql_connection()
    sql_table(db)