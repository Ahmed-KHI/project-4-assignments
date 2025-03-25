def main():
    voting_ages = {
        "Peturksbouipo": 16,
        "Stanlau": 25,
        "Mayengua": 48
    }

    user_age = int(input("How old are you? "))

    for country, age in voting_ages.items():
        if user_age >= age:
            print(f"You can vote in {country} where the voting age is {age}.")
        else:
            print(f"You cannot vote in {country} where the voting age is {age}.")

if __name__ == "__main__":
    main()