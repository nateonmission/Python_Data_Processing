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
    my_data_list = pd.read_csv(data_file)
    print(' ')
    print('The data has been read from CSV & loaded into the list')
    print(f'There are {len(my_data_list)} records.')
    pause_me = input('Press ENTER to verify this? ')
    os_stuff.clear()
    print(my_data_list.head())
    pause_me = input('Press ENTER key to continue to the next step.')
    return my_data_list
