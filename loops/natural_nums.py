"""
Challenge 17: Display the Series 1, 2, 3, 4, 5... N
"""
def main():
    try:
        n = int(input("Enter value of N: "))
        
        # Use a for loop to iterate from 1 to N 
        for i in range(1, n + 1):
            print(i, end=" ")
            
        print() # New line at the end
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()