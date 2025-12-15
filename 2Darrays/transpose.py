"""
Challenge 58: Matrix Transpose

"""
def main():
    rows = int(input("Enter Rows: "))
    cols = int(input("Enter Cols: "))
    
    # 1. Input Matrix
    matrix = []
    print("Enter Matrix Elements:")
    for i in range(rows):
        r = []
        for j in range(cols):
            r.append(int(input(f"[{i}][{j}]: ")))
        matrix.append(r)
        
    # 2. Transpose Logic
    
    transpose = []
    for j in range(cols):
        new_row = []
        for i in range(rows):            
            new_row.append(matrix[i][j])
        transpose.append(new_row)
        
    # 3. Display
    print("\nOriginal Matrix:")
    for r in matrix: print(r)
    
    print("\nTranspose Matrix:")
    for r in transpose: print(r)

if __name__ == "__main__":
    main()