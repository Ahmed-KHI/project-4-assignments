MAX_TERM_VALUE = 10000  

def main():
    fib_sequence = []  
    a, b = 0, 1  
    
    while a <= MAX_TERM_VALUE:
        fib_sequence.append(a)
        a, b = b, a + b  

    print(" ".join(map(str, fib_sequence)))  

if __name__ == '__main__':
    main()