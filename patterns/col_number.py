"""
Challenge 36 : Fixed Column Numbers
12345
12345
12345
"""
def main():
    try:
        n = int(input("Enter number of rows: "))
        
        for i in range(n):
            for j in range(1, 6):   # Columns 1 to 5
                print(j, end="")    # Print the Column Number
            print()
    except ValueError:
        print("Invalid input")        

if __name__ == "__main__":
    main()