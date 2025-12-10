"""
--------------------------------------------------------------------------------
Coding Challenge 2: Simple Interest Calculator
--------------------------------------------------------------------------------
Description: 
    This program calculates Simple Interest based on Principal amount, 
    Rate of interest, and Time period.

Formula: Simple Interest = (Principal * Rate * Time) / 100

Input:
    - Principal Amount (P): The money lent or invested.
    - Rate of Interest (R): Annual rate in percentage.
    - Time Period (T): Time in years.
Output:
    - Calculated Simple Interest value.
    - Total Amount value. 
--------------------------------------------------------------------------------
"""
def calculate_simple_interest(principle,rate,time):
    #Formula to calculate simple interest
    interest = (principle*rate*time) / 100
    return interest
def main():
    print("Simple interest Calculator")
    try:
        # Take inputs
        p_input = input("Enter the principle amount(Rs): ")
        principle = float(p_input)
        rate = float(input("Enter the rate(%): "))
        time = float(input("Enter the Time period(years): "))
        #Check for Negative values
        if principle<0 or rate<0 or time<0:
            print("Error inputs cannot be negative values")
            return
        #logic
        simple_interest = calculate_simple_interest(principle,rate,time)
        #output
        print(f"The Simple interest is {simple_interest:.2f} Rs")
        print(f"The total Amount is {(principle+simple_interest):.2f} Rs")
    except ValueError:
        print("Error:Invalid input.Enter numerical values only")

if __name__ == "__main__":
    main()             
            