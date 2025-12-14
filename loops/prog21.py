"""
Challenge 21: Display Series 1, 4, 9, 25, 36, 49, 81...
Logic: Squares of natural numbers (n^2), but skip if n is divisible by 4.
"""
def main():
    try:
        n = int(input("Enter number of terms to check: "))
        
        count = 0
        i = 1
        print("Series:", end=" ")
        for i in range(1, n + 1):
            
            # The pattern skips 16 (4^2), 64 (8^2), etc.
            if i % 4 == 0:
                continue  # Skip this iteration
            
            print(i*i, end=" ")
            
        print()
        
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()