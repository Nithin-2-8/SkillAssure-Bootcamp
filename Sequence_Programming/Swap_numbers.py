"""
Coding Challenge 4: Swap Two Numbers

Description: 
    This program accepts two numbers, swaps their values, and displays
    the result.
Input:
    - First Number (A)
    - Second Number (B)
Output:
    - Swapped values of A and B.
"""

def swap_value(a,b):
    a,b=b,a
    return a,b
def main():
    print("Number Swapper")
    try:
        #input
        val1=input("Enter the 1st value: ")
        val2=input("Enter the 2nd value: ")
        print("Before Swapping")
        print(f"A = {val1}")
        print(f"B = {val2}")
        #logic
        new_val1,new_val2 = swap_value(val1,val2)
        #output
        print("After Swapping")
        print(f"A = {new_val1}")
        print(f"B = {new_val2}")
    except Exception as e:
        print(f"Unexpected error occured{e}")
if __name__ == "__main__":
    main()            