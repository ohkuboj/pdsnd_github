import time
import pandas as pd
import numpy as np

#below includes bikeshare customer data from Chicago, New York City, and Washington. These are cities in the USA.

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city_names = ['chicago', 'new york city', 'washington']
month_names = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
day_names = ['all', 'sunday', 'monday', 'tuesday',
             'wednesday', 'thursday', 'friday', 'saturday']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
    (str) city - name of the city to analyze
    (str) month - name of the month to filter by, or "all" to apply no month filter
    (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). In current set-up, user cannot select 'all' cities. HINT: Use a while loop to handle invalid inputs
    try:
        city = input('Please enter a city: chicago, new york city or washington.').lower()       
        while (city not in city_names):
            print("You entered an invalid ", city, " please try again")
            sys.exit(1)
        print("You selected ", city, " nice choice!")
    except:
        print("error - you entered an invalid city - script will now end")
        quit()
    # TO DO: get user input for month (all, january, february, ... , june)
    try:
        month = input('Please enter a month: all, january, february, ... , june.').lower()
        while (month not in month_names):
            print("You entered an invalid ", month, " please try again")
            sys.exit(1)
        print("You selected ", month, " that's tight!")
    except:
        print("error - you entered an invalid month - script will now end")
        quit()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    try:
        day = input('Please enter a day: all, monday, tuesday, ... sunday.').lower()
        while (day not in day_names):
            print("You entered an invalid ", day, " please try again")
            sys.exit(1)
        print("You selected ", day, ". That's totally rad dude!")
    except:
        print("error - you entered an invalid day - script will now end")
        quit()

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
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    #convert Start Time data to Date time

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('The most popular month traveled: {}.\n'.format(common_month))

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    common_day_of_week = df['day_of_week'].mode()[0]
    print('The most popular day of the week traveled: {}.\n'.format(common_day_of_week))

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most popular hour traveled: {}.\n'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    pop_strt_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is {}.'.format(pop_strt_station))

    # TO DO: display most commonly used end station
    pop_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is {}.'.format(pop_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    pop_strt_end_stations = df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).nlargest(1)
    print('The most common start and end stations are {}.\n'.format(pop_strt_end_stations))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = (df['Trip Duration'].sum())/60
    print('Total travel time is {}.'.format(total_travel_time))

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print('Average travel time is {}.'.format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    Total_User_Type = df['User Type'].nunique()
    print('The total # of users types are :', Total_User_Type)

    # TO DO: Display counts of gender (Washington does not have gender data)
    try:
        Total_Genders = df['Gender'].nunique()
        print('The total # of gender types are :', Total_Genders)
    except:
        print('There are is not gender data for Washington.') 

    # TO DO: Display earliest, most recent, and most common year of birth (Washington has no age data).
    try:
        Earliest_birthday = df['Birth Year'].min()
        print('The earliest birthday is ', Earliest_birthday)
        
        Latest_birthday = df['Birth Year'].max()
        print('The latest birthday is ', Latest_birthday)
        
        Most_common_birthday = df['Birth Year'].mode()[0]
        print('The most common birthday is ', Most_common_birthday)
    except:
        print('There are is not birth data for Washington.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
   


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
