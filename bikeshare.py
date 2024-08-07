import time
import pandas as pd
import numpy as np
import calendar

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
    city = input("Enter your city: ")
    city= city.lower()
    if(not CITY_DATA[city]) :
       raise ValueError('Invalid city')

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter your month: ")
    month= month.lower()
    if(month != 'all') :
      month=month.capitalize()
      if(not month.capitalize() in calendar.month_name[1:]) :  
          raise ValueError('Invalid month')
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter your day of week: ")
    day= day.lower()
    if(day != 'all') :
      day= day.capitalize()
      print(calendar.day_name)
      if(not day.capitalize() in calendar.day_name) :  
          raise ValueError('Invalid day of week')

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
    fileName= CITY_DATA[city]
    data= pd.read_csv(fileName, parse_dates=['Start Time','End Time'])
    day_of_week_map = {i: day for i, day in enumerate(calendar.day_name)}
    month_map = {i: day for i, day in enumerate(calendar.month_name)}
    data['day'] = data['Start Time'].dt.dayofweek.map(day_of_week_map)
    data['month'] = data['Start Time'].dt.month.map(month_map)

    if month != 'all': data= data[(data['month']==month)]
    
    print(data.head(), day)
    if day != 'all': data= data[(data['day']==day)]

    print(data.head())
    return data


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    if(df.empty):
        print('Data is null')
        return;
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time    = time.time()

    # DO: display the most common month
    commonMonth= df['month'].mode()[0]
    print ('The most month is ',commonMonth)
    # TO DO: display the most common day of week
    commonDay= df['day'].mode()[0]
    print ('The most day of week is ',commonDay)    

    # TO DO: display the most common start hour
    commonTime= df['Start Time'].dt.time.mode()[0]
    print ('The most start hour is ',commonTime)    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonStartStation= df['Start Station'].mode()[0]
    print ('The most start station is ',commonStartStation)
    # TO DO: display most commonly used end station
    commonEndStation= df['Start Station'].mode()[0]
    print ('The most end station is ',commonEndStation)

    # TO DO: display most frequent combination of start station and end station trip
    df['StartEndStation']= df['Start Station'] + ' ' + df['End Station']
    commonEndStation= df['StartEndStation'].mode()[0]
    print ('The most end station is ',commonEndStation)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['duration']= df['End Time'] - df['Start Time']
    total= df['duration'].sum()
    print('Total Travel Time: ',total)

    # TO DO: display mean travel time
    mean= df['duration'].mean()
    print('Total Mean Time: ',mean)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    countUserTypes=df['User Type'].value_counts()
    print('Total User Types: ',countUserTypes)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        countGender=df['Gender'].value_counts()
        print('Total Gender: ', countGender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('Earliest Year: ',df['Birth Year'].min())
        print('Most Recent Year: ',df['Birth Year'].max())
        print('Most Common Year: ',df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        print(df.shape)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
