"""
Challenge 6: Check if a number is Even or Odd
"""
def main():
    try:
        num = int(input("Enter a number: "))
        
        if num % 2 == 0:
            print(f"{num} is an EVEN number.")
        else:
            print(f"{num} is an ODD number.")
            
    except ValueError:
        print("Invalid input. Please enter a whole number.")

if __name__ == "__main__":
    main()