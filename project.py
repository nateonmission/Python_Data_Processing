import os

import read_csv

data_file = 'MusicData.csv'
db_name = 'billboard.db'

print(os.getcwd())
print(data_file)

read_csv.read_print_csv(data_file)


# OTHER STUFF
# with open('MusicData.csv') as my_data:
#     df = pd.read_csv(my_data, index_col=5)
# start_date = '1990-01-01'
# end_date = '2000-01-01'
# mask = ((df['WeekID'] > start_date) & (df['WeekID'] <= end_date) ) & (df['Week Position'] < 11)
# ninties = df.loc[mask]