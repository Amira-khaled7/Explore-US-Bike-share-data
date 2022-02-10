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
    citys=['chicago','new york city', 'washington']
    city=input("Enter your city as: chicago, new york city, washington ").lower()
    while city not in citys:
        print("Is not valid city")
        city=input("Enter your city as: chicago, new york city, washington ").lower()
        
    # TO DO: get user input for month (all, january, february, ... , june)
    months=["january","february","march","april","may","june","all"]
    month=input("Enter the months from january to june or enter all if you dont need filter a data ").lower()
    while month not in months:
        print("invalid month, please enter months from january to june or enter all ")
        month=input("Enter the months from january to june or enter all if you dont need filter a data ").lower()
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['saturday','sunday','monday','tuesday','wednesday','thursday','friday','all']
    day=input("Enter a day or enter all if you dont need filter a data ").lower()
    while day not in days:
        print("invalid day , valid day or enter all")
        day=input("Enter a day or enter all if you dont need filter a data ").lower()
       
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
    # convert start time column to datetime
    df['Start Time']=pd.to_datetime(df['Start Time'])
    # extract month and days of week to creat anew column
    df['month']=df['Start Time'].dt.month_name()
    df['day_of_week']=df['Start Time'].dt.day_name()
    # Filter by mounth 
    
    if month != 'all':
        df = df[df['month'] == month.title()]
    # Filter by day 
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # To Do: display the most common month
    most_common_month=df['month'].mode()[0]
    print('most common month: ',most_common_month)
  
    # TO DO: display the most common day of week
    
    most_common_day=df['day_of_week'].mode()[0]
    print('most common day: ',most_common_day)
    
    # TO DO: display the most common start hour
    #creat an hour column 
    df['hour']=df['Start Time'].dt.hour
    #find the most common start hour 
    most_common_hour=df['hour'].mode()[0]
    print('the most common start hour:', most_common_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    pop_start_station=df['Start Station'].mode()[0]
    print('The most commonly used start station : ',pop_start_station)

    # TO DO: display most commonly used end station
    pop_end_station=df['End Station'].mode()[0]
    print('The most commonly used end station : ',pop_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    #creat Trip column
    df['Trip']=df['Start Station'] + ' : ' + df['End Station']
    most_common_trip=df['Trip'].mode()[0]
    print('The most common trip : ', most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time=df['Trip Duration'].sum()
    print("The total travel time is : ",total_time)
    # TO DO: display mean travel time
    average_travel_time=df['Trip Duration'].mean()
    print("The average travel time is : ",average_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    userscount=df['User Type'].value_counts()
    print("The counts of user types are : ",userscount)


    # TO DO: Display counts of gender
    try:
        gender=df['Gender'].value_counts()
        print("The counts of gender are : ",gender)
    except:
        print("This data is not found")
    
    

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birth_year=df['Birth Year'].min()
        print('the earliest year of birth : ' ,earliest_birth_year)
        recent_birth_year=df['Birth Year'].max()
        print('the recent year of birth : ' ,recent_birth_year)
        common_birth_year=df['Birth Year'].mode()[0]
        print('the most common year of birth : ' ,common_birth_year)
    except:
        print("This data is not found")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    ''' this function display five raw data 
        and ask the user if you want display more
    '''
    ask=input("Are you want to display five raw of data enter yes or No ").lower()
    while True:
        if ask=='yes':
            print("The five raw data is : ", df.sample(5))
            ask=input("Are you want to display five raw of data again enter yes or No ").lower()
            
        else:
            print("Thank you")
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
