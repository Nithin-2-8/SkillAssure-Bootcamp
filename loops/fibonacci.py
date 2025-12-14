"""
Challenge 24: Fibonacci Series (1, 1, 2, 3, 5, 8...)
Logic: Next = Prev + Current
"""
def main():
    try:
        n = int(input("How many terms? "))
        
        a, b = 1, 1
        
        if n >= 1: print(a, end=" ")
        if n >= 2: print(b, end=" ")
        
        for i in range(3, n + 1):
            next_val = a + b
            print(next_val, end=" ")
            
            # Shift
            a = b
            b = next_val
            
        print()
    except ValueError:
        print("Invalid input")    

if __name__ == "__main__":
    main()