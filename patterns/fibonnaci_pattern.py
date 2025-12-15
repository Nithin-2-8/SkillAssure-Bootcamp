"""
Challenge 38: Fibonacci Series Pattern
1
1 2
3 5 8
13 21 34 55
"""
def main():
    try:
        n = int(input("Enter number of rows: "))
        
        # Initialize first two Fibonacci numbers
        a, b = 1, 1
        
        # Reset a, b for the start
        a, b = 0, 1 
        
        for i in range(1, n + 1):
            for j in range(i):
                # Calculate next fib number
                # Logic to print b, then update
                if i == 1 and j == 0:
                    print(1, end=" ")
                    a, b = 1, 1 # Reset for the standard sequence start
                else:
                    curr = a + b
                    print(curr, end=" ")
                    a = b
                    b = curr
                    
            print() # New line
    except ValueError:
        print("Invalid input")    

if __name__ == "__main__":
    main()