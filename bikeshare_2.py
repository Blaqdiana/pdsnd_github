import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#  Names of cities needed for the analysis
city_names = ["chicago", "new york city", "washington"]
# Names of months needed for the analysis
month_options = ["january", "february", "march", "april", "may", "june", "all"]
# Days of the week
day_options = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = input("Enter the name of your choice of city from this pool (Chicago, New york, Washington): ").lower()
        if city in city_names:
            break
        else:
            print("Invalid city name. Please enter a valid city name\n")

    # get user input for month (all, january, february, ... -, june)
    
    while True:
        month = input("Enter the name of month you want to view the stats ('january', 'february', 'march', 'april', 'may', 'june') or \nEnter all to get the analysis of the entire 6 months: ").lower()
        if month in month_options:
            break
        else:
            print("Invalid month name. Please enter a valid month name \n")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        day = input("Enter the name of any of the days of the week that you want to analyze \n(monday, tuesday, wednesday, thursday, friday, saturday, sunday) or \nEnter all if you'll like the analysis to be for all days of the week: ").lower()
        if day in day_options:
            break
        else:
            print("Invalid day name. Please enter a valid day name\n")
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
    # Load data into the DataFrame
    df = pd.read_csv(CITY_DATA[city])
    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extract month from the Start Time datetime column
    df['Month'] = df['Start Time'].dt.month
    # Extract day of the week from the Start Time datetime column
    df['Week Day'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['Month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Week Day'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['Month'].mode()[0]
    print("The most common month is {}".format(common_month))
    # display the most common day of week
    common_weekday = df['Week Day'].mode()[0]
    print("The most common day of the week is {}".format(common_weekday))
    # display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    start_hour = df['Hour'].mode()[0]
    print("The most common start hour is {}".format(start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    commonly_used_start_Station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: {}".format(commonly_used_start_Station))
    # display most commonly used end station
    commonly_used_end_Station = df['End Station'].mode()[0]
    print("The most commonl used end station is: {}".format(commonly_used_end_Station))
    # display most frequent combination of start station and end station trip
    df['Start & End Station'] = df['Start Station'] + ' - ' + df['End Station']
    commonly_used_s_and_e_station = df['Start & End Station'].mode()[0]
    print("The most frequently used commbination of start station and end station is: {}".format(commonly_used_s_and_e_station))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("This is the total travel time: {}".format(total_travel_time))
    # display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print("This is the average travel time: {}".format(average_travel_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types_count = df['User Type'].value_counts()
    print("Here is the user count stats: \n{}\n".format(user_types_count))
    # Display counts of gender
    if 'Gender' in df.columns:
        gender_count = df['Gender'].value_counts()
        print("These are the counts of gender: \n{}\n".format(gender_count))
    else:
        print("Gender is not available in the DataFrame.")
    

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        # Earliest birth year
        earliest_year = df['Birth Year'].min()
        print("This is the earliest birth year {}".format(earliest_year))
        # 
        recent_birth_year = df['Birth Year'].max()
        print("This is the most recent birth year: {}".format(recent_birth_year))
        common_year = df['Birth Year'].mode()[0]
        print("This is the most recent birth year: {}".format(common_year))
    else:
        print("Birth year data cannot be determined.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        # Prompt user to decide whether to view the raw data
        view_raw_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n')
        # Initialize the starting index for slicing the data
        start_idx = 0

        # While the user wants to view raw data
        while view_raw_data.lower() == 'yes':
            # Slice the DataFrame to get a range of 5 rows and print
            value_range = df.iloc[start_idx:start_idx + 5]
            print(value_range)
            # Ask the user if they want to view more data
            view_raw_data = input('\nWould you like to see 5 more lines of raw data? Enter yes or no.\n')
            # If the user wants to view more data
            while view_raw_data.lower()  == 'yes':
                # Update the starting index by the length of the current data range
                start_idx += len(value_range)
                # Check if the starting index exceeds the length of the DataFrame
                if start_idx >= len(df):
                    # Calculate the remaining data to display
                    blaqdiana = len(df) - len(value_range)
                    # Print the remaining data and notify the user that there is no more data to display
                    print(df.iloc[start_idx:start_idx + blaqdiana])
                    print("No more raw data to display.")
            

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
