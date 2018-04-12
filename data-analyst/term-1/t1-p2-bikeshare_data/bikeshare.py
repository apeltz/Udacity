import time
import pandas as pd
import numpy as np
from datetime import datetime
import sys
from termcolor import colored, cprint
import os

dirname = os.path.dirname(__file__)

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'new_york_city.csv',
    'washington': 'washington.csv'
}

MONTH_DICT = {
    'jan': 1,
    'feb': 2,
    'mar': 3,
    'apr': 4,
    'may': 5,
    'jun': 6,
    'all': 'all'
}

MONTH_LIST = [ None, 'January', 'February', 'March', 'April', 'May', 'June']

DOW_DICT = {
    'mon': 0,
    'tue': 1,
    'wed': 2,
    'thu': 3,
    'fri': 4,
    'sat': 5,
    'sun': 6,
    'all': 'all'
}

DOW_LIST = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def readable_hour(n):
    suffix = 'pm' if n >= 12 else 'am'
    return str(n%12) + suffix

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    greeting = '{: ^100}'.format('Hello! Let\'s explore some US bikeshare data!')
    cprint('*'*len(greeting), 'white', 'on_cyan')
    cprint(greeting, 'white', 'on_cyan', attrs=['bold'])
    cprint('*'*len(greeting), 'white', 'on_cyan')
    cprint('\n\n')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cprint('Which city would you like to get info for?', 'magenta')
    while True:
        city = input('Please choose Chicago, New York City, or Washington:\n').lower()
        if city in CITY_DATA.keys():
            cprint('\nIt looks like you want information for ' + city.title() + '. We can get that for you!\n', 'yellow')
            break
        else:
            cprint('\nI\'m sorry, I dont have info for that city. Please choose a valid city.\n', 'red')

    # get user input for month (all, january, february, ... , june)
    cprint('Which month would you like to get data for?', 'magenta')
    while True:
        month = input('Please choose: Jan, Feb, Mar, Apr, May, Jun, or All\n').lower()
        if month in MONTH_DICT.keys():
            cprint('\nIt looks like you want information for ' + month.title() + '. We can get that for you!\n', 'yellow')
            month = MONTH_DICT[month]
            break
        else:
            cprint('\nI\'m sorry, I dont have info for that month. Please choose a valid month.\n', 'red')


    # get user input for day of week (all, monday, tuesday, ... sunday)
    cprint('Which day of the week would you like to get data for?', 'magenta')
    while True:
        day = input('Please choose: Mon, Tue, Wed, Thu, Fri, Sat, Sun, or All\n').lower()
        if day in DOW_DICT.keys():
            cprint('\nIt looks like you want information for ' + day.title() + '. We can get that for you!\n', 'yellow')
            day = DOW_DICT[day]
            break
        else:
            cprint('\nI\'m sorry, I dont have info for that day. Please choose a valid day.\n', 'red')

    cprint('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    file_path = os.path.join(dirname, CITY_DATA[city])
    df = pd.read_csv(file_path)

    # Format start and end time strings into usable date objects
    df['Start Time'] = pd.to_datetime(df['Start Time'], format='%Y-%m-%d %H:%M:%S')
    df['End Time'] = pd.to_datetime(df['End Time'], format='%Y-%m-%d %H:%M:%S')

    # Filter by requested criteria, if provided
    if month == 'all' and day == 'all': 
        return df
    elif month == 'all':
        return df[(df['Start Time'].dt.dayofweek == day)]
    elif day == 'all':
        return df[(df['Start Time'].dt.month == month)]
    else:
        return df[ (df['Start Time'].dt.month == month) & (df['Start Time'].dt.dayofweek == day) ]


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    month_counts = df['Start Time'].dt.month.value_counts()
    month_max = month_counts.idxmax()

    # mean_count_month = 
    counts_day_of_week = df['Start Time'].dt.dayofweek.value_counts()
    counts_hour = df['Start Time'].dt.hour.value_counts()

    # display the most common month
    cprint('The most common month that people chose to ride:', 'white')
    cprint(MONTH_LIST[month_counts.idxmax()] + '\n', 'cyan', attrs=['bold'])

    # display the most common day of week
    cprint('The most common day that people chose to ride:', 'white')
    cprint(DOW_LIST[counts_day_of_week.idxmax()] + '\n', 'cyan', attrs=['bold'])

    # display the most common start hour
    cprint('The most common hour that people chose to ride:', 'white')
    cprint(readable_hour(counts_hour.idxmax()) + '\n', 'cyan', attrs=['bold'])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print(df.head())
    print
    print
    top_start_stations = df['Start Station'].value_counts().keys().tolist()[:5]
    top_start_counts = df['Start Station'].value_counts().tolist()[:5]
    top_start = zip(top_start_stations, top_start_counts)

    top_end_stations = df['End Station'].value_counts().keys().tolist()[:5]
    top_end_counts = df['End Station'].value_counts().tolist()[:5]
    top_end = zip(top_start_stations, top_start_counts)

    df['Start End'] = df['Start Station'] + ' --> ' + df['End Station']
    top_start_end_stations = df['Start End'].value_counts().keys().tolist()[:5]
    top_start_end_counts = df['Start End'].value_counts().tolist()[:5]
    top_start_end = zip(top_start_stations, top_start_counts)
    print(df.head())

    # display most commonly used start station
    for station, count in top_start:
        print('The next station is: ', station, count)

    # display most commonly used end station


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_travel_time = df['Trip Duration'].sum()
    mean_travel_time = df['Trip Duration'].mean()
    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    t1 = df['User Type'].value_counts()
    t2 = df['Gender'].value_counts()
    count_user_types = df['User Type'].notnull().value_counts()
    count_gender = df['Gender'].notnull().value_counts()
    count_dob = df['Birth Year'].notnull().value_counts()
    count_dob_common = df['Birth Year'].notnull().value_counts().mode()
    count_dob_youngest = df['Birth Year'].notnull().max()
    count_dob_oldest = df['Birth Year'].notnull().max()

    # Display counts of user types


    # Display counts of gender


    # Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.head(5))
        time_stats(df)
        # station_stats(df)
        # trip_duration_stats(df)
        # user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
