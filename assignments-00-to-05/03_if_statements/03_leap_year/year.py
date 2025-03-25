def main():
    year = int(input("Please input a year: "))

    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    if is_leap:
        print("That's a leap year!")
    else:
        print("That's not a leap year.")

if __name__ == '__main__':
    main()