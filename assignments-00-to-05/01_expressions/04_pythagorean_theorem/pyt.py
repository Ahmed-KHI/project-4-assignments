import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

def main():
    side1 = float(input("Enter the length of first perpendicular side: "))
    side2 = float(input("Enter the length of second perpendicular side: "))

    hypotenuse = calculate_hypotenuse (side1, side2)

    print(f"The length of hypotenuse is: {hypotenuse:.2f}")

if __name__ =="__main__":
    main()