import os

import os_stuff
import read_csv
import build_db
import db_query

data_file = 'MusicData.csv'
db_name = 'billboard.db'
pre_loaded_db = 'pre-loaded.db'

os_stuff.clear_old_file(db_name)

#  TASK 1 - READ FROM CSV INTO MEMORY AND PRINT
data_list = read_csv.read_print_csv(data_file)
os_stuff.clear()
print("This is a large dataset and it will take a while to read and save into the DB.")
print("To skip this step, you can press 'Y' and we'll use a pre-loaded DB,")
print("or press 'N' and we'll let you see the DB load.")
print(' ')
skip2 = input("Do you want to skip the DB step and use a pre-loaded DB? (Y/n)")

# TASK 2 - READ LIST FROM MEMORY INTO DB
if skip2.upper() == 'N':
    build_db.build_db(db_name, data_list)
    build_db.load_data_into_db(db_name, data_list)
else:
    pass

# TASK 3 - QUERY AND MANIPULATE DATA FROM DB
if skip2.upper() == 'N':
    db_query.db_query(db_name)
else:
    db_query.db_query(pre_loaded_db)
