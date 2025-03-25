def main():
    degree_fahrenheit = float(input("Enter Temperature In Fahrenheit: "))
    degree_celsius = (degree_fahrenheit - 32) * 5.0 / 9.0

    print(f"Temperature: {degree_fahrenheit}F = {round(degree_celsius, 2)}C ")


if __name__ == "__main__":
    main()