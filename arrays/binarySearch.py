"""
Challenge 54: Binary Search
The array MUST be sorted first.

"""
def main():
    try:
        # 1. Setup Sorted Array
        n = int(input("Enter size of array: "))
        arr = []
        print(f"Enter {n} numbers:")
        for i in range(n):
            arr.append(int(input(f"Element {i+1}: ")))        
        
        arr.sort()
        print(f"Sorted Array (Required for Binary Search): {arr}")
        
        # 2. Input Target
        target = int(input("\nEnter number to search for: "))
        
        # 3. Binary Search Logic
        low = 0
        high = n - 1
        found = False
        
        while low <= high:
            mid_index = (low + high) // 2
            mid_value = arr[mid_index]
            
            if mid_value == target:
                print(f"Success! Found {target} at index {mid_index}.")
                found = True
                break
            elif target < mid_value:
                # Target is in the left half
                high = mid_index - 1
            else:
                # Target is in the right half
                low = mid_index + 1
                
        if not found:
            print("Element not found.")
    except ValueError:
        print("Invalid input")        

if __name__ == "__main__":
    main()