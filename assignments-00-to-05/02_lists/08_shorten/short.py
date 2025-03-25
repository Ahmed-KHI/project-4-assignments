MAX_LENGTH = 3  

def shorten(lst):
   
    while len(lst) > MAX_LENGTH:
        removed_element = lst.pop()  
        print(removed_element)  

def get_lst():
    lst = []
    while True:
        elem = input("Please enter an element of the list or press enter to stop: ")
        if elem == "":  
            break
        lst.append(elem) 
    return lst

def main():
    lst = get_lst()  
    shorten(lst)  

if __name__ == '__main__':
    main()