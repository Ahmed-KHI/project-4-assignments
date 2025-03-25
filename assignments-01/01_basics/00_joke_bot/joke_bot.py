PROMPT = "Tell me what you want: "
JOKE = "Here’s a joke for you! Sophia is heading to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why, and Sophia replies: 'because they had eggs.'"
SORRY = "Oops! I can only tell jokes."

def main():
    response = input(PROMPT).strip().capitalize() 

    if response == "Joke": 
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()