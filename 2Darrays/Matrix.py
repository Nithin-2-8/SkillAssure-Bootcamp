"""
Challenges 55, 56, 57: 2D Array Operations
Objectives:
1. Create a Matrix (M x N).
2. Display Row-wise.
3. Calculate Sum of all elements.
4. Search for an element.
"""

def main():
    try:
        #  CHALLENGE 55: Create & Display 
        print(" Step 1: Create Matrix ")
        rows = int(input("Enter number of Rows (M): "))
        cols = int(input("Enter number of Columns (N): "))
        
        # Initialize empty matrix
        matrix = []
        
        print(f"Enter {rows * cols} numbers:")
        for i in range(rows):
            current_row = []
            for j in range(cols):
                val = int(input(f"Element at [{i}][{j}]: "))
                current_row.append(val)
            matrix.append(current_row)
            
        print("\n Matrix Display ")
        # Logic to print in grid format
        for i in range(rows):
            for j in range(cols):
                print(matrix[i][j], end="\t") 
            print() # New line after every row

        #  CHALLENGE 56: Sum of Elements 
        print("\n Step 2: Sum Calculation ")
        total_sum = 0
        for i in range(rows):
            for j in range(cols):
                total_sum += matrix[i][j]
                
        print(f"Total Sum of Matrix: {total_sum}")

        #  CHALLENGE 57: Search Element 
        print("\n--- Step 3: Search ---")
        target = int(input("Enter value to search: "))
        found = False
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == target:
                    print(f"Success! Found {target} at Row {i}, Column {j}")
                    found = True
                   
        
        if not found:
            print("Element not found.")

    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()