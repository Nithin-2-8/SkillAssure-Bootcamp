"""
Challenge 23: Display Series 1, 5, 9, 13, 21, 25, 29, 37...
Logic: Start at 1, add 4 each time. 
Exception: Skip numbers 17, 33, 49... (Every 4th step involves a double jump or a skip).
"""
def main():
    try:
        n = int(input("Enter max value (N): "))
        
        current_num = 1
        
        print("Series:", end=" ")
        
        while current_num <= n:
            # Check if this is a number to be skipped
            # The skipped numbers are 17, 33, 49... 
            # pattern: 17 + (16 * k)
            
            is_skipped_number = False
            if current_num >= 17:
                if (current_num - 17) % 16 == 0:
                    is_skipped_number = True
            
            if not is_skipped_number:
                print(current_num, end=" ")
                
            # Standard increment
            current_num += 4
            
        print()
    except ValueError:
        print("Invalid input")    

if __name__ == "__main__":
    main()