import os
import csv
import sqlite3
from sqlite3 import Error
import pandas as pd
import datetime
from itertools import groupby

data_file = 'MusicData.csv'
db_name = 'billboard.db'

print(os.getcwd())
print(data_file)

# TASK 1 - READ A DATA FILE INTO MEMORY
with open(data_file, 'r') as my_data:
    my_data_list = list(csv.reader(my_data))

my_data_list.pop(0)  # Toss headings
my_data_list.pop(0)  # Toss blank line

print('Data has been read from CSV & loaded into a list')
print(f'There are {len(my_data_list)} records.')
preview_range = input('How many records would you like to see to verify this? ')

if int(preview_range) > len(my_data_list)-1:
    for item in range(5):
        print(my_data_list[item])
    print('That was too many. So, here is 5.')
else:
    for item in range(int(preview_range)):
        print(my_data_list[item])


# TASK 2 - LOAD DATA INTO A SQL DATABASE

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
        "CREATE TABLE employees(
            id integer PRIMARY KEY,
            url text,
            week_id date,
            chart_position intiger,
            song_title text,
            artist text,
            song_id text,
            prev_week intiger,
            peak_position intiger,
            weeks_on_chart intiger
        )"
    )
    db.commit()


db = sql_connection()
sql_table(db)

# TASK 3 - MANIPULATE THE DATA IN THE DATABASE AND SHOW RESULTS






# OTHER STUFF
# with open('MusicData.csv') as my_data:
#     df = pd.read_csv(my_data, index_col=5)
# start_date = '1990-01-01'
# end_date = '2000-01-01'
# mask = ((df['WeekID'] > start_date) & (df['WeekID'] <= end_date) ) & (df['Week Position'] < 11)
# ninties = df.loc[mask]