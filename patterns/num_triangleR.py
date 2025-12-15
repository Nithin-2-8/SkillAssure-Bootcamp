"""
Challenge 36: Increasing Repeated Number Pattern
1
22
333
4444
"""
def main():
    try:
        n = int(input("Enter number of rows: "))
        
        for i in range(1, n + 1):
            for j in range(i):
                print(i, end="") # Print the Row Number
            print()
    except ValueError:
        print("Invalid input")        

if __name__ == "__main__":
    main()