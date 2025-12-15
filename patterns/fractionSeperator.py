"""
Challenge 43: Separate Whole and Fraction values

"""
import math

def main():
    try:
        num = float(input("Enter a decimal number (e.g., 12.45): "))                
        whole_part = int(num)
        fraction_part = num - whole_part
        print(f"Original Number: {num}")
        print(f"Whole Part:      {whole_part}")
        print(f"Fraction Part:   {fraction_part:.4f}") 
        
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()