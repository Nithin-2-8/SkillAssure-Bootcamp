"""
Challenge 34: Square Star Pattern
*****
*****
*****
"""
def main():
    try:
        n = int(input("Enter number of rows: "))
        
        for i in range(n):          # Outer Loop: Controls Rows
            for j in range(5):      # Inner Loop: Controls Columns (Fixed at 5)
                print("*", end="")
            print()                 # Move to next line after printing 5 stars
    except ValueError:
        print("Invalid input")
if __name__ == "__main__":
    main()