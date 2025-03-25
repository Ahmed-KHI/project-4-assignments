def get_numbers_from_user():

    numbers = []
    while True:
        user_input = input("Enter a number (press Enter to stop): ")
        
        if user_input == "":
            break
        
        numbers.append(int(user_input))
    
    return numbers

def count_occurrences(numbers_list):

    count_dict = {}
    for number in numbers_list:
        count_dict[number] = count_dict.get(number, 0) + 1
    
    return count_dict

def display_counts(count_dict):

    for number, count in count_dict.items():
        print(f"{number} appears {count} times.")

def main():

    user_numbers = get_numbers_from_user()
    occurrences = count_occurrences(user_numbers)
    display_counts(occurrences)

if __name__ == '__main__':
    main()