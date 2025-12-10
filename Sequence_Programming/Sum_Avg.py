"""
--------------------------------------------------------------------------------
Coding Challenge 1: Sum and Average of Two Variables
--------------------------------------------------------------------------------

Description: 
    This program accepts two numbers from the user, calculates their sum 
    and average, and displays the results.

Input:
    - Two numeric values (integer or float).
Output:
    - Sum of the two numbers.
    - Average of the two numbers.
--------------------------------------------------------------------------------
"""

def calculate_metrics(num1, num2):
    """
    Performs the mathematical logic.    
    """
    total_sum = num1 + num2
    average = total_sum / 2
    return total_sum, average

def main():
    print("--- Sum and Average Calculator ---")
    
    # 1. INPUT BLOCK
    # We use float() to handle both whole numbers (10) and decimals (10.5)
    # Using try-except to ensure the program doesn't crash if user types text (Zero Defects)
    try:
        input_1 = input("Enter the first number: ")
        number_1 = float(input_1)
        
        input_2 = input("Enter the second number: ")
        number_2 = float(input_2)

        # 2. LOGIC BLOCK
        result_sum, result_avg = calculate_metrics(number_1, number_2)

        # 3. OUTPUT BLOCK        
        print(f"\nResults:")
        print(f"Sum:     {result_sum}")
        print(f"Average: {result_avg}")

    except ValueError:
        print("\n[!] Error: Invalid input. Please enter numeric values only.")

# This block ensures the code runs only when executed directly
if __name__ == "__main__":
    main()

"""
--------------------------------------------------------------------------------
TEST CASES (Quality Assurance)
--------------------------------------------------------------------------------
1. Positive Case (Integers)
   Input: 10, 20
   Expected Output: Sum=30.0, Average=15.0
   
2. Positive Case (Decimals)
   Input: 10.5, 20.5
   Expected Output: Sum=31.0, Average=15.5

3. Negative Case (Invalid Input)
   Input: "Ten", 20
   Expected Output: Error message displayed (Program does not crash)

4. Edge Case (Zero)
   Input: 0, 0
   Expected Output: Sum=0.0, Average=0.0
--------------------------------------------------------------------------------
"""