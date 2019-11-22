# TASK 3 - QUERY THE SQLite DB AND GENERATE INFORMATION FROM THE DATA
import os_stuff
import db_tools

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')


def intro(db_name):
    os_stuff.clear()
    print("TASK 3 - QUERYING THE DB")
    print('------------------------')
    print(' ')
    print(f"In this step, you'll walk through pulling information from the DB file ({db_name})"
          f" in a structured manner.")
    print(' ')
    pause_me = input('Press ENTER key to begin.')


def query_menu(db_name):
    repeat = 1
    while repeat == 1:
        os_stuff.clear()
        print('******************** PICK A QUERY ********************')
        print('BASIC SQL QUERIES')
        print('01 - Songs in Top 10 for a given year')
        print('02 - Songs in Top 10 for a given year and month')
        print('03 - Songs in Top 10 for a given Artist')
        print('')
        print('MatPlotLib QUERIES')
        print('11 - Plots Song Popularity over time')
        print('12 - Plots Artist Popularity over time')
        print('')
        print('PANDAS-BASED QUERIES')
        print('21 - Stats by Artist (Work In Progress)')
        print('')
        print('99 - EXIT')
        print('')
        selection = input("Query number: ")
        if selection.isdigit():
            if int(selection) == 1:
                top_10_by_year(db_name)
                repeat = 1
            elif int(selection) == 2:
                top_10_by_yr_and_mo(db_name)
                repeat = 1
            elif int(selection) == 3:
                query_by_artist(db_name)
                repeat = 1
            elif int(selection) == 11:
                plot_song_pop_over_time(db_name)
                repeat = 1
            elif int(selection) == 12:
                plot_artist_pop_over_time(db_name)
                repeat = 1
            elif int(selection) == 21:
                stats_by_artist(db_name)
                repeat = 1
            elif int(selection) == 99:
                break
            else:
                pass
        else:
            pass
    print('GOOD BYE')


# BASIC QUERIES
def top_10_by_year(db_name):
    os_stuff.clear()
    db = db_tools.sql_connection(db_name)
    print('opening data...')
    cur = db.cursor()
    cur.execute('SELECT min(WeekID) FROM music')
    min_year = int(cur.fetchone()[0][-4::])
    cur.execute('SELECT max(WeekID) FROM music')
    max_year = int(cur.fetchone()[0][-4::])
    os_stuff.clear()
    print("DB contains data from " + str(min_year) + " to " + str(max_year) + ".")
    repeat = 1
    while repeat == 1:
        selected_year = input("Enter a year to explore: ")
        if int(selected_year) < min_year or int(selected_year) > max_year:
            print("Invalid year!")
            pause_me = input("Press ENTER key to continue")
        else:
            repeat = 0
    db_response = date_query(cur, selected_year)
    print_db_results(db_response)
    db.close()


def top_10_by_yr_and_mo(db_name):
    os_stuff.clear()
    db = db_tools.sql_connection(db_name)
    print('opening data...')
    cur = db.cursor()
    cur.execute('SELECT min(WeekID) FROM music')
    min_year = int(cur.fetchone()[0][-4::])
    cur.execute('SELECT max(WeekID) FROM music')
    max_year = int(cur.fetchone()[0][-4::])
    os_stuff.clear()
    print("DB contains data from " + str(min_year) + " to " + str(max_year) + ".")
    repeat = 1
    while repeat == 1:
        selected_year = input("Enter a year: ")
        if not selected_year.isdigit():
            print("Invalid year!")
            pause_me = input("Press any key to continue")
        elif int(selected_year) < min_year or int(selected_year) > max_year:
            print("Invalid year!")
            pause_me = input("Press any key to continue")
        else:
            repeat = 0
    repeat = 1
    while repeat == 1:
        selected_month = input("Enter a month as a number: ")
        if not selected_month.isdigit():
            print("Invalid month!")
            pause_me = input("Press any key to continue")
        elif int(selected_month) < 1 or int(selected_month) > 12:
            print("Invalid month!")
            pause_me = input("Press any key to continue")
        else:
            repeat = 0
    date_string = selected_month + '/' + selected_year
    db_response = date_query(cur, date_string)
    print_db_results(db_response)
    db.close()


def query_by_artist(db_name):
    os_stuff.clear()
    db = db_tools.sql_connection(db_name)
    print('opening data...')
    cur = db.cursor()
    selected_artist = input("Enter a SOLO ARTIST or a BAND: ")
    ex_str = f'SELECT * FROM music WHERE Performer LIKE "%{selected_artist}%" AND "Week Position" <= 10 GROUP BY SongID ORDER BY WeekID ASC'
    cur.execute(ex_str)
    db_response = cur.fetchall()
    print_db_results(db_response)
    db.close()


# MatPlotLib BASED QUERIES
def plot_song_pop_over_time(db_name):
    os_stuff.clear()
    db = db_tools.sql_connection(db_name)
    print('opening data...')
    cur = db.cursor()
    artist_repeat = 1
    while artist_repeat == 1:
        selected_artist = input("Enter a SOLO ARTIST or a BAND: ")
        ex_str = f'SELECT * FROM music WHERE artist LIKE "%{selected_artist}%"  GROUP BY song_id ORDER BY WeekID ASC'
        cur.execute(ex_str)
        os_stuff.clear()
        db_response = cur.fetchall()
        if len(db_response) != 0:
            artist_repeat = 0
        else:
            print('No results found')
            pause_me = input('Press ENTER to Continue')
            pass
    songs = []
    menu_counter = 1
    os_stuff.clear()
    for line in db_response:
        print(f'{menu_counter}. {line[4]} by {line[5]} ({line[2][:4]})')
        songs.append(line[4])
        menu_counter += 1
    repeat = 1
    while repeat == 1:
        song_selection = input("Select a song by the number: ")
        if song_selection.isdigit():
            if 0 < int(song_selection) < len(songs)+1:
                repeat = 0
            else:
                pass
        else:
            pass
    song_index = int(song_selection) - 1
    print(f"You chose {songs[song_index]}")
    ex_str = f'SELECT * FROM music WHERE artist LIKE "%{selected_artist}%" AND song_title LIKE "{songs[song_index]}" ORDER BY WeekID ASC'
    cur.execute(ex_str)
    os_stuff.clear()
    db_response = cur.fetchall()
    dates = []
    chart_positions = []
    for line in db_response:
        line_date = line[2][:10]
        dates.append(datetime.strptime(line_date, '%Y-%m-%d'))
        chart_positions.append(line[3])
    plt.plot_date(dates, chart_positions, '-')
    plt.gca().invert_yaxis()
    plt.show()


def plot_artist_pop_over_time(db_name):
    os_stuff.clear()
    db = db_tools.sql_connection(db_name)
    print('opening data...')
    cur = db.cursor()
    artist_repeat = 1
    while artist_repeat == 1:
        selected_artist = input("Enter a SOLO ARTIST or a BAND: ")
        ex_str = f'SELECT * FROM music WHERE artist LIKE "%{selected_artist}%" ORDER BY WeekID ASC'
        cur.execute(ex_str)
        os_stuff.clear()
        db_response = cur.fetchall()
        if len(db_response) != 0:
            artist_repeat = 0
        else:
            print('No results found')
            pause_me = input('Press ENTER to Continue')
            pass
    dates = []
    chart_positions = []
    for line in db_response:
        line_date = line[2][:10]
        dates.append(datetime.strptime(line_date, '%Y-%m-%d').date())
        chart_positions.append(line[3])
    plt.plot_date(dates, chart_positions, '-')
    plt.gca().invert_yaxis()

    plt.show()


# PANDAS QUERIES
def stats_by_artist(db_name):
    os_stuff.clear()
    db = db_tools.sql_connection(db_name)
    print('opening data...')
    artist_repeat = 1
    while artist_repeat == 1:
        selected_artist = input("Enter a SOLO ARTIST or a BAND: ")
        db_response = pd.read_sql_query(f'SELECT * FROM music WHERE artist LIKE "%{selected_artist}%" ORDER BY WeekID ASC', db)
        os_stuff.clear()
        if len(db_response) != 0:
            artist_repeat = 0
        else:
            print('No results found')
            pause_me = input('Press ENTER to Continue')
            pass
    artist_data = pd.DataFrame(db_response)
    artist_data = artist_data.set_index('id')

    print(artist_data.groupby(['song_title']).mean())
    pause_me = input('Press ENTER to continue.')


# HELPER FUNCTIONS
def date_query(cur, date_string):
    ex_str = f'SELECT * FROM music WHERE WeekID LIKE "%{date_string}%" AND "Week Position" <= 10 GROUP BY SongID'
    cur.execute(ex_str)
    db_response = cur.fetchall()
    return db_response


def print_db_results(db_response):
    for item in db_response:
        print(item[4] + " by " + item[5])
    print('')
    print(str(len(db_response)) + " total songs found.")
    pause_me = input('Press ENTER key to continue')


# PRIMARY FUNCTION
def db_query(db_name):
    intro(db_name)
    query_menu(db_name)
