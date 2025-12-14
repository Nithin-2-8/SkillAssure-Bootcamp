"""
Challenge 22: Display Series 1, 4, 7, 12, 23...
Logic: Next number = Sum of previous 3 numbers.
"""
def main():
    try:
        n = int(input("How many terms (N)? "))
        
        # Initial seeds
        a, b, c = 1, 4, 7
        
        if n >= 1: print(a, end=" ")
        if n >= 2: print(b, end=" ")
        if n >= 3: print(c, end=" ")
        
        # Start loop from 4th term
        for i in range(4, n + 1):
            next_val = a + b + c
            print(next_val, end=" ")
            
            # Shift values to the left for the next iteration
            a = b
            b = c
            c = next_val
            
        print()
    except ValueError:
        print("Invalid input")    

if __name__ == "__main__":
    main()