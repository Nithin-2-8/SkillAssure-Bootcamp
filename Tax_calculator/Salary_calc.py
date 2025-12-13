"""
Hackathon: Tax Calculator - Challenge 11
Objective: Basic Input and Salary Calculation.
"""

def get_float_input(prompt):
    #to ensure the user gets valid positive number
    while True:
        try:
            value = float(input(prompt))
            if value >= 0:
                return value
            print("Error: Value cannot be negative.")
        except ValueError:
            print("Error: Please enter a valid number.")

def main():
    print("GlobalNext Solutions: Salary Calculator")
    
    # CAPTURE EMPLOYEE DETAILS 
    # Validation: Ensure name is not empty
    while True:
        emp_name = input("Enter Employee Name: ").strip()
        if emp_name.replace(" ", "").isalpha():
            break
        print("Error: Name must contain alphabets only.")

    emp_id = input("Enter Employee ID: ").strip()

    # CAPTURE SALARY COMPONENTS
    basic_salary = get_float_input("Enter Basic Monthly Salary (Rs.): ")
    special_allowances = get_float_input("Enter Special Allowances (Rs.): ")
    bonus_percentage = get_float_input("Enter Bonus Percentage (%): ")

    # CALCULATIONS
    # Gross Monthly Salary = Basic + Allowances
    gross_monthly_salary = basic_salary + special_allowances
    
    # Calculate Annual Base (before bonus)
    annual_base_salary = gross_monthly_salary * 12
    
    # Calculate Bonus Amount
    # Logic: Bonus is a percentage of the annual salary derived from monthly components
    bonus_amount = annual_base_salary * (bonus_percentage / 100)
    
    # Annual Gross Salary = (Gross Monthly * 12) + Bonus
    annual_gross_salary = annual_base_salary + bonus_amount

    #4. DISPLAY OUTPUT 
    print("\n")
    print(f"SALARY SLIP: {emp_name.upper()} ({emp_id})")
    print(f"Basic Salary (Monthly):    Rs. {basic_salary:,.2f}")
    print(f"Special Allowances:        Rs. {special_allowances:,.2f}")
    print(f"Gross Monthly Salary:      Rs. {gross_monthly_salary:,.2f}")
    print(f"Annual Base Salary:        Rs. {annual_base_salary:,.2f}")
    print(f"Annual Bonus ({bonus_percentage}%):       Rs. {bonus_amount:,.2f}")
    print(f"ANNUAL GROSS SALARY:       Rs. {annual_gross_salary:,.2f}")

if __name__ == "__main__":
    main()