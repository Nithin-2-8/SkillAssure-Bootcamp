"""
Challenge 60: Matrix Multiplication
Logic: Result[i][j] = Sum(A[i][k] * B[k][j])
"""
def get_matrix(name, r, c):
    print(f"Enter elements for Matrix {name} ({r}x{c}):")
    mat = []
    for i in range(r):
        row = []
        for j in range(c):
            row.append(int(input(f"[{i}][{j}]: ")))
        mat.append(row)
    return mat

def main():
    print("Matrix A Dimensions:")
    r1 = int(input("Rows: "))
    c1 = int(input("Cols: "))
    
    print("Matrix B Dimensions:")
    r2 = int(input("Rows: "))
    c2 = int(input("Cols: "))
    
    # Validation Rule: Cols of A must equal Rows of B
    if c1 != r2:
        print("Error: Matrix Multiplication not possible. Cols of A must match Rows of B.")
        return

    # Input Matrices
    mat_a = get_matrix("A", r1, c1)
    mat_b = get_matrix("B", r2, c2)
    
    # Initialize Result Matrix (Size: r1 x c2) with zeros
    result = [[0 for _ in range(c2)] for _ in range(r1)]
    
    # Multiplication Logic 
    for i in range(r1):           # Iterate through Rows of A
        for j in range(c2):       # Iterate through Cols of B
            for k in range(c1):   # Iterate through common dimension
                result[i][j] += mat_a[i][k] * mat_b[k][j]
                
    print("\nResultant Matrix:")
    for row in result:
        print(row)

if __name__ == "__main__":
    main()