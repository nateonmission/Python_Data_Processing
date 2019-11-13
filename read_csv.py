#  TASK 1 READ CSV AND PRINT IT
import csv
import os_stuff


def read_print_csv(data_file):
    os_stuff.clear()
    print('TASK 1 - READ A CSV FILE INTO MEMORY')
    print('-------------------------------------')
    print(' ')
    print(f'The file {data_file} will be read from the current directory and each line added to a list, '
          f'which will, then, be returned')
    print(' ')
    pause_me = input('Press any key to begin.')
    with open(data_file, 'r') as my_data:
        my_data_list = list(csv.reader(my_data))

    my_data_list.pop(0)  # Toss headings
    my_data_list.pop(0)  # Toss blank line

    print('The data has been read from CSV & loaded into the list')
    print(f'There are {len(my_data_list)} records.')
    preview_range = input('How many records would you like to see to verify this? ')
    if not preview_range.isdigit():
        for item in range(5):
            print(my_data_list[item])
        print(f"Yeah, I did not understand what '{preview_range}' meant. So, here's 5.")
    elif int(preview_range) > len(my_data_list)-1:
        for item in range(5):
            print(my_data_list[item])
        print('Yeah, I did not understand that. So, here is 5.')
    else:
        for item in range(int(preview_range)):
            print(my_data_list[item])
    print(' ')
    pause_me = input('Press any key to continue to the next step.')
    return my_data_list
