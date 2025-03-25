def get_first_element(lst):
  
    print(lst[0])

def get_lst():
   
    lst = []
    while True:
        elem = input("Please enter an element of the list or press enter to stop: ")
        if elem == "":
            break
        lst.append(int(elem)) 
    return lst

def main():

    lst = get_lst()
    get_first_element(lst)

if __name__ == '__main__':
    main()