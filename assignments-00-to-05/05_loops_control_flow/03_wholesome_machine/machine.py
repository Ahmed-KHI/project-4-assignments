AFFIRMATION = "I am capable of doing anything I put my mind to."

def main():
    while True:  
        user_input = input("Type the following affirmation:\n" + AFFIRMATION + "\n")  
        
        if user_input == AFFIRMATION:
            print("Great! You got it right. 😊")  
            break  
        else:
            print("Oops! That wasn't quite right. Try again! 🔄")  

if __name__ == "__main__":
    main()