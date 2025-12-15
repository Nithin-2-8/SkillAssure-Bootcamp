"""
Challenge 35: Increasing Star Pattern
*
**
***
****
"""
def main():
    try:
        n = int(input("Enter number of rows: "))
        
        # Outer Loop: Controls Row Number (1 to N)
        for i in range(1, n + 1):
            
            # Inner Loop: Controls how many stars to print
            # It runs 'i' times. If i is 3, it prints 3 stars.
            for j in range(i):
                print("*", end="")
                
            print() # New line after finishing the row
    except ValueError:
        print("Invalid input")        

if __name__ == "__main__":
    main()