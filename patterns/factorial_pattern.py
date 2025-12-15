"""
Challenge 40: Pattern of Factorials in N Rows
1
1 2
6 24 120
"""
def main():
    try:
        n = int(input("Enter number of rows: "))
        # Start at 0! which is 1
        index = 0
        current_factorial = 1
        
        for i in range(1, n + 1):
            for j in range(i):
            
                # handle index 0 separately or use logic
                
                if index == 0:
                    current_factorial = 1
                else:
                    current_factorial = current_factorial * index
                
                print(current_factorial, end=" ")
                index += 1
                
            print()
    except ValueError:
        print("Invalid input")        

if __name__ == "__main__":
    main()