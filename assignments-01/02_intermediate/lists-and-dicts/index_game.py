def create_list():
    """Creates and returns a list of fruits."""
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    return fruit_list

def print_length(fruit_list):
    """Prints the length of the list."""
    print(f"Length of the list: {len(fruit_list)}")

def add_mango(fruit_list):
    """Adds 'mango' at the end of the list and prints it."""
    fruit_list.append('mango')
    print("Updated list:", fruit_list)

def access_element(lst, index):
    """Returns the element at the given index or an error message."""
    if 0 <= index < len(lst):
        return lst[index]
    return "Index out of range!"

def modify_element(lst, index, new_value):
    """Modifies the element at the given index or returns an error message."""
    if 0 <= index < len(lst):
        lst[index] = new_value
        return f"Updated list: {lst}"
    return "Index out of range!"

def slice_list(lst, start, end):
    """Returns a sliced list from start to end index."""
    if 0 <= start < len(lst) and 0 <= end <= len(lst):
        return lst[start:end]
    return "Invalid index range!"

def main():
    fruit_list = create_list()
    print_length(fruit_list)
    add_mango(fruit_list)
    
    fruit_list = fruit_list 
    
    while True:
        print("\nChoose an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            index = int(input("Enter index to access: "))
            print("Element:", access_element(fruit_list, index))
        
        elif choice == "2":
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            print(modify_element(fruit_list, index, new_value))
        
        elif choice == "3":
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            print("Sliced list:", slice_list(fruit_list, start, end))
        
        elif choice == "4":
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()