import os

import read_csv
import build_db

data_file = 'MusicData.csv'
db_name = 'billboard.db'

print(os.getcwd())
print(data_file)

#  TASK 1 - READ FROM CSV INTO MEMORY AND PRINT
data_list = read_csv.read_print_csv(data_file)

# TASK 2 - READ LIST FROM MEMORY INTO DB
pause = input("Press any key to build DB")
build_db.build_db(db_name, data_list)

# TASK - QUERY AND MANIPULATE DATA FROM DB
