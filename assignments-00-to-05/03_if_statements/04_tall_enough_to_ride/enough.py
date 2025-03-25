def main():
    min_height = 50 

    while True:
        user_input = input("How tall are you? (Press Enter to exit) ")
        
        if not user_input: 
            print("Exiting the program. Goodbye!")
            break

        height = float(user_input)

        if height >= min_height:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

if __name__ == "__main__":
    main()