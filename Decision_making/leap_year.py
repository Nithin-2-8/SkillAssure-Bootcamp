"""
Challenge 9: Leap Year Checker
"""
def main():
    try:
        year = int(input("Enter a year (e.g., 2024): "))
        
        # Logic: (Divisible by 4 AND NOT 100) OR (Divisible by 400)
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(f"{year} is a LEAP YEAR.")
        else:
            print(f"{year} is NOT a leap year.")
            
    except ValueError:
        print("Invalid input. Please enter a valid year.")

if __name__ == "__main__":
    main()