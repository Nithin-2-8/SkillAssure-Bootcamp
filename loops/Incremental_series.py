"""
Challenge 20: Display Series 1, 2, 4, 7, 11, 16...
Logic: The gap between numbers increases by 1 each step.
"""
def main():
    try:
        n = int(input("How many terms? "))
    
        current_num = 1
        gap = 0  # The amount we add starts at 0
    
        for i in range(n):
            current_num = current_num + gap
            print(current_num, end=" ")
        
            # Prepare the gap for the NEXT number
            if i == 0:
                gap = 1 # Special case to jump from 1st term to 2nd term
            else:
                gap += 1 # Increase the gap size

        print()
    except ValueError:
        print("Invalid input")    

if __name__ == "__main__":
    main()