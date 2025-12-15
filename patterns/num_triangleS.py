"""
Challenge 37: Increasing Sequential Number Pattern
1
12
123
1234
"""
def main():
    try:
        n = int(input("Enter number of rows: "))
        
        for i in range(1, n + 1):
            # Inner loop runs from 1 up to 'i'
            for j in range(1, i + 1):
                print(j, end="") # Print the Column Number
            print()
    except ValueError:
        print("Invalid input")        

if __name__ == "__main__":
    main()