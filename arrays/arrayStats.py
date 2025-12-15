"""
Challenges 45 - 48: Arrays (Levels 0-3)
Objectives:
1. Accept N numbers.
2. Find Sum.
3. Find Minimum.
4. Find Maximum.
"""

def main():
    #  LEVEL 0: Accept N elements (Challenge 45)    
    try:
        n = int(input("Enter the size of the array (N): "))
        arr = [] # Initialize empty list
        
        print(f"Please enter {n} numbers:")
        for i in range(n):
            val = int(input(f"Element {i+1}: "))
            arr.append(val)
            
        print(f"\nYour Array: {arr}")
        
        #  LEVEL 1: Find Sum (Challenge 46) 
        total_sum = 0
        for num in arr:
            total_sum += num
            
        print(f"Sum of elements:     {total_sum}")

        #  LEVEL 2 & 3: Find Min and Max (Challenge 47 & 48)        
        if n > 0:
            min_val = arr[0]
            max_val = arr[0]
            
            for num in arr:
                if num < min_val:
                    min_val = num
                if num > max_val:
                    max_val = num
            
            print(f"Minimum Value:       {min_val}")
            print(f"Maximum Value:       {max_val}")
        else:
            print("Array is empty, cannot find Min/Max.")

    except ValueError:
        print("Invalid input. Please enter integers.")

if __name__ == "__main__":
    main()