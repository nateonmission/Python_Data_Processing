# TASK 2 - LOAD DATA INTO A SQL DATABASE

import os_stuff
import db_tools
import pandas as pd


def load_data_into_db(db_name, data_list):
    os_stuff.clear()
    print("Now, we'll load that data into the a Pandas DataFrame and then send it into a SQLite DB.")
    print(" ")
    pause_me = input("Press ENTER key to continue.")

    def insert_data(db, data_list):
        music_df = pd.DataFrame(data_list)
        music_df.columns = music_df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
        music_df.to_sql('music', con=db, if_exists='replace', index_label='id')

    db = db_tools.sql_connection(db_name)
    insert_data(db, data_list)
    db.close()
    print('')
    print("Whew... So, that's done.")
    pause_me = input('Press ENTER key to continue.')
