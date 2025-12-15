"""
Challenges 49 - 50: Search and Count Logic
Objectives:
1. Search for a specific element .
2. Count Odd and Even numbers.
"""

def main():
    try:
        # 1. Setup the array 
        n = int(input("Enter size of array: "))
        arr = []
        print(f"Enter {n} numbers:")
        for i in range(n):
            arr.append(int(input(f"Element {i+1}: ")))

        # LEVEL 4: Search for Element (Challenge 49) 
        target = int(input("\nEnter element to search for: "))
        found = False
        
        # Linear Search Logic
        for index, num in enumerate(arr):
            if num == target:
                print(f"Success! Number {target} found at index {index}.")
                found = True
                break 
                
        if not found:
            print(f"Number {target} not found in the array.")

        # LEVEL 5: Odd/Even Count (Challenge 50) 
        odd_count = 0
        even_count = 0
        
        for num in arr:
            if num % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
                
        print("-" * 30)
        print(f"Even Numbers count: {even_count}")
        print(f"Odd Numbers count:  {odd_count}")
    except ValueError:
        print("Invalid input.")    

if __name__ == "__main__":
    main()