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
    city = ''
    month = ''
    day = ''
    city_list = ['chicago', 'new york', 'washington']
    month_list = ['all','january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    day_list = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while True:
        city = input("Please enter city name between Chicago, New York, Washington: ").lower()
        if city not in city_list:
            print("please enter a valid city")
            continue
        # TO DO: get user input for month (all, january, february, ... , june)
        month = input("Please enter the month as ('all','january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'): ").lower()
        if month not in month_list:
            print("please enter a valid month")
            continue
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input("please enter the day as ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'): ").lower()
        if day not in day_list:
            print("please enter a valid day")
            continue
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
    ############### this code got it from the practice problem 3 ################
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        month_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = month_list.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    ############### this code got it from the practice problem 3 ################
    #removing NaN rows The "dealing with NaN" Video in this course helped in this line
    df.dropna(axis=0, inplace = True)
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    print("the most common month: {}".format(df['Start Time'].dt.month.mode()[0]))

    # TO DO: display the most common day of week
    print("the most common day of week: {}".format(df['Start Time'].dt.weekday_name.mode()[0]))

    # TO DO: display the most common start hour
    print("the most common start hour: {}".format(df['Start Time'].dt.hour.mode()[0]))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("most commonly used start station: {}".format(df['Start Station'].mode()[0]))


    # TO DO: display most commonly used end station
    print("most commonly used end station: {}".format(df['End Station'].mode()[0]))


    # TO DO: display most frequent combination of start station and end station trip
    #got this solotion form https://www.reddit.com/r/learnpython/comments/7s99rk/pandas_sort_by_most_frequent_value_combinations/
    most = str(df.groupby(['Start Station', 'End Station']).size().sort_values(ascending=False).head(1))
    print("most frequent combination of start station and end station trip:\n {}".format(most[:-12]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("total travel time: {}".format(df['Trip Duration'].sum()))


    # TO DO: display mean travel time
    print("mean travel time: {}".format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("counts user types: \n {}".format(df['User Type'].value_counts()))


    # TO DO: Display counts of gender
    #how to check an column if exist or not https://stackoverflow.com/questions/24870306/how-to-check-if-a-column-exists-in-pandas
    if 'Gender' in df:
        print("counts of gender: \n {}".format(df['Gender'].value_counts()))
    else:
        print("gender info doesn't exist")

    # TO DO: Display earliest, most recent, and most common year of birth
    #how to check an column if exist or not https://stackoverflow.com/questions/24870306/how-to-check-if-a-column-exists-in-pandas
    if 'Birth Year' in df:
        print("earliest year of birth: {}".format(df['Birth Year'].min()))
        print("most recent year of birth: {}".format(df['Birth Year'].max()))
        print("most common year of birth: {}".format(df['Birth Year'].mode()))
    else:
        print("birth year info doesn't exist")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    i = 0
    while True:
        #try:
            user_input = input("Do you want to see the raw data? write 'yes' to see, or write 'no' to stop: ").lower()
            if user_input == 'yes':
                #how to check if the data frame is empty https://stackoverflow.com/questions/19828822/how-to-check-whether-a-pandas-dataframe-is-empty
                if df.empty:
                    print("\nData Frame is empty")
                    break
                print(df.iloc[i:i+5])
                i += 5
            elif user_input == 'no':
                break
            else:
                print("please answer with 'yes' or 'no'")
                continue
       

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        try:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
        except IndexError:
            print("there is no info for the month you had select")
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
