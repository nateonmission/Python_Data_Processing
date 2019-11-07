#  TASK 1 READ CSV AND PRINT IT
import csv


def read_print_csv(data_file):
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
    return my_data_list
