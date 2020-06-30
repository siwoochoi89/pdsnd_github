import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    list_city = ['chicago', 'new york city', 'washington']
    while True:
        city_input = str(input("Choos a city to analyze (chicago, new york, washington)? "))
        city = city_input.lower()
        if city not in list_city:
            print(That\'s not a valid answer!')
            else:
                break 
    
    # TO DO: get user input for month (all, january, february, ... , june)
    list_month = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month_input = str(input("\nWhat month(january, february, march, april, may, june or all) do you want to analyze? "))
        month = month_input.lower()
        if month.lower() not in list_month:
            print('That\'s not a valid answer!')
            else:
                break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    list_dayofweek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day_input = str(input("\nwhat day of the week(monday, tuesday, wednesday, thursday, friday, saturday, sunday or all) do you want to analyze? "))
        day = day_input.lower()
        if day not in list_dayofweek:
            print('That\'s not a valid answer!')
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

    df = pd.read_csv(CITY_DATA[city])


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].apply(lambda x x.month)
    df['day_of_week'] = df['Start Time'].dt.apply(lambda x x.strftime('%A').lower())


    # filter by month if applicable
    if month != 'all':

        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month],:]


    # filter by day of week if applicable
    if day != 'all':

        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day,:]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df["month"].mode()[0]
    print("The most popular month:", common_month)

    # TO DO: display the most common day of week
    common_day = df["day_of_week"].mode()[0]
    print("The most popular day:", common_day)

    # TO DO: display the most common start hour
    df['hour'] = df["Start Time"].dt.hour
    common_hour = df['hour'].mode()[0]
    print("The most popular hour:", common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_startstation = df["Start Station"].value_counts().idxmax()
    print("The most commonly Start Station:", common_startstation)

    
    # TO DO: display most commonly used end station
    common_endstation = df["End Station"].value_counts().idxmax()
    print("The most commonly End Station:", common_endstation)


    # TO DO: display most frequent combination of start station and end station trip
    df['Combined Station'] = df['Start Station'] + ' and ' + df['End Station']
    common_combinedstation = df['Combined Station'].count()
    print('\nThe most frequent combination Start and End Station together:', common_combinedstation)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is : %d hours' % Total)


    # TO DO: display mean travel time
    mean_travel_time = df["Trip Duration"].mean()
    print('Mean travel duration: %d hours' % int(Mean))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df["User Type"].value_counts()
    
    # TO DO: Display counts of gender
    gender_types = df["Gender"].value_counts()
    print("Count of gender:", gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    earliest_birth = df['Birth Year'].min()
    print('\nThe earliest birth: year', int(earliest_birth))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        counter1 = 0
        counter2 = 3

        while True:
            ch = input("Do you want to see raw data yes or no?\n")
            ch = ch.lower()
            if ch == "yes":
                print(df.iloc[counter1:cointer2])
                counter1 = counter1+3
                counter2 = counter2+3
                else:
                    break

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
