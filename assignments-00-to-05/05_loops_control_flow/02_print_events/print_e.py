def main():
    even_numbers = [num for num in range(0, 40, 2)] 
    print(" ".join(map(str, even_numbers)))  

if __name__ == "__main__":
    main()