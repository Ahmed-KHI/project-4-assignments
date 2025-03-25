def create_phonebook():
   
    contacts = {} 

    while True:
        name = input("Enter contact name (Press Enter to stop): ")
        if not name:
            break
        number = input("Enter phone number: ")
        contacts[name] = number

    return contacts


def display_contacts(contacts):

    print("\nPhonebook Contacts:")
    for name, number in contacts.items():
        print(f"{name} -> {number}")


def search_contact(contacts):

    while True:
        name = input("\nEnter name to find (Press Enter to exit): ")
        if not name:
            break
        print(f"{name}: {contacts.get(name, 'Not found in phonebook')}") 


def main():

    phonebook = create_phonebook()
    display_contacts(phonebook)
    search_contact(phonebook)


if __name__ == "__main__":
    main()