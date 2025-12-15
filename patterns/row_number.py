"""
Challenge 35: Repeated Row Numbers
11111
22222
33333
"""
def main():
    try:
        n = int(input("Enter number of rows: "))
        
        for i in range(1, n + 1):
            for j in range(5):
                print(i, end="")    # Print the Row Number
            print()
    except ValueError:
        print("Invalid input")        

if __name__ == "__main__":
    main()