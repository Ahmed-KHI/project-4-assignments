def main():
    
    set1 = float(input("What is the length of side 1? "))
    set2 = float(input("What is the length of side 2? "))
    set3 = float(input("What is the length of side 3? "))

    perimeter = set1 + set2 + set3

    print(f"The perimeter of the triangle is {perimeter}")

if __name__ == "__main__":
    main()