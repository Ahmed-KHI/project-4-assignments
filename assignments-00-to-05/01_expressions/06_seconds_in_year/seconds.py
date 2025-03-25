DAYS_IN_YEAR = 365
HOURS_IN_DAY = 24
MINUTES_IN_HOUR = 60
SECONDS_IN_MINUTES = 60

def calculate_second_in_year():
    return DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTES

def main():
    total_seconds = calculate_second_in_year()
    print(f"There are {total_seconds} seconds in the year! ")

if __name__ == "__main__":
    main()