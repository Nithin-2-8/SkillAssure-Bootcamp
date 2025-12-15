"""
Challenge 42: Generate Series 1, -5, 9, -13, 17...
Absolute value increases by 4 (1, 5, 9, 13)
Sign flips every iteration (+, -, +, -)

"""
def main():
    try:
        n = int(input("Enter number of terms (N): "))
        
        current_val = 1
        sign = 1  # 1 for positive, -1 for negative
        
        for _ in range(n):
            # Calculate term: value * sign
            term = current_val * sign
            print(term, end=", ")
            
            # Prepare for next loop
            current_val += 4  # Increase magnitude by 4
            sign = sign * -1  # Flip the sign
            
        print()
    except ValueError:
        print("Invalid input")    

if __name__ == "__main__":
    main()