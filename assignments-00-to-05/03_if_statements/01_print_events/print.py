def main():
    even_numbers = []  
    for i in range(20):
        even_numbers.append(i * 2) 

    print(*even_numbers) 


if __name__ == "__main__":
    main()