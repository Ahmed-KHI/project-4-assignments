def main():
    curr_value = int(input("Enter a number: ")) 
    result = []  

    while curr_value < 100:
        curr_value *= 2  
        result.append(str(curr_value)) 

    print(" ".join(result))  

if __name__ == "__main__":
    main()