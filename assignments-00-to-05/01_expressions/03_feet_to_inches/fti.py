INCHES_PER_FOOT = 12

def convert_feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

def main():
    feet = float(input("Enter length in feet: "))
    inches = convert_feet_to_inches(feet)
    print(f"{feet} feet is equal to {inches} inches.")

if __name__ == "__main__":
    main()