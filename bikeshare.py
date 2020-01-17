# create a bikeshare project by using US Bikeshare data and python
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
    months = ['all', 'january', 'febuary', 'march', 'april', 'may', 'june']
    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    print('Hello! Let\'s explore some US bikeshare data!')


    # TO DO: get user input for city (chicago, new york city, washington). Add a break into the code by using while loop to handle invalid inputs

    while True:
        city = input(' Would you like to see data from Chicago, New York City or Washington? \n').lower()

        if city in CITY_DATA:
            print('You have chossen following city:', city)
            break
        else:
            print('Please enter a valid city')






    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input('Would you like to filter the data by month? Please enter: all,January, Febuary, March, April, May or June: \n ').lower()

        if month not in months:
            print("Please enter again.")

        else:
            break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input('Which day do you want to see? Please enter all, Monday, ...Sunday: \n').lower()

        if day not in days:
            print("Please enter again.")

        else:
            break




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
    df=pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'febuary', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month']==month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    df['hour'] = df['Start Time'].dt.hour


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month is: ', common_month)



    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day is: ', common_day)




    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most common hour is: ', common_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most common Start Station is: ', common_start_station)


    # TO DO: display most commonly used end station
    common_end_station =df['End Station'].mode()[0]
    print('Most common End Station is: ', common_end_station)


    # TO DO: display most frequent combination of start station and end station trip
    df['end_and_start_station'] = df['End Station']+ ' to ' +df['Start Station']
    common_end_and_start_station = df['end_and_start_station'].mode()[0]
    print('Most common Start and End Station is: ', common_end_and_start_station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time is: ', total_travel_time)


    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('Number of user type: \n', user_type)


    # TO DO: Display counts of gender
    """GENDER INFORMATION IS ONLY AVAILABLE FOR NEW YORK CITY AND CHICAGO"""
    if 'Gender'in df:
        print('\n Number of genders are as follow: \n',df['Gender'].value_counts())

    else:
        print('Sorry information about the gender  is not available for this city.')




    # TO DO: Display earliest, most recent, and most common year of birth
    """Birth INFORMATION IS ONLY AVAILABLE FOR NEW YORK CITY AND CHICAGO"""
    if 'Birth Year' in df:
        print('\n This is the earliest birth year: \n',df['Birth Year'].min())
        print('\n This is the most recent birth year: \n', df['Birth Year'].max())
        print('\n This is the most common birth year:\n', df['Birth Year'].mode()[0])


    else:
        print('sorry, information about the birth year is not available for this city')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

   #displaying answer if user want to view first five rows of data or not
    while True:
        answer = input('\nWould you like to view the first 5 rows of the data? Enter yes or no\n').lower()

        if answer == 'yes':
            print('First five raw data\n', df.head())
            break
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
