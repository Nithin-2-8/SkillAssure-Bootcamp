"""
Challenges 52 & 53: Reverse and Sort Array

"""
def main():
    try:
        # Setup (Level 0) 
        n = int(input("Enter size of array: "))
        arr = []
        print(f"Enter {n} numbers:")
        for i in range(n):
            arr.append(int(input(f"Element {i+1}: ")))
        
        #  LEVEL 1: Reverse Array (Challenge 52)    
        reversed_arr = arr[:] 
        start = 0
        end = n - 1
        
        while start < end:
            # Swap
            reversed_arr[start], reversed_arr[end] = reversed_arr[end], reversed_arr[start]
            start += 1
            end -= 1
            
        print(f"\nOriginal Array: {arr}")
        print(f"Reversed Array: {reversed_arr}")
        
        # LEVEL 2: Sort Array (Challenge 53) 
        # Logic: Bubble Sort Algorithm
        print("\nSort Menu:")
        print("1. Ascending (Small -> Large)")
        print("2. Descending (Large -> Small)")
        choice = input("Enter choice (1 or 2): ")
        
        sorted_arr = arr[:] 
        
        # Bubble Sort Loop
        for i in range(n):
            for j in range(0, n - i - 1):
                should_swap = False
                
                if choice == '1': # Ascending
                    if sorted_arr[j] > sorted_arr[j + 1]:
                        should_swap = True
                elif choice == '2': # Descending
                    if sorted_arr[j] < sorted_arr[j + 1]:
                        should_swap = True
                
                if should_swap:
                    # Swap elements
                    sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                    
        print(f"Sorted Array:   {sorted_arr}")
    except ValueError:
        print("Invalid input")    

if __name__ == "__main__":
    main()