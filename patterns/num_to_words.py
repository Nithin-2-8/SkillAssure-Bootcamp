"""
Challenge 41: Convert Number to Words
Example: 270 -> Two Seven Zero

"""
def main():
    try:
        num_str = input("Enter a number: ")
        
        # Mapping digits to words
        digit_map = {
            '0': "Zero", '1': "One", '2': "Two", '3': "Three", '4': "Four",
            '5': "Five", '6': "Six", '7': "Seven", '8': "Eight", '9': "Nine"
        }
        
        print("Output:", end=" ")
        
        for char in num_str:
            if char in digit_map:
                print(digit_map[char], end=" ")
            else:
                # Handle negative signs or decimals if entered
                if char == '-':
                    print("Minus", end=" ")
                elif char == '.':
                    print("Point", end=" ")
                    
        print()
        
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()