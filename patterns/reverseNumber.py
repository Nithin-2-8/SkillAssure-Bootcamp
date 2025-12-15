"""
Challenge 44: Reverse of a number
Last Digit = num % 10
Reverse = (Reverse * 10) + Last Digit

"""
def main():
    try:
        num = int(input("Enter a number to reverse: "))
        original_num = num 
        
        reverse_val = 0
        
        while num > 0:
            remainder = num % 10
            reverse_val = (reverse_val * 10) + remainder
            num = num // 10
            
        print(f"Original: {original_num}")
        print(f"Reversed: {reverse_val}")
        
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()