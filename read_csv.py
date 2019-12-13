#  TASK 1 READ CSV AND PRINT IT

import os_stuff
import pandas as pd


def read_print_csv(data_file):
    os_stuff.clear()
    print('TASK 1 - READ A CSV FILE INTO MEMORY')
    print('-------------------------------------')
    print(' ')
    print(f'The file {data_file} will be read from the current directory and each line added to a list, '
          f'which will, then, be returned')
    print(' ')
    pause_me = input('Press ENTER key to begin.')
    print(' ')
    print('Converting date formats in the CSV to YEAR-MONTH-DAY. This will take a moment.')
    print('Reading CSV')
    my_data_list = pd.read_csv(data_file)
    print('Converting Data to DateFrame')
    music_df = pd.DataFrame(my_data_list)
    print('Converting Date format')
    music_df['WeekID'] = pd.to_datetime(music_df['WeekID'])
    music_df['WeekID'] = music_df['WeekID'].dt.strftime('%Y-%m-%d')
    print(' ')
    print('The data has been read from CSV & loaded into the list')
    print(f'There are {len(my_data_list)} records.')
    pause_me = input('Press ENTER to verify this? ')
    os_stuff.clear()
    print(music_df.head())
    pause_me = input('Press ENTER key to continue to the next step.')
    return music_df
