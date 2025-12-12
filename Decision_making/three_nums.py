"""
Challenge 8: Find the largest of three numbers
"""
def main():
    print("Enter three numbers to find the largest.")
    try:
        n1 = float(input("First number: "))
        n2 = float(input("Second number: "))
        n3 = float(input("Third number: "))
        
        # Logic using if-elif-else
        if n1 >= n2 and n1 >= n3:
            largest = n1
        elif n2 >= n1 and n2 >= n3:
            largest = n2
        else:
            largest = n3
            
        print(f"The largest number is: {largest}")
        
    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()