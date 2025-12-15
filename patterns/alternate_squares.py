"""
Challenge 39: Pattern of Perfect Squares with Alternating Signs
1
-4 9
-16 25 -36
"""
def main():
    try:
        n = int(input("Enter number of rows: "))
        
        count = 1 # We start squaring from 1
        
        for i in range(1, n + 1):
            for j in range(i):
                square = count * count
                
                # Apply Sign Logic: Even numbers are negative
                if count % 2 == 0:
                    print(f"-{square}", end=" ")
                else:
                    print(f"{square}", end=" ")
                    
                count += 1 # Move to next number for next iteration
                
            print()
    except ValueError:
        print("Invalid input")        

if __name__ == "__main__":
    main()