def sum_numbers(num_list: list[int]) -> int:

    return sum(num_list) 

def main():
    numbers = [1, 2, 3, 4, 5]  
    total = sum_numbers(numbers) 
    print(f"The sum of the numbers is: {total}") 

if __name__ == '__main__':
    main()