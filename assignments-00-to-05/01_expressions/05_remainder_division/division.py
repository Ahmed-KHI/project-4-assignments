def divide_numbers(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return  quotient , remainder

def main():
    num1 = int(input("Enter the number to be divided: "))
    num2 = int(input("Enter the divisor: "))

    quotient, remainder = divide_numbers(num1, num2)

    print(f"The result of this division is {quotient} with a remainder of {remainder}.")

if __name__ == "__main__":
    main()