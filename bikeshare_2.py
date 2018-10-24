import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input("Would you like to see data for Chicago, New York City, or Washington? ").lower()
            break
        except KeyError:
            print("That\'s not a valid city!")
        # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input("What month would you like to view data for? ").lower()
            break
        except:
            print("That\'s not a valid month!")

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input("Which day would you like to view data for? ").lower()
            break
        except:
            print("That\'s not a valid day!")

    print('-'*40)
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
    #load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # TO DO: display the most common month
    most_com_month = df['Start Time'].dt.month.mode()[0]
    print('Most common month: ', most_com_month)

    # TO DO: display the most common day of week
    most_com_day = df['Start Time'].dt.weekday.mode()[0]
    print('Most common day of the week: ', most_com_day)

    # TO DO: display the most common start hour
    most_com_start_hour = df['Start Time'].dt.hour.mode()[0]
    print('Most common hour: ', most_com_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mc_start_station = df['Start Station'].value_counts().nlargest(1)
    print('The most commonly used startion station is: ', mc_start_station)

    # TO DO: display most commonly used end station
    mc_end_station = df['End Station'].value_counts().nlargest(1)
    print('The most commonly used end station is: ', mc_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    mc_startend_stations = df.groupby(['Start Station', 'End Station']).size().nlargest(1)

    print('most commonly used start and end station combo: ', mc_startend_stations)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    df['Total Time'] = df['End Time'] - df['Start Time']
    total = df['Total Time'].sum()
    print('Total travel time: ', total)



    # TO DO: display mean travel time
    mean = df['Total Time'].mean()
    print('Mean travel time: ', mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        genders = df['Gender'].value_counts()
        print(genders)

    # TO DO: Display earliest, most recent, and most common year of birth


    if 'Birth Year' in df:
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_year_birth = df['Birth Year'].value_counts().nlargest(1)
        print('Most recent year of birth', recent_birth)
        print('Most common year of birth', common_year_birth)
        print('Earliest year of birth: ', earliest_birth)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    start = 0
    end = 5
    while True:
        more_data = input("\nDo you want to see raw data?\n")
        if more_data.lower() != 'yes':
            break
        else:
            print(df.iloc[start:end])
            start += 5
            end += 5




def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
