def double_numbers(numbers: list[int]) -> list[int]:

    return [num * 2 for num in numbers]  

def main():
    numbers = [1, 2, 3, 4]  
    doubled_list = double_numbers(numbers) 
    print("Original List:", numbers)
    print("Doubled List:", doubled_list) 

if __name__ == '__main__':
    main()