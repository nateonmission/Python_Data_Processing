# Main Script Body

import os_stuff
import read_csv
import build_db
import db_query

data_file = './MusicData.csv'
db_name = './billboard.db'

os_stuff.clear_old_file(db_name)

#  TASK 1 - READ FROM CSV INTO MEMORY AND PRINT
data_list = read_csv.read_print_csv(data_file)

# TASK 2 - READ LIST FROM MEMORY INTO DB
build_db.load_data_into_db(db_name, data_list)

# TASK 3 - QUERY AND MANIPULATE DATA FROM DB
db_query.db_query(db_name)
